import zmq
from abstract_protocol import AbstractProtocol
import time
from time import sleep


class ZeroMQProtocol(AbstractProtocol):
    def __init__(self, port, com):
        self.port = int(port)
        self.socket = None
        self.com = com
        self.plt_data = []
        self.id = 0
        self.wait = True

    def initialize(self):
        context = zmq.Context()
        if self.com == "PUB":
            self.socket = context.socket(zmq.PUB)
            self.socket.setsockopt(zmq.SNDHWM, 2000000)
            self.socket.bind("tcp://*:%s" % self.port)
            sleep(3)

        else:
            self.socket = context.socket(zmq.SUB)
            self.socket.setsockopt(zmq.RCVHWM, 2000000)
            self.socket.connect("tcp://localhost:%s" % self.port)
        
        
        

    def send_message(self, message, topic):
        topic_message = str(topic) + "&" + str(message)  # Ajouter le topic au message
        self.socket.send_string(topic_message)



    def receive_message(self,message_count):
        topicfilter = "10001"
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "10002")

        for i in range(message_count+1):
            string = self.socket.recv()
            t1 = time.time()
            #topic, messagedata = string.split()
            topic, messagedata = string.decode('utf-8').split("&")
            #print(messagedata)
            
            if topic == "10001" :
                self.id+=1
                tmp= [self.id, messagedata,t1]
                self.plt_data.append(tmp)
            elif topic == "10002":
                print("2")
                self.wait=False
            
        while self.wait:
            pass
        #print(messagedata)
        #messagedata = messagedata.decode('utf-8')
        return(self.plt_data)

