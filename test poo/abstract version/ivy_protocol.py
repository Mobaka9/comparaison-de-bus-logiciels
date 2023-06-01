import getopt
import os
import string
from ivy.std_api import *
from time import sleep, time
import sys
import time
from abstract_protocol import AbstractProtocol



class IvyProtocol(AbstractProtocol):
    
    def __init__(self,args):
        self.is_initialized = False
        self.args = args
        self.msg = None
        
    
    
        
    def initialize(self):
        if not self.is_initialized:
            IVYAPPNAME = 'pyhello'
            sivybus = ''
            sisreadymsg = '[%s is ready]' % IVYAPPNAME
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

                    
            
            try:
                optlist, left_args = getopt.getopt(self.args, 'hb:', ['ivybus='])
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
                sechoivybus = 'ivydefault'''
            
            lprint('Ivy will broadcast on %s ', sechoivybus)

                # initialising the bus
            IvyInit(IVYAPPNAME,     # application name for Ivy
                    sisreadymsg,    # ready message
                    0,              # main loop is local (ie. using IvyMainloop)
                    oncxproc,       # handler called on connection/disconnection
                    ondieproc)      # handler called when a <die> message is received
            IvyStart(sivybus)
            self.is_initialized = True
            IvyBindMsg(self.onmsgproc, '(.*)')

    def send_message(self, message):
    
            IvySendMsg(message)
    @staticmethod
    def lprint(fmt, *arg):
            IVYAPPNAME = 'pyhello'
            print(IVYAPPNAME + ': ' + fmt % arg)
    def onmsgproc(self,agent, *larg):
        #self.lprint('Received from %r: [%s] ', agent, larg[0])

        self.msg = larg[0]
            
            
    def receive_message(self):
        while(not self.msg):
            pass
        msg=self.msg
        self.msg = None
        return msg