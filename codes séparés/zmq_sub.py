import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print ("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)
    
# Subscribe to 10001
topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

total_value = 0
for update_nbr in range (5):
    string = socket.recv()
    print(string.decode('utf-8'))
    topic, messagedata = string.split()
    total_value += int(messagedata)
    print (topic.decode('utf-8'), messagedata.decode('utf-8'))

print ("Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr))
      