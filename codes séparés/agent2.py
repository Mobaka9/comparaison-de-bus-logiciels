from ivy.std_api import *
import argparse
import sys

def usage():
    usage = ('Usage: agent2 [options] regexps\n'
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

def on_msg(agent, *arg):
    print('Received from', agent, arg and str(arg) or '<no args>')


def on_engine_msg(agent, test):
    print('Received from', agent, ": Test,", test)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--ivybus", nargs='?', default="127:2010",
                        help="defines the Ivy bus to join; defaults to 127:2010")
    args = parser.parse_args()
    ivybus = args.ivybus

    # initialising the bus
    readymsg = '[agent2 is ready]'
    IvyInit("Agent2",  # application name for Ivy
            readymsg,  # ready message
            0,  # parameter ignored
            on_connection_change,  # handler called on connection/disconnection
            on_die_proc)  # handler called when a die msg is received

    # starting the bus
    IvyStart(ivybus)
    print("Agent2 started on bus :", ivybus)

    # Bindings to some messages
    IvyBindMsg(on_engine_msg, "^TOTO TEST=(\\S*)")

    while True:
        print("Input a regexp to bind:")
        try:
            regexp = input('')
        except (EOFError, KeyboardInterrupt):
            IvyStop()
            break

        IvyBindMsg(on_msg, regexp)
