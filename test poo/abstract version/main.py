
from abc import ABC, abstractmethod
from ivy.std_api import *
import sys
import getopt
from ivy_protocol import IvyProtocol
from zeromq import ZeroMQProtocol
from kafka_protocol import KafkaProtocol
from message_sender import MessageSender





def main():
    if len(sys.argv) < 4:
        print("Pas assez d'arguments: python3 main.py [protocol] [message_count] [type de test] [port ou adresse broadcast(ivy)]")
        return

    protocol = sys.argv[1]
    message_count = int(sys.argv[2])
    type_test = sys.argv[3]

    com = "PUB"
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
        print("Protocole invalide spécifié")
        return



    sender = MessageSender(protocol_obj)
    sender.send_messages(message_count, type_test)


if __name__ == '__main__':
    main()