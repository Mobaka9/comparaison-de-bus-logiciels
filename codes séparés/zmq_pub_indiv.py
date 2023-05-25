import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.SNDHWM, 1000000)
socket.bind("tcp://*:%s" % port)


#nombre de messages en 2eme parametre
total_msgs = sys.argv[2]
time.sleep(2)
for i in range(int(total_msgs)+1):
    #print(i)
    topic = 10001
    start_time = time.time()
    messagedata = "hello ="+str(start_time)
    #print (topic, messagedata)
    socket.send_string(str(topic) + "&" + str(messagedata))
    
