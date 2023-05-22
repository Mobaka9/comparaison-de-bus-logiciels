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
socket.setsockopt(zmq.RCVHWM, 1000000)


print ("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 3:
    socket.connect ("tcp://localhost:%s" % port1)
    
#Subscribe to 10001
topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

plt_data = []
msg_id = 0
total_msgs = sys.argv[2]
total_msgs = int(total_msgs)
for i in range(total_msgs):
    #print(i)
    string = socket.recv()
    t1 = time.time()
    #print(string.decode('utf-8'))
    #topic, messagedata = string.split()
    topic, messagedata = string.decode('utf-8').split("&")

    #messagedata = messagedata.decode('utf-8')
    t0 = float(messagedata.split("=")[1])
    time_interval = t1-t0
    plt_data.append(time_interval)
print(len(plt_data))
print(total_msgs)

if len(plt_data) == total_msgs:

    # Dessiner le graphique
    plt.plot(range(1, total_msgs+1), plt_data, 'ro')
    plt.xlabel('Message number')
    plt.ylabel('Time (s)')
    plt.title('Time to receive each message')
    print("La moyenne est ", mean(plt_data))
    plt.title("temps moyens d'émission de "+str(total_msgs)+" messages courts avec ZeroMQ.")
    plt.show()
    plt.savefig("10 msgs courts.png")
    plt.close()
      