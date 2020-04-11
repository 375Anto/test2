import socket
import os, os.path
import time

path = os.path.curdir + "/tmp/sock_test.s"


def create_file():
    if os.path.exists(path):
        os.remove(path)


if __name__ == '__main__':
    print('we are located in --->' + os.path.abspath(os.path.curdir))
    create_file()
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as new_server:
        # new_server.bind(('127.0.0.1', 8888))
        new_server.bind(path)
        new_server.listen(5)
        while True:
            try:
                client, addr = new_server.accept()
            except KeyboardInterrupt:
                new_server.close()
                break
            else:
                result = client.recv(1024)
                print('Received from {addr} a message {result} in {time}'.format(addr=client, result=result.decode('UTF-8'), time=time.time()))
                try:
                    response = 1
                    for a in result.decode('UTF-8').split(","): response = response*int(a)
                except ValueError:
                    response = 'Mistake'
                client.send(bytes('Answer is ' + str(response), 'UTF-8'))
                client.close()
                print('Message', result.decode('utf-8'))
