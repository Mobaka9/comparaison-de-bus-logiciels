import random
import string
from time import sleep, time
import time


class MessageSender:
    def __init__(self, protocol):
        self.protocol = protocol
        self.topic = "10001"

    def send_messages(self, message_count, type):
        
        
        if type == "total":
            length_of_string = 300000
            message_rand = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))+"="

            start_time = time.time() 
            for i in range(message_count):
                #print(i)

                #sleep(0.0001)
                message = str(message_rand) + str(start_time)
                #message = "hello =" + str(start_time)
                self.protocol.send_message(message, self.topic)
            message = "last message =" + str(start_time)
            self.protocol.send_message(message, "10002")
        elif type == "graph":
            for i in range(message_count):
                #print(i)
                length_of_string = 1100

                message_rand = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))+"="
                start_time = time.time()
                message = str(message_rand) + str(start_time)
                #message = "hello =" + str(start_time)
                self.protocol.send_message(message, self.topic)
            message = "last message =" + str(start_time)
            self.protocol.send_message(message, "10002")
        else :
            print("mauvais type de test choisi. veuillez entrer soit graph soit total.")