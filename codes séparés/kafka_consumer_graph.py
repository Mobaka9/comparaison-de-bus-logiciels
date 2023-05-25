import json
from time import sleep
import sys
import time
import matplotlib.pyplot as plt
from statistics import mean
from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'test_topic',
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
        t1 = time.time()
        t0 = float(msg.value.decode('utf-8').split("=")[1])
        time_interval = t1-t0
        
        plt_data.append(time_interval)
        print(msg.value)
        print(i)
        
        if len(plt_data) == total_msgs:

            # Dessiner le graphique
            plt.plot(range(1, total_msgs+1), plt_data, 'ro')
            plt.xlabel('Message number')
            plt.ylabel('Time (s)')
            plt.title('Time to receive each message')
            print("La moyenne est ", mean(plt_data))
            plt.title("temps moyens d'émission de "+str(total_msgs)+" messages longs avec apache kafka.")
            plt.show()
            plt.savefig("10 msgs courts.png")
            plt.close()
        

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