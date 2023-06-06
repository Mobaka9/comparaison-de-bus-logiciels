from time import sleep, time
import time


class MessageSender:
    def __init__(self, protocol):
        self.protocol = protocol
        self.topic = "10001"

    def send_messages(self, message_count, type):
        
        
        if type == "total":
            start_time = time.time() 
            sleep(10)
            for i in range(message_count):
                #print(i)
                
                message = "hello =" + str(start_time)
                self.protocol.send_message(message, self.topic)
            message = "last message =" + str(start_time)
            self.protocol.send_message(message, "10002")
        elif type == "graph":
            for i in range(message_count):
                #print(i)
                start_time = time.time()
                message = "hello =" + str(start_time)
                self.protocol.send_message(message, self.topic)
            message = "last message =" + str(start_time)
            self.protocol.send_message(message, "10002")
        else :
            print("mauvais type de test choisi. veuillez entrer soit graph soit total.")