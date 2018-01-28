'''
In this progeam, I use Youtube API to get statistics [viewCount, commentCount, subscribeCount, videoCount] of 1 million youtube channels.
And each data will be streaming thru Kafka and the jason files will be processed in consumer thru Kafka stream.
'''
import requests
import re
import string
import json
import os , sys
import getopt
import traceback
import time
import datetime as dt
from kafka import KafkaProducer 
import csv


producer = KafkaProducer(bootstrap_servers='Public-DNS-Kafka-Cluster-Master-Node:9092')


#api key
KEY = "Your-API-KEY"

def get_channels_statistics(channels):
    url_api = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNELS}&key={YOUR_API_KEY}"
    url_call = url_api.format ( CHANNELS = ",".join(channels), YOUR_API_KEY = KEY)
    data = requests.get (url_call)
    items = data.json()['items']
    results = {}
    for i in items:
        channel_id = i['id']
        results[channel_id] = i['statistics']
    return results


#it gets all channel ids from csv file and insert in a list
def send_channels_statistics(filename):
    with open(filename, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            producer.send('my-topic', str(get_channels_statistics([row[0]])).encode())


if __name__ == '__main__':   
    file = "channels.csv"
    while True:
        last_time = dt.datetime.today().timestamp()
        send_channels_statistics(file)
        new_time = dt.datetime.today().timestamp()
        with open("log.txt", "a") as t:
            t.write("time to get 1000000 events from API: {}\n".format(new_time - last_time))
                
            
        
        
            
            
