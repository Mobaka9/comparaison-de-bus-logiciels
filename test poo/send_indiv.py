import zmq
import getopt
import os
import string
from ivy.std_api import *
from time import sleep, time
import sys
from kafka import KafkaProducer
import time



class MessageSender:
    def __init__(self, protocol):
        self.protocol = protocol
        self.kafka_producer = None
        
    

    def initialize_ivy(self):
        IVYAPPNAME = 'pyhello'
        sivybus = ''
        sisreadymsg = '[%s is ready]' % IVYAPPNAME
        
        def lprint(fmt, *arg):
            print(IVYAPPNAME + ': ' + fmt % arg)
            
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
                lprint('Ivy application %r was disconnected', agent)
            else:
                lprint('Ivy application %r was connected', agent)
            lprint('currents Ivy application are [%s]', IvyGetApplicationList())


        def ondieproc(agent, _id):
            lprint('received the order to die from %r with id = %d', agent, _id)

                
          
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
        lprint('Ivy will broadcast on %s ', sechoivybus)

            # initialising the bus
        IvyInit(IVYAPPNAME,     # application name for Ivy
                sisreadymsg,    # ready message
                0,              # main loop is local (ie. using IvyMainloop)
                oncxproc,       # handler called on connection/disconnection
                ondieproc)      # handler called when a <die> message is received
        IvyStart(sivybus)


    def initialize_zmq(self, port):
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.setsockopt(zmq.SNDHWM, 2000000)
        socket.bind("tcp://*:%s" % port)
        return socket
    
    def initialize_kafka(self):
        self.kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))


    def send_messages_ivy(self, message_count):
        sleep(2)

        for i in range(1000):
            print(i)
            t0 = time.time()
            IvySendMsg("hello world number =" + str(t0))
            

    def send_messages_zmq(self, socket, message_count):
        

        sleep(2)
        for i in range(int(message_count)+1):
            #print(i)
            topic = 10001
            start_time = time.time()
            messagedata = "hello ="+str(start_time)
            #print (topic, messagedata)
            socket.send_string(str(topic) + "&" + str(messagedata))
            
    def publish_message_kafka(self, topic_name, msg):
        try:
            string_bytes = str.encode(msg)
            self.kafka_producer.send(topic_name, value=string_bytes)
            self.kafka_producer.flush()
        except Exception as ex:
            print(str(ex))

    def send_messages_kafka(self, message_count):
        for i in range(message_count):
            start_time = time.time()
            msg = "hello ="+str(start_time)
            self.publish_message_kafka(
                topic_name='hello',
                msg=str(i)+msg
                
            )

    def send_messages(self, port, message_count):
        if self.protocol == 'ivy':
            self.initialize_ivy()
            self.send_messages_ivy(message_count)
        elif self.protocol == 'zeromq':
            socket = self.initialize_zmq(port)
            self.send_messages_zmq(socket, message_count)
        elif self.protocol == 'kafka':
            self.initialize_kafka()
            self.send_messages_kafka(message_count)
        else:
            print("Invalid protocol specified")

    

def main():
    if len(sys.argv) < 4:
        print("pas assez d'arguments: python3 send.py [protocol]  [message_count] [port ou adresse broadcast(ivy)]")
        return

    protocol = sys.argv[1]
    port = sys.argv[3]

    message_count = int(sys.argv[2])

    sender = MessageSender(protocol)
    sender.send_messages(port, message_count)


if __name__ == '__main__':
    main()
