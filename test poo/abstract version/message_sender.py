from time import sleep, time
import time


class MessageSender:
    def __init__(self, protocol):
        self.protocol = protocol

    def send_messages(self, message_count, type):
        
        sleep(2)
        
        if type == "total":
            start_time = time.time() 
            for i in range(message_count-1):
                print(i)
                
                message = "hello =" + str(start_time)
                self.protocol.send_message(message)
            message = "last message =" + str(start_time)
            self.protocol.send_message(message)
        elif type == "graph":
            for i in range(message_count):
                print(i)
                start_time = time.time()
                message = "hello =" + str(start_time)
                self.protocol.send_message(message)
        else :
            print("mauvais type de test choisi. veuillez entrer soit graph soit total.")