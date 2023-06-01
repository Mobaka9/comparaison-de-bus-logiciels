import zmq
from abstract_protocol import AbstractProtocol



class ZeroMQProtocol(AbstractProtocol):
    def __init__(self, port, com):
        self.port = int(port)
        self.socket = None
        self.topic = "10001"
        self.com = com

    def initialize(self):
        context = zmq.Context()
        if self.com == "PUB":
            self.socket = context.socket(zmq.PUB)
            self.socket.setsockopt(zmq.SNDHWM, 2000000)
            self.socket.bind("tcp://*:%s" % self.port)
        else:
            self.socket = context.socket(zmq.SUB)
            self.socket.setsockopt(zmq.RCVHWM, 2000000)
            self.socket.connect("tcp://localhost:%s" % self.port)
        
        

    def send_message(self, message):
        topic_message = str(self.topic) + "&" + str(message)  # Ajouter le topic au message
        self.socket.send_string(topic_message)

    def receive_message(self):
        topicfilter = "10001"
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)


        string = self.socket.recv()
        
        #topic, messagedata = string.split()
        topic, messagedata = string.decode('utf-8').split("&")
        #print(messagedata)
        #messagedata = messagedata.decode('utf-8')
        return(messagedata)

