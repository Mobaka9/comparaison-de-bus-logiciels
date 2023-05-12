from ivy.std_api import *
import argparse
import sys
from time import sleep
def usage():
    usage = ('Usage: agent1 [options] regexps\n'
             'Options:\n'
             '\t-b, --ivybus=bus    defines the Ivy bus to join; defaults to 127:2010\n')
    print(usage)


def on_connection_change(agent, event):
    if event == IvyApplicationDisconnected:
        print('Ivy application ', agent, ' has disconnected')
    else:
        print('Ivy application ', agent, ' has connected')
    print('Ivy applications currently on the bus: ',
          ','.join(IvyGetApplicationList()))

def on_die_proc(agent, _id):
    print('received the order to die from', agent,' with id = ', _id)
    sys.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--ivybus",  nargs='?', default="127:2010", help="defines the Ivy bus to join; defaults to 127:2010")
    args = parser.parse_args()
    ivybus = args.ivybus

    # initialising the bus
    readymsg = '[agent1 is ready]'
    IvyInit("Agent1",  # application name for Ivy
            readymsg,  # ready message
            0,  # parameter ignored
            on_connection_change,  # handler called on connection/disconnection
            on_die_proc)  # handler called when a die msg is received

    # starting the bus
    IvyStart(ivybus)
    print("Agent1 started on bus :", ivybus)
    sleep(2)

    IvySendMsg("TOTO TEST=oui")
    #IvySendMsg("TaxibotAllocation AEON_FM Taxibot=101 Time=09:00:01 Nb=15 Slice=driving 1 AFR072 2500 2600 F05 SE1 driving 2 AFR072 2500 2600 F05 SE1 driving 3 AFR072 2500 2600 F05 SE1 driving 4 AFR072 2500 2600 F05 SE1 driving 5 AFR072 2500 2600 F05 SE1 driving 6 AFR072 2500 2600 F05 SE1 driving 7 AFR072 2500 2600 F05 SE1 driving 8 AFR072 2500 2600 F05 SE1 driving 9 AFR072 2500 2600 F05 SE1 driving 10 AFR072 2500 2600 F05 SE1 driving 11 AFR072 2500 2600 F05 SE1 driving 12 AFR072 2500 2600 F05 SE1 driving 5 AFR072 2500 2600 F05 SE1 driving 5 AFR072 2500 2600 F05 SE1")
    #IvySendMsg("TaxibotAllocation AEON_FM Taxibot=101 Time=09:00:01 Nb=15 Slice=driving 1 AFR072 2500 2600 F05 SE1 driving 2 AFR072 2500 2600 F05 SE1 driving 3 AFR072 2500 2600 F05 SE1 driving 4 AFR072 2500 2600 F05 SE1 driving 5 AFR072 2500 2600 F05 SE1")
    #IvySendMsg("TaxibotAllocation AEON_FM Taxibot=101 Time=09:00:01 Nb=15 EndSlice")
