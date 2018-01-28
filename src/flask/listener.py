'''
Implementing a listener to Subscribe 250k channels (done this part in sendsub.py) to hub and listening to them.
Getting notification from hub when any changes happen to any of these channels in terms of number of videos,
video's titles, videos description. Then storing the chaanges into Redis.
'''
import flask
from flask import Flask, jsonify, render_template, request, redirect, url_for, abort, session
import redis, json
import re

app = Flask(__name__)

r = redis.StrictRedis(host='Public-DNS-of-Redis-Cluster', port=6379, db=0)

@app.route('/channels', methods = ['GET', 'POST'])
def channels():
    if request.method == 'POST':
        #When a a chaneg happens, we get a POST request. We pars the xml and get the chId, and all fields.
        #into a text file here and then represent the content to flask UI
        #put it in redis with a key like PUSH-chId just to recognize it from a normal channel id that comes from Poll based model
        doc = flask.request.data
        chId = re.search("<yt:channelId>.*</yt:channelId>", doc).group(0).split(">")[1].split("<")[0]
        publishDate = re.search("<published>.*</published>", doc).group(0).split(">")[1].split("<")[0]
        updateDate = re.search("<updated>.*</updated>", doc).group(0).split(">")[1].split("<")[0]
        chUri = re.search("<uri>.*</uri>", doc).group(0).split(">")[1].split("<")[0]
        
        #check the number of times we crawled a channel id using pull-based approach            
        with open("log.txt", "a") as t:
            t.write("channel {} got updated".format(chId))
                  
        r.set("*PUSH*"+chId, (updateDate, publishDate, chUri))
            

    #we reply with 200 OK a request body of exactly the string provided in the "hub.challenge" to hub to confirm subscription to hub. 
    if flask.request.method == 'GET':
        return flask.request.args.get('hub.challenge')
        

@app.route('/poll', methods = ('GET', 'POST'))
def lookupPoll():
    keys = r.keys()
    rows = {} #dictionary of lists
    counter = 0
    for key in keys[:100]:
        chId = key.decode("utf-8")
        viewCount = r.get(key).decode("utf-8").split("(")[1].split(",")[0]
        commentCount = r.get(key).decode("utf-8").split("(")[1].split(",")[1]
        subscribeCount = r.get(key).decode("utf-8").split("(")[1].split(",")[2]
        videoCount = r.get(key).decode("utf-8").split("(")[1].split(",")[3].split(")")[0]
        val = [chId, viewCount, commentCount, subscribeCount, videoCount]
        if key and b"*PUSH*" not in key: #it is poll based            
            rows[key] = val
    return render_template('home.html', rows = rows)

@app.route('/push', methods = ('GET', 'POST'))
def lookupPush():
    keys = r.keys()
    rows = {}
    for key in keys[:100]:
        chId = key.decode("utf-8")
        publishDate = r.get(key).decode("utf-8").split("(")[1].split(",")[0]
        updateDate = r.get(key).decode("utf-8").split("(")[1].split(",")[1]
        chUri = r.get(key).decode("utf-8").split("(")[1].split(",")[2]
        val = [chId, publishDate, updateDate, chUri]
        if key and b"*PUSH*" in key: #it is push based
            rows[key] = val
 
    return render_template('home.html', rows = rows)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
       
