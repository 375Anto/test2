# example 1 (UDP client socket )
import socket
import os.path

# создаем TCP сокет-клиент
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
# подключаемся к 8888 порту
sock.connect(os.path.curdir + "/tmp/sock_test.s")
# отпарлвяем сообщение
sock.send(bytes(input('to get multiplicate, enter numbers separated ","\n'), 'UTF-8'))
msg = sock.recv(1024)
print(msg.decode('UTF-8'))
# закрываем сокет-соединение
sock.close()
