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
        self.port_test = "5557"

    def initialize(self):
        context = zmq.Context()
        if self.com == "PUB":
            self.socket = context.socket(zmq.PUB)
            self.socket.setsockopt(zmq.SNDHWM, 2000000)
            self.socket.bind("tcp://*:%s" % self.port)
            

            #sleep(3)

        else:
            self.socket = context.socket(zmq.SUB)
            self.socket.setsockopt(zmq.RCVHWM, 2000000) 
            self.socket.connect("tcp://localhost:%s" % self.port)
            
        
          

    def send_message(self, message, topic):
        #sleep(0.0001)

        topic_message = str(topic) + "&" + str(message)  # Ajouter le topic au message
        self.socket.send_string(topic_message)



    def receive_message(self,message_count,queue):
        #initialisation
        """ context2 = zmq.Context()
        self.socket_test = context2.socket(zmq.PUB)
        self.socket_test.setsockopt(zmq.SNDHWM, 2000000)
        self.socket_test.bind("tcp://*:%s" % self.port_test)
        topic_message = "10000&receiver ready"  # Ajouter le topic au message
        print(topic_message)
        self.socket_test.send_string(topic_message) """

        queue.put("RECEIVER_READY")

        topicfilter = "10001"
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "10002")

        while not self.test_finished:
            string = self.socket.recv()
            t1 = time.time()
            topic, messagedata = string.decode('utf-8').split("&")

            if topic == "10001" :
                self.id+=1
                tmp= [self.id, messagedata,t1]
                self.plt_data.append(tmp)
            else:
                print("error")

        return(self.plt_data)

