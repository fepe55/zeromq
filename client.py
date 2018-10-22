"""
  path/to/env/bin/python path/to/env/src/banunban.py <ban|unban> <ip>
"""
import sys
import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

if __name__ == '__main__':
    action = sys.argv[1]
    ip = sys.argv[2]

    if action in ['ban', 'unban']:
        socket.send_string('{}: {}'.format(action, ip))
