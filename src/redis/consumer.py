from kafka import KafkaConsumer
import datetime
import redis

consumer = KafkaConsumer("my-topic", group_id = "my_group", bootstrap_servers='Public-DNS-Kafka-Cluster-Master-Node:9092')
r = redis.StrictRedis(host = 'Phblic-DNS-Redis-Cluster, port = 6379, db = 0)


#value: viewCount, commentCount, subscribeCount, videoCount, str(datetime.datetime.now())
#key: id

'''

Sample of row in Redis: chId ('5290041', '0', '11109', '1348', '2018-01-23 10:07:40.389227')
'''

for message in consumer:
    if (len (str(message.value).split("'")) > 1):
        chId = str(message.value).split("'")[1]
    else:
        chId = NOCH
        
    if (len (str(message.value).split("'")) > 5):
        viewCount = str(message.value).split("'")[5]
    else:
        viewCount = 0
        
    if (len (str(message.value).split("'")) > 9):
        commentCount = str(message.value).split("'")[9]
    else:
        commentCount = 0
        
    if  (len (str(message.value).split("'")) > 13):
        subscriberCount = str(message.value).split("'")[13]
    else:
        subscriberCount = 0
        
    if (len (str(message.value).split("'")) > 19):
        videoCount = str(message.value).split("'")[19]
    else:
        videoCount = 0

    r.set(chId, (viewCount, commentCount, subscriberCount, videoCount,str(datetime.datetime.now())))
    
                         
consumer.subscribe(['my-topic'])

