#---------------------------------------------
from src.param import param_co
from src.misc import network
from src.misc import terminal

import socket
import threading
import platform
import signal
import time
import os
import getpass
import sys
import argparse
import psutil


# Manage Ctrl+C input
def handler(signum, frame):
    param_co.run_loop = False

signal.signal(signal.SIGINT, handler)

def system_clear():
    os.system('clear')

def update_nb_thread():
    param_co.state_co["self"]["nb_thread"] = threading.active_count()

def check_for_root():
    if not os.geteuid() == 0:
        sys.exit("\nOnly root can run this script\n")

def system_information(prog_name):
    check_for_root()

    #Info
    program = prog_name
    ip = network.get_ip_adress()
    hostname = socket.gethostname()
    arch = platform.architecture()[0]
    core = platform.uname()[2]
    proc = platform.processor()
    python = platform.python_version()
    mode = param_co.status_ui

    try:
        OS = platform.freedesktop_os_release()['PRETTY_NAME']
    except:
        OS = platform.system()

    #Header
    print('%-12s' '\033[1;34m%s\033[0m' % ("[Obstacle]", program))
    print("-----------------------")
    print('%-12s' '\033[1;34m%s\033[0m' % ("IP", ip))
    print('%-12s' '\033[1;34m%s\033[0m' % ("Hostname", hostname))
    print('%-12s' '\033[1;34m%s\033[0m, \033[1;34m%s\033[0m' % ("Arch", arch, proc))
    print('%-12s' '\033[1;34m%s\033[0m' % ("OS", OS))
    print('%-12s' '\033[1;34m%s\033[0m' % ("Core", core))
    print('%-12s' '\033[1;34m%s\033[0m' % ("Python", python))
    print("-----------------------")

def manage_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", action="store_true")
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--fullscreen", action="store_true")
    args = parser.parse_args()

    if(args.dev):
        param_co.status_ui = "dev"
    elif(args.demo):
        param_co.status_ui = "demo_minimized"
    elif(args.fullscreen):
        param_co.status_ui = "demo_fullscreen"
    else:
        param_co.status_ui = "dev"

def get_temps_core(number):
    temp = psutil.sensors_temperatures()
    if(temp):
        try:
            temperature = temp["coretemp"][number+1].current
        except:
            temperature = 0
        return temperature