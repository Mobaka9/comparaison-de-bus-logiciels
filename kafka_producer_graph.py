import json
import time
import sys
from kafka import KafkaProducer


def publish_message(kafka_producer, topic_name, msg):
    try:
        #key_bytes = str(employee['id']).encode('utf-8')

        string_bytes = str.encode(msg)

        kafka_producer.send(topic_name, value=string_bytes)
        kafka_producer.flush()
        print('Message published successfully.')
    except Exception as ex:
        print(str(ex))


if __name__ == '__main__':
    kafka_producer  = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    msg = 'hello'
    total_msgs = sys.argv[1]
    total_msgs = int(total_msgs)
    
    for i in range(total_msgs):
        start_time = time.time()
        msg = "hello ="+str(start_time)
        publish_message(
                kafka_producer=kafka_producer,
                topic_name='test_topic',
                msg=msg
                
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