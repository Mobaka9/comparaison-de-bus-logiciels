import getopt
import os
import string
import sys
import time
from time import sleep
from statistics import mean

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from ivy.std_api import *

IVYAPPNAME = 'pyhello'


def lprint(fmt, *arg):
    print(IVYAPPNAME + ': ' + fmt % arg)


def usage(scmd):
    lpathitem = string.split(scmd, '/')
    fmt = '''Usage: %s [-h] [-b IVYBUS | --ivybus=IVYBUS]
    where
    \t-h provides the usage message;
    \t-b IVYBUS | --ivybus=IVYBUS allow to provide the IVYBUS string in the form
    \t adresse:port eg. 127.255.255.255:2010
    '''
    print(fmt % lpathitem[-1])


def oncxproc(agent, connected):
    if connected == IvyApplicationDisconnected:
        lprint('Ivy application %r was disconnected', agent)
    else:
        lprint('Ivy application %r was connected', agent)
    lprint('currents Ivy application are [%s]', IvyGetApplicationList())


def ondieproc(agent, _id):
    lprint('received the order to die from %r with id = %d', agent, _id)
    
#declaration des variables globales
msgid= 0
plt_data = []
#à changer en fonction du nombre de messages recus
total_msgs = 1000

def onmsgproc(agent, *larg):
    global plt_data, msgid, total_msgs, time_interval
    t1 = time.time()
    #lprint('Received from %r: [%s] ', agent, larg[0])
    
    
    if "hello world number" in larg[0]:
        msgid+=1
        t0 = float(larg[0].split("=")[1])
        time_interval = t1 - t0
        plt_data.append(time_interval)
        #print("condition")
        print(larg[0])
        print(len(plt_data))


        
    
    
    #print(total_msgs)
    #print(plt_data)
        
    #print(len(plt_data))
    '''
    if len(plt_data) == total_msgs:
        # Dessiner le graphique
        plt.plot(range(1, total_msgs+1), plt_data, 'ro')
        plt.xlabel('Message number')
        plt.ylabel('Time (s)')
        plt.title('Time to receive each message')
        plt.show()
        plt.savefig("High resoltion.png",dpi=300)
        plt.close()
'''
    
    
    

def onhello(agent, *larg):
    
    sreply = 'goodday %s to=%s from=%s ' % (larg[0], larg[1], IVYAPPNAME)
    lprint('on hello , replying to %r: [%s]', agent, sreply)
    IvySendMsg(sreply)


def ontick():
    lprint('%s send a tick', IVYAPPNAME)
    IvySendMsg('%s_tick' % IVYAPPNAME)


if __name__ == '__main__':
    # initializing ivybus and isreadymsg
    sivybus = ''
    sisreadymsg = '[%s is ready]' % IVYAPPNAME
    # getting option
    try:
        optlist, left_args = getopt.getopt(sys.argv[1:], 'hb:', ['ivybus='])
    except getopt.GetoptError:
        # print help information and exit:
        usage(sys.argv[0])
        sys.exit(2)
    for o, a in optlist:
        if o in ('-h', '--help'):
            usage(sys.argv[0])
            sys.exit()
        elif o in ('-b', '--ivybus'):
            sivybus = a
    if sivybus:
        sechoivybus = sivybus
    elif 'IVYBUS' in os.environ:
        sechoivybus = os.environ['IVYBUS']
    else:
        sechoivybus = 'ivydefault'
    lprint('Ivy will broadcast on %s ', sechoivybus)

    # initialising the bus
    IvyInit(IVYAPPNAME,     # application name for Ivy
            sisreadymsg,    # ready message
            0,              # main loop is local (ie. using IvyMainloop)
            oncxproc,       # handler called on connection/disconnection
            ondieproc)      # handler called when a <die> message is received

    # starting the bus
    # Note: env variable IVYBUS will be used if no parameter or empty string
    # is given ; this is performed by IvyStart (C)
    IvyStart(sivybus)
    # binding on dedicated message : starting with 'hello ...'
    #IvyBindMsg(onhello,'^hello=([^ ]*) from=([^ ]*)')
    # binding to every message
    IvyBindMsg(onmsgproc, '(.*)')
    while msgid < total_msgs:
        sleep(1)
    
    print(len(plt_data))
    if len(plt_data) == total_msgs:

        # Dessiner le graphique
        plt.plot(range(1, total_msgs+1), plt_data, 'ro')
        plt.xlabel('Message number')
        plt.ylabel('Time (s)')
        plt.title('Time to receive each message')
        print("La moyenne est ", mean(plt_data))
        plt.show()
        plt.savefig("10 msgs courts.png")
        plt.close()

    