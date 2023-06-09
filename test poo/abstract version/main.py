import sys
import multiprocessing
from main_send import main_send
from main_receive import main_receive
from time import sleep

def main():
    
    
    if len(sys.argv) < 5:
        print("Pas assez d'arguments: python3 main.py [protocol] [message_count] [type de test] [port ou adresse broadcast(ivy)]")
        return

    protocol = sys.argv[1]
    message_count = int(sys.argv[2])
    test_type = sys.argv[3]
    port = sys.argv[4:] if protocol == 'ivy' else sys.argv[4]

    queue = multiprocessing.Queue()
    
    receive_process = multiprocessing.Process(target=main_receive, args=(protocol, message_count, test_type, port, queue))
    send_process = multiprocessing.Process(target=main_send, args=(protocol, message_count, test_type, port, queue))
    receive_process.start()
    #sleep(2)
    send_process.start()


    send_process.join()
    receive_process.join()

if __name__ == '__main__':
    main()
