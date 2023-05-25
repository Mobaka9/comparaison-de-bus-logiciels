import json
from time import sleep

from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'employees',
        auto_offset_reset='latest',
        bootstrap_servers=['localhost:9092'],
        api_version=(0, 10),
        consumer_timeout_ms=10000
    )
    for msg in consumer:
        print(msg.value)
        sleep(3)

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