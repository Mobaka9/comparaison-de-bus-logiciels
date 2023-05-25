import sys
import zmq
import time
import matplotlib.pyplot as plt
from statistics import mean

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 3:
    port1 =  sys.argv[3]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.RCVHWM, 2000000)


print ("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 3:
    socket.connect ("tcp://localhost:%s" % port1)
    
#Subscribe to 10001
topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

total_msgs = sys.argv[2]
total_msgs = int(total_msgs)
for i in range(total_msgs):
    print(i)
    string = socket.recv()
    
    #print(string.decode('utf-8'))
    #topic, messagedata = string.split()
    topic, messagedata = string.decode('utf-8').split("&")

    #messagedata = messagedata.decode('utf-8')
    start_time = float(messagedata.split("=")[1])

    if "last message" in messagedata:
        end_time = time.time()
        print("Temps total de communication : ", (end_time - start_time))

      