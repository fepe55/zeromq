import zmq
import time
import subprocess

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://localhost:5555')

while True:
    message = socket.recv()
    action, ip = str(message).split(': ')
    # print('Received action {} from ip {}'.format(action, ip))

    # action = action.decode('utf-8')

    if action not in ['ban', 'unban']:
        socket.send(b'Wrong action')
    else:
        if action == 'ban':
            command = 'ls -l'
        if action == 'unban':
            command = 'ls -l'
        subprocess.run(command.split(' '))
        #  Send reply back to client
        socket.send(b'Done')
