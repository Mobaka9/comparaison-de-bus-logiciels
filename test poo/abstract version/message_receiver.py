from time import sleep, time
import time
import matplotlib.pyplot as plt
from statistics import mean


class MessageReceiver:
    def __init__(self, protocol_obj, bus):
        self.protocol_obj = protocol_obj
        self.bus = bus
        self.plt_data = []
    
    
    def draw_graph(self, protocole, message_count):
        
        plt.plot(range(1, message_count+1), self.plt_data, 'ro')
        plt.xlabel('Message number')
        plt.ylabel('Time (s)')
        plt.title("temps moyens d'émission de "+str(message_count)+" messages courts avec "+str(protocole)+".")
        print("La moyenne est", mean(self.plt_data))
        plt.savefig('graph.png')  # Enregistre le graphique dans un fichier
        plt.close()  # Ferme la figure pour libérer les ressources

        
    def receive_messages(self, message_count, test_type):
        
        sleep(2)
        
        
        if test_type == "total":
        
            '''if self.bus == "ivy":
                
                print("hi")
                msg = self.protocol_obj.receive_message()
                
                if msg is not None:
                        start_time = float(msg.split("=")[1])
                        if "last message" in msg:
                            end_time = time.time()
                            print("Temps total de communication : ", (end_time - start_time))
                
            else: '''   
            for i in range(message_count):
                msg = self.protocol_obj.receive_message()
                print(i)
                if msg is not None :
                    print(msg)
                    
                    if not "ready" in msg:
                        start_time = float(msg.split("=")[1])
                    if "last message" in msg:
                        end_time = time.time()
                        print("Temps total de communication : ", (end_time - start_time))
        elif test_type == "graph":
               
            for i in range(message_count):
                msg = self.protocol_obj.receive_message()
                t1 = time.time()
                if msg : 
                    print(msg)
                    t0 = float(msg.split("=")[1]) 
                    print(t0) 
                    time_interval = t1 - t0
                    self.plt_data.append(time_interval)
                    print(len(self.plt_data))
            if len(self.plt_data) == message_count:
                    self.draw_graph(self.bus, message_count)    
        else :
            print("mauvais type de test choisi. veuillez entrer soit graph soit total.")