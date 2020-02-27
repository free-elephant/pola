from socket import *
import threading
import time
import sys

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))


def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))

try:
    port = 8088

    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('192.168.0.56', port))

    print('접속 완료')

    sender = threading.Thread(target=send, args=(clientSock,))
    receiver = threading.Thread(target=receive, args=(clientSock,))

    sender.start()
    receiver.start()

    while True:
        time.sleep(1)
        pass
except KeyboardInterrupt:
    clientSock.close()
    sys.exit()
