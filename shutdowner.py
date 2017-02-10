import time
import os
import pip
import progressbar
import argparse

from builtins import print
from shutdown import *


parser = argparse.ArgumentParser(description='Shutdowner')
# parser.add_argument("-d", "--dependencies", help="Install dependencies", action='store_true')
parser.add_argument('action', help='shutdown, restart, hibernate, logoff, cancel')
parser.add_argument('time', help='Time in seconds', type=int)
parser.add_argument("-f", "--force", help="Force application close", action='store_true')
parser.add_argument("-w", "--warning", help="Instant off", action='store_true')
args = parser.parse_args()


def print_delfyn():
    print(
        "                                         __ \n                                     _.-~  ) \n                          _..--~~~~,'   ,-/     _ \n                       .-'. . . .'   ,-','    ,' ) \n                     ,'. . . _   ,--~,-'__..-'  ,' \n                   ,'. . .  (@)' ---~~~~      ,' \n                  /. . . . '~~             ,-' \n                 /. . . . .             ,-' \n                ; . . . .  - .        ,' \n               : . . . .       _     / \n              . . . . .          `-.: \n             . . . ./  - .          ) \n            .  . . |  _____..---.._/ ____ ~ Delfyn ~ ... ... ... " + os.name + " \n      ~---~~~~----~~~~~~---~~~~----~~~ \n")
# def dependencies():
#     print("Look's you don't have installed dependencies :( \n")
#     print("Installing shutdown : \n")
#     pip.main(["install", "shutdown"])
#     print("Installing proggressbar2 : \n")
#     pip.main(["install", "progressbar2"])


def select_action(action, time, force=False, instant=False):
    if action == "shutdown":
        shutdown(time=time, force=force, warning_off=instant)

    elif action == "restart":
        restart(time=time, force=force)

    elif action == "hibernate":
        hibernate(force=force)

    elif action == "logoff":
        hibernate(force=force)

    elif action == "cancel":
        cancel()
    else:
        print(" Shutdown - time, force, instant \n Restart - time, force, instant \n Hibernate - force \n Logoff - force \n")
        print(" Cancel progress bar - Ctrl - C \n")


def progress_bar(arg_time):
    bar = progressbar.ProgressBar()
    for i in bar(range(arg_time)):
        time.sleep(1)


def windows():
    select_action(args.action, args.time, args.force, args.warning)
    progress_bar(args.time)


if __name__ == '__main__':
    print_delfyn()
    try:
        if os.name == 'nt':
            windows()
    except KeyboardInterrupt:
        cancel()
        print('  Action aborted -> User interruption')