import zmq
from ivy.std_api import *
import sys
from abstract_protocol import AbstractProtocol
from zeromq import ZeroMQProtocol
from ivy_protocol import IvyProtocol
from kafka_protocol import KafkaProtocol
from message_receiver import MessageReceiver






def main():
    if len(sys.argv) < 5:
        print("Pas assez d'arguments: python3 main_receive.py [protocol] [message_count] [type de test] [port ou adresse broadcast(ivy)]")
        return

    protocol = sys.argv[1]
    message_count = int(sys.argv[2])
    test_type =sys.argv[3]
    
    com = "sub"
    if protocol == 'ivy':
        args = sys.argv[4:]
        print(args)
        protocol_obj = IvyProtocol(args)
        protocol_obj.initialize()
    elif protocol == 'zeromq':
        port = sys.argv[4]
        protocol_obj = ZeroMQProtocol(port, com)
        protocol_obj.initialize()
    elif protocol == 'kafka':
        protocol_obj = KafkaProtocol(com)
        protocol_obj.initialize()
    else:
        print("Unsupported protocol: "+str(protocol))
        return

    receiver = MessageReceiver(protocol_obj, protocol)
    receiver.receive_messages(message_count, test_type)
    
    '''sender = MessageSender(protocol_obj)
    sender.send_messages(message_count)'''


if __name__ == '__main__':
    main()
