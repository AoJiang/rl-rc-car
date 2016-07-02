"""
Just used to test our server.
http://ilab.cs.byu.edu/python/socket/echoclient.html
"""

import socket
import numpy as np
import time

HOST = '192.168.2.9'
PORT = 8888
SIZE = 1024

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    readings = s.recv(SIZE)
    s.close()

    # Turn our weird stringed list into an actual list.
    readings = readings.decode('utf-8')
    readings = readings[1:-1]
    readings = readings.split(', ')
    readings = [float(i) for i in readings]
    print(np.array([readings]))

    time.sleep(0.5)
