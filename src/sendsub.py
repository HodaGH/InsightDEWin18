'''
Sending subscribing POSTS to hub. This is the first step: "Send the subscription request " in PubSubHubBub architecture.

Send the subscription request
To subscribe, send a form-encoded POST request to the hub with the following parameters:

hub.mode - The string "subscribe"
hub.topic - The URL with the content you are subscribing to, which was the value of the "self" link previously discovered
hub.callback - The URL that you want the hub to send notifications to, so it must be a publicly-accessible URL. It is a good idea to use a unique URL per subscription so that you know what feed is updated when you receive a notification.
The hub will reply with either 202 Accepted or 400 Bad Request. If there were any problems with the request, such as the subscriber attempting to subscribe to a topic that does not exist, the hub will return 400 Bad Request and a plain text description of the error. If the hub accepted the subscription request, it will return 202 Accepted and will then attempt to verify the subscription request.

We just sent subscribtion request to 250k channels. And got 202 ACCEPTED output 250k times.

This code can be run on local machine as first step.

hub = https://pubsubhubbub.appspot.com/subscribe

publisher = youtube

Subscriber = My code (flask web server)

'''
import requests
import csv

chlids = []

def subscribe():
    #have list of channels id in a csv file called channels located in the same directory with this .py script
    with open("channels.csv", encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            r = requests.post('https://pubsubhubbub.appspot.com/subscribe', data = {'hub.mode':'subscribe', 'hub.callback': 'http://public-DNS-of-Flask-webserver/channels', 'hub.topic':'https://www.youtube.com/xml/feeds/videos.xml?channel_id=%s'%row[0]})
            print(r.status_code)


subscribe()

