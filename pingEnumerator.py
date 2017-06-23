#!/usr/bin/python -u
#simplePingExample.py
from Ping import Ping
import sys
import getopt
from Ping import Message
from pymavlink import mavutil
import time
import serial
import socket

#TODO remove parsebyte
#TODO scan for available devices automatically
#TODO make a symlink or something so it will register in 'ENDPOINTS' via webui
#TODO add firmware update

##### Scan for available devices

import subprocess

try:
    output = subprocess.check_output("ls /dev/serial/by-id", shell=True)
    
    for line in output.split('\n'):
        if len(line) > 0:
            # Skip devices that we have already labeled
            if "Ping1D-id-" in line:
                continue
            print "Looking for Ping at", "/dev/serial/by-id/" + line
            newPing = Ping.Ping1D("/dev/serial/by-id/" + line)
            if newPing.initialize() == True:
                try:
                    print "Found Ping1D (ID: %d) at /dev/serial/by-id/%s" % (newPing.device_id, line)
                    target_device = subprocess.check_output("readlink -f /dev/serial/by-id/" + line, shell=True)
                    # Strip newline from output
                    target_device = target_device.split('\n')[0]
                    print "Creating symbolic link to", target_device
                    output = subprocess.check_output("ln -fs " + target_device + " /dev/serial/by-id/Ping1D-id-" + str(newPing.device_id), shell=True)
                except subprocess.CalledProcessError as e:
                    print e
                    continue
                
except subprocess.CalledProcessError as e:
    print e
