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
        x, y, z = sock.recv(1024).decode('utf-8').split()
        print('상대방 :', x, type(x))

try:
    port = 8088

    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSock.bind(('', port))
    serverSock.listen(1)

    print('%d번 포트로 접속 대기중...'%port)

    connectionSock, addr = serverSock.accept()

    print(str(addr), '에서 접속되었습니다.')

    sender = threading.Thread(target=send, args=(connectionSock,))
    receiver = threading.Thread(target=receive, args=(connectionSock,))

    sender.start()
    receiver.start()

    while True:
        time.sleep(1)
        pass
except KeyboardInterrupt:
    serverSock.close()
    sys.exit()
