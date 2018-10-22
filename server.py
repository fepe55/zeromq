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

    comando = 'ls -l'
    subprocess.run(comando.split(' '))

    time.sleep(1)

    #  Send reply back to client
    socket.send(b'Done')
