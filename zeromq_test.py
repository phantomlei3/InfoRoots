#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")

test_url = b"URL https://www.nytimes.com/2020/02/17/world/asia/coronavirus-westerdam-cambodia-hun-sen.html?action=click&module=Top%20Stories&pgtype=Homepage"

socket.send(test_url)
message = socket.recv()
print(message)