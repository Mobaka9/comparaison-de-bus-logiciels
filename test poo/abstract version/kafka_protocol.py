from kafka import KafkaProducer
from abstract_protocol import AbstractProtocol
from kafka import KafkaConsumer


class KafkaProtocol(AbstractProtocol):
    def __init__(self, com):
        self.kafka_producer = None
        self.consumer = None
        self.com = com

    def initialize(self):
        
        if self.com == "PUB":
            self.kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
        else:
            self.consumer = KafkaConsumer(
                'hello',
                auto_offset_reset='latest',
                bootstrap_servers=['localhost:9092'],
                api_version=(0, 10),
                consumer_timeout_ms=10000
            )

    def send_message(self, message):
        try:
            string_bytes = str.encode(message)
            self.kafka_producer.send('hello', value=string_bytes)
            self.kafka_producer.flush()
        except Exception as ex:
            print(str(ex))

    def receive_message(self):
        for msg in self.consumer:
            
            
            #print("fct "+msg.value.decode('utf-8'))
            return msg.value.decode('utf-8')
            
            

        if self.consumer is not None:
            self.consumer.close()