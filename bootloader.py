#!/usr/bin/python -u
#simplePingExample.py
from Ping import Ping1D
import sys
import getopt
import Message
from pymavlink import mavutil
import time
import serial
import socket

#TODO remove parsebyte
#TODO scan for available devices automatically
#TODO make a symlink or something so it will register in 'ENDPOINTS' via webui
#TODO add firmware update

master = mavutil.mavlink_connection('udpout:0.0.0.0:9000', source_system=66)


sockit = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockit.setblocking(False)
sockit.bind(('127.0.0.1', 6666))


time_boot_ms = 0
min_distance = 20
max_distance = 5000
type = 2
id = 1
orientation = 25
covarience = 0

device = ''
instructions = "Usage: python simplePingExample.py -d <device_name>"

##Parse Command line options
############################
try:
    options, remainder = getopt.getopt(sys.argv[1:],"hd:",["help", "device="])
except:
    print(instructions)
    exit(1)

for opt, arg in options:
    if opt in ('-h', '--help'):
        print(instructions)
        exit(1)
    elif opt in ('-d', '--device'):
        if (arg != ''):
            device = arg
    else:
        print(instructions)
        exit(1)

#Make a new Ping
myPing = Ping1D(device)
myPing.initialize()

myPing.sendMessage(Message.gen_goto_bootloader, [], 255)
exit(1)
