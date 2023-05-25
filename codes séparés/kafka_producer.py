import json

from kafka import KafkaProducer


def publish_message(kafka_producer, topic_name, String):
    try:
        #key_bytes = str(employee['id']).encode('utf-8')

        string_bytes = str.encode(String)

        kafka_producer.send(topic_name, value=string_bytes)
        kafka_producer.flush()
        print('Message published successfully.')
    except Exception as ex:
        print(str(ex))


if __name__ == '__main__':
    kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    String = 'hello'
    
    publish_message(
            kafka_producer=kafka_producer,
            topic_name='employees',
            String=String
            
        )
    if kafka_producer is not None:
        kafka_producer.close()









'''
from kafka import KafkaProducer
import time

# Créer un producteur Kafka qui envoie des messages à l'adresse du broker
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
time.sleep(5)

# Envoyer un message à un sujet (topic) spécifique
producer.send('mon-sujet', b'Mon message de test!')
print('Message envoyé avec succès.')
'''