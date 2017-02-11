import time
import os
import pip
import progressbar
import argparse

from builtins import print
from shutdown import *


parser = argparse.ArgumentParser(description='Shutdowner')
parser.add_argument('action', help='shutdown, restart, hibernate, logoff, cancel')
parser.add_argument('time', help='Time in seconds', type=int)
parser.add_argument("-f", "--force", help="Force application close", action='store_true')
parser.add_argument("-i", "--instant", help="Instant off", action='store_true')
args = parser.parse_args()


def print_delfyn():
    print(
        "                                         __ \n                                     _.-~  ) \n                          _..--~~~~,'   ,-/     _ \n                       .-'. . . .'   ,-','    ,' ) \n                     ,'. . . _   ,--~,-'__..-'  ,' \n                   ,'. . .  (@)' ---~~~~      ,' \n                  /. . . . '~~             ,-' \n                 /. . . . .             ,-' \n                ; . . . .  - .        ,' \n               : . . . .       _     / \n              . . . . .          `-.: \n             . . . ./  - .          ) \n            .  . . |  _____..---.._/ ____ ~ Delfyn ~ ... ... ... " + os.name + " \n      ~---~~~~----~~~~~~---~~~~----~~~ \n")


def windows_action(action, time, force=False, instant=False):
    if action == "shutdown":
        shutdown(time=time, force=force, warning_off=instant)

    elif action == "restart":
        restart(time=time, force=force)

    elif action == "hibernate":
        hibernate(force=force)

    elif action == "logoff":
        hibernate(force=force)

    else:
        print(" Shutdown - time, force, instant \n Restart - time, force, instant \n Hibernate - force \n Logoff - force \n")
        print(" Cancel progress bar - Ctrl - C \n")


def progress_bar(arg_time):
    bar = progressbar.ProgressBar()
    for i in bar(range(arg_time)):
        time.sleep(1)


def windows():
    windows_action(args.action, args.time, args.force, args.instant)
    progress_bar(args.time)


def windows():
    windows_action(args.action, args.time, args.force, args.instant)
    progress_bar(args.time)


def linux(action, time, force=False, instant=False):
    if action == "shutdown":
        os.system("shutdown -t " + str(time))

    elif action == "restart":
        if args.force:
            os.system("reboot -f")
        else:
            os.system("reboot")

    elif action == "hibernate":
        os.system("pm-hibernate")

    elif action == "logoff":
        os.system("logout")

    else:
        print(
            " Shutdown - time \n Restart - force \n Hibernate -  \n Logoff -  \n")
        print(" Cancel progress bar - Ctrl - C \n")


if __name__ == '__main__':
    print_delfyn()
    try:
        if os.name == 'nt':
            windows()
        elif os.name == 'posix':
            pass
        else:
            print('Mac OS / Unix not supported')
    except KeyboardInterrupt:
        cancel()
        print('  Action aborted -> User interruption')