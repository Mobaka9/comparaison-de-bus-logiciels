import getopt
import os
import string
import sys
from time import sleep
import time
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


def onmsgproc(agent, *larg):
    lprint('Received from %r: [%s] ', agent, larg[0])


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
    start_time = time.time()
    print(start_time)
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
    

    # envoie un message à toutes les applications connectées
    sleep(2)
    for i in range(1000000):
        #print(i)
        t0 = time.time()
        IvySendMsg("hello world number Lorem ipsum dolor sit amet. Aut laboriosam praesentium hic voluptatem praesentium sit architecto unde. Qui officia adipisci sit obcaecati debitis et adipisci adipisci et iste nisi aut consequuntur dolores qui labore dolorem. Eum dolorem natus ea suscipit tempore At molestiae magnam qui alias dignissimos aut similique impedit. Id sunt dolores aut quis nemo sed voluptas asperiores qui voluptate quidem non galisum sint ut corrupti architecto. In accusantium exercitationem aut saepe dolores sed incidunt rerum aut aspernatur architecto ut dolor facere et voluptas doloremque. Id exercitationem saepe ut unde commodi aut magnam commodi? Ea quae accusantium et labore quia ab voluptates ratione qui suscipit deleniti est temporibus perferendis. Ea dolores dolore est saepe dolores ad architecto consequatur eum reprehenderit obcaecati ab voluptatem galisum. Nam perspiciatis placeat sed autem sunt qui rerum voluptatem in nisi iure. Aut nisi illum nam perspiciatis odit quo beatae vero ut sunt vitae id velit fugiat id aliquid repellat. Est sunt reprehenderit et odio quia rem laudantium mollitia sed velit tempore.Lorem ipsum dolor sit amet. Aut laboriosam praesentium hic voluptatem praesentium sit architecto unde. Qui officia adipisci sit obcaecati debitis et adipisci adipisci et iste nisi aut consequuntur dolores qui labore dolorem. Eum dolorem natus ea suscipit tempore At molestiae magnam qui alias dignissimos aut similique impedit. Id sunt dolores aut quis nemo sed voluptas asperiores qui voluptate quidem non galisum sint ut corrupti architecto. In accusantium exercitationem aut saepe dolores sed incidunt rerum aut aspernatur architecto ut dolor facere et voluptas doloremque. Id exercitationem saepe ut unde commodi aut magnam commodi? Ea quae accusantium et labore quia ab voluptates ratione qui suscipit deleniti est temporibus perferendis. Ea dolores dolore est saepe dolores ad architecto consequatur eum reprehenderit obcaecati ab voluptatem galisum. Nam perspiciatis placeat sed autem sunt qui rerum voluptatem in nisi iure. Aut nisi illum nam perspiciatis odit quo beatae vero ut sunt vitae id velit fugiat id aliquid repellat. Est sunt reprehenderit et odio quia rem laudantium mollitia sed velit tempore.Lorem ipsum dolor sit amet. Aut laboriosam praesentium hic voluptatem praesentium sit architecto unde. Qui officia adipisci sit obcaecati debitis et adipisci adipisci et iste nisi aut consequuntur dolores qui labore dolorem. Eum dolorem natus ea suscipit tempore At molestiae magnam qui alias dignissimos aut similique impedit. Id sunt dolores aut quis nemo sed voluptas asperiores qui voluptate quidem non galisum sint ut corrupti architecto. In accusantium exercitationem aut saepe dolores sed incidunt rerum aut aspernatur architecto ut dolor facere et voluptas doloremque. Id exercitationem saepe ut unde commodi aut magnam commodi? Ea quae accusantium et labore quia ab voluptates ratione qui suscipit deleniti est temporibus perferendis. Ea dolores dolore est saepe dolores ad architecto consequatur eum reprehenderit obcaecati ab voluptatem galisum. Nam perspiciatis placeat sed autem sunt qui rerum voluptatem in nisi iure. Aut nisi illum nam perspiciatis odit quo beatae vero ut sunt vitae id velit fugiat id aliquid repellat. Est sunt reprehenderit et odio quia rem laudantium mollitia sed velit tempore.Lorem ipsum dolor sit amet. Aut laboriosam praesentium hic voluptatem praesentium sit architecto unde. Qui officia adipisci sit obcaecati debitis et adipisci adipisci et iste nisi aut consequuntur dolores qui labore dolorem. Eum dolorem natus ea suscipit tempore At molestiae magnam qui alias dignissimos aut similique impedit. Id sunt dolores aut quis nemo sed voluptas asperiores qui voluptate quidem non galisum sint ut corrupti architecto. In accusantium exercitationem aut saepe dolores sed incidunt rerum aut aspernatur architecto ut dolor facere et voluptas doloremque. Id exercitationem saepe ut unde commodi aut magnam commodi? Ea quae accusantium et labore quia ab voluptates ratione qui suscipit deleniti est temporibus perferendis. Ea dolores dolore est saepe dolores ad architecto consequatur eum reprehenderit obcaecati ab voluptatem galisum. Nam perspiciatis placeat sed autem sunt qui rerum voluptatem in nisi iure. Aut nisi illum nam perspiciatis odit quo beatae vero ut sunt vitae id velit fugiat id aliquid repellat. Est sunt reprehenderit et odio quia rem laudantium mollitia sed velit tempore.Lorem ipsum dolor sit amet. Aut laboriosam praesentium hic voluptatem praesentium sit architecto unde. Qui officia adipisci sit obcaecati debitis et adipisci adipisci et iste nisi aut consequuntur dolores qui labore dolorem. Eum dolorem natus ea suscipit tempore At molestiae magnam qui alias dignissimos aut similique impedit. Id sunt dolores aut quis nemo sed voluptas asperiores qui voluptate quidem non galisum sint ut corrupti architecto. In accusantium exercitationem aut saepe dolores sed incidunt rerum aut aspernatur architecto ut dolor facere et voluptas doloremque. Id exercitationem saepe ut unde commodi aut magnam commodi? Ea quae accusantium et labore quia ab voluptates ratione qui suscipit deleniti est temporibus perferendis. Ea dolores dolore est saepe dolores ad architecto consequatur eum reprehenderit obcaecati ab voluptatem galisum. Nam perspiciatis placeat sed autem sunt qui rerum voluptatem in nisi iure. Aut nisi illum nam perspiciatis odit quo beatae vero ut sunt vitae id velit fugiat id aliquid repellat. Est sunt reprehenderit et odio quia rem laudantium mollitia sed velit tempore. =" + str(t0))
        
    

   # IvyMainLoop()
