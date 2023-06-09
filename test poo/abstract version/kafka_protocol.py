from kafka import KafkaProducer
from abstract_protocol import AbstractProtocol
from kafka import KafkaConsumer
import time
from time import sleep

class KafkaProtocol(AbstractProtocol):
    def __init__(self, com):
        self.kafka_producer = None
        self.consumer = None
        self.kafka_test = None
        self.com = com
        self.plt_data = []
        self.id = 0
        self.wait = True
        self.ready = False

    def initialize(self):
        
        if self.com == "PUB":
            self.kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
            '''self.kafka_test= KafkaConsumer(
                
                auto_offset_reset='latest',
                bootstrap_servers=['localhost:9092'],
                api_version=(0, 10),
                consumer_timeout_ms=10000
            )
            self.kafka_test.subscribe('start')'''
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

    def receiver_ready(self):
        self.kafka_test = KafkaConsumer(
            
            auto_offset_reset='latest',
            bootstrap_servers=['localhost:9092'],
            api_version=(0, 10),
            consumer_timeout_ms=10000
        )
        self.kafka_test.subscribe('start')
        print("start receive")
        while not self.ready:
            print("a")
            for msg in self.kafka_test:
                print("topic")
                if msg.topic == 'start':
                    print("start received")
                    self.ready = True
                    
        print("The receiver is ready")
        return self.ready
    
    def receive_message(self, message_count, queue):
        #self.kafka_test = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
        self.kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
        
        string_bytes = str.encode("receiver ready")
        self.kafka_producer.send('start', value=string_bytes)
        self.kafka_producer.flush()
        queue.put("RECEIVER_READY")
        for msg in self.consumer:
            if msg.topic == '10001':
                self.id += 1
                t1 = time.time()
                tmp = [self.id, msg.value.decode('utf-8'), t1]
                self.plt_data.append(tmp)
                #print("fct "+msg.value.decode('utf-8'))
            elif msg.topic == '10002':
                self.wait = False
            elif msg.topic == "start":
                return msg.value.decode('utf-8')
        
        
        while self.wait:
            pass            
        return self.plt_data
