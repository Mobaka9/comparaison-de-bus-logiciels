import zmq
import getopt
import os
import string
from ivy.std_api import *
from time import sleep, time
import sys
from kafka import KafkaConsumer
import time


class MessageReceiver:
    
    def __init__(self, protocol):
        self.protocol = protocol
        self.kafka_producer = None

    @staticmethod
    def lprint(fmt, *arg):
            IVYAPPNAME = "pyhello"
            print(IVYAPPNAME + ': ' + fmt % arg)

    def initialize_ivy(self):
        IVYAPPNAME = 'pyhello'
        sivybus = ''
        sisreadymsg = '[%s is ready]' % IVYAPPNAME
        
        
            
        def usage(scmd):
            lpathitem = string.split(scmd, '/')
            fmt = '''Usage: %s [-h] [-b IVYBUS | --ivybus=IVYBUS]
            where
            \t-h provides the usage message;
            \t-b IVYBUS | --ivybus=IVYBUS allow to provide the IVYBUS string in the form
            \t adresse:port eg. 127.255.255.255:2010
            '''
            print(fmt % lpathitem[-1])
        
        def oncxproc(agent, connected):
            if connected == IvyApplicationDisconnected:
                self.lprint('Ivy application %r was disconnected', agent)
            else:
                self.lprint('Ivy application %r was connected', agent)
            self.lprint('currents Ivy application are [%s]', IvyGetApplicationList())


        def ondieproc(agent, _id):
            self.lprint('received the order to die from %r with id = %d', agent, _id)
        
        try:
            optlist, left_args = getopt.getopt(sys.argv[3:], 'hb:', ['ivybus='])
        except getopt.GetoptError:
            # print help information and exit:
            usage(sys.argv[0])
            sys.exit(2)
        for o, a in optlist:
            if o in ('-h', '--help'):
                usage(sys.argv[0])
                sys.exit()
            elif o in ('-b', '--ivybus'):
                sivybus = a
        if sivybus:
            sechoivybus = sivybus
        elif 'IVYBUS' in os.environ:
            sechoivybus = os.environ['IVYBUS']
        else:
            sechoivybus = 'ivydefault'
        self.lprint('Ivy will broadcast on %s ', sechoivybus)

            # initialising the bus
        IvyInit(IVYAPPNAME,     # application name for Ivy
                sisreadymsg,    # ready message
                0,              # main loop is local (ie. using IvyMainloop)
                oncxproc,       # handler called on connection/disconnection
                ondieproc)      # handler called when a <die> message is received
        IvyStart(sivybus)

    def initialize_zmq(self, port):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.setsockopt(zmq.SNDHWM, 2000000)
        print ("Collecting updates from weather server...")
        socket.connect ("tcp://localhost:%s" % port)
        return socket
    
    def initialize_kafka(self):
        consumer = KafkaConsumer(
            'hello',
            auto_offset_reset='latest',
            bootstrap_servers=['localhost:9092'],
            api_version=(0, 10),
            consumer_timeout_ms=10000
        )
        return consumer
   


    def receive_msg_ivy(self):
        def onmsgproc(agent, *larg):
            global start_time, end_time
            print("hi")
            self.lprint('Received from %r: [%s] ', agent, larg[0])

            if "start_time" in larg[0]:
                    start_time = float(larg[0].split("=")[1])
                    print(start_time)
            if "last message" in larg[0]:
                end_time = time.time()
                print("Temps total de communication : ", (end_time - start_time))

        IvyBindMsg(onmsgproc, '(.*)')
        
    def receive_msg_zmq(self, socket, message_count):
                      
            #Subscribe to 10001
            topicfilter = "10001"
            socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)


            for i in range(message_count):
                print(i)
                print("hi")
                string = socket.recv()
                
                print(string.decode('utf-8'))
                #topic, messagedata = string.split()
                topic, messagedata = string.decode('utf-8').split("&")

                #messagedata = messagedata.decode('utf-8')
                start_time = float(messagedata.split("=")[1])

                if "last message" in messagedata:
                    end_time = time.time()
                    print("Temps total de communication : ", (end_time - start_time))

    def receive_msg_kafka(self, message_count, consumer):
        
        for msg in consumer:
            
            
            
            print(msg.value)
            #print(i)
            
            if "last message" in msg.value.decode('utf-8'):
                end_time = time.time()
                start_time = float(msg.value.decode('utf-8').split("=")[1])
                print("Temps total de communication : ", (end_time - start_time))
            

        if consumer is not None:
            consumer.close()
        
    
        
    def receive_messages(self, port, message_count):
        if self.protocol == 'ivy':
            self.initialize_ivy()
            self.receive_msg_ivy()
        elif self.protocol == 'zeromq':
            socket = self.initialize_zmq(port)
            self.receive_msg_zmq(socket, message_count)
        elif self.protocol == 'kafka':
            consumer = self.initialize_kafka()
            self.receive_msg_kafka(message_count, consumer)    
            
            
def main():
    if len(sys.argv) < 4:
        print("pas assez d'arguments: python3 receive.py [protocol]  [message_count] [port ou adresse broadcast(ivy)]")
        return

    protocol = sys.argv[1]
    port = sys.argv[3]
    int(port)
    message_count = int(sys.argv[2])

    receiver = MessageReceiver(protocol)

    receiver.receive_messages(port, message_count)


if __name__ == '__main__':
    main()