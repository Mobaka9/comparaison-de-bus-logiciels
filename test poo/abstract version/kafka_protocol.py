from kafka import KafkaProducer
from abstract_protocol import AbstractProtocol
from kafka import KafkaConsumer
import time

class KafkaProtocol(AbstractProtocol):
    def __init__(self, com):
        self.kafka_producer = None
        self.consumer = None
        
        self.com = com
        self.plt_data = []
        self.id = 0
        self.wait = True

    def initialize(self):
        
        if self.com == "PUB":
            self.kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
        else:
            
            topics = ['10001','10002']
            self.consumer = KafkaConsumer(
                
                auto_offset_reset='latest',
                bootstrap_servers=['localhost:9092'],
                api_version=(0, 10),
                consumer_timeout_ms=10000
            )
            self.consumer.subscribe(topics)

    def send_message(self, message, topic):
        try:
            string_bytes = str.encode(message)
            self.kafka_producer.send(topic, value=string_bytes)
            self.kafka_producer.flush()
        except Exception as ex:
            print(str(ex))

    
    def receive_message(self, message_count):
        for msg in self.consumer:
            if msg.topic == '10001':
                self.id += 1
                t1 = time.time()
                tmp = [self.id, msg.value.decode('utf-8'), t1]
                self.plt_data.append(tmp)
                #print("fct "+msg.value.decode('utf-8'))
            elif msg.topic == '10002':
                self.wait = False
        
        
        while self.wait:
            pass            
        return self.plt_data
