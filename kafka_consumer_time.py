import json
from time import sleep
import sys
import time
import matplotlib.pyplot as plt
from statistics import mean
from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'hello',
        auto_offset_reset='latest',
        bootstrap_servers=['localhost:9092'],
        api_version=(0, 10),
        consumer_timeout_ms=10000
    )
    total_msgs = sys.argv[1]
    total_msgs = int(total_msgs)
    plt_data = []
    
    i=0
        
    for msg in consumer:
        i+=1
        
        
        #print(msg.value)
        #print(i)
        
        if "last message" in msg.value.decode('utf-8'):
            end_time = time.time()
            start_time = float(msg.value.decode('utf-8').split("=")[1])
            print("Temps total de communication : ", (end_time - start_time))
        

    if consumer is not None:
        consumer.close()
    

    



'''
from kafka import KafkaConsumer

# Créer un consommateur Kafka qui lit des messages à partir de l'adresse du broker
consumer = KafkaConsumer('mon-sujet', auto_offset_reset='earliest',
        bootstrap_servers=['localhost:9092'],
        api_version=(0, 10),
        consumer_timeout_ms=1000)

# Lire les messages à partir du sujet (topic) spécifié
for message in consumer:
    print(message.value)

if consumer is not None:
        consumer.close()
'''