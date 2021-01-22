from socket import *
import os
import sys

clientSock = socket(AF_INET, SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 8080

clientSock.connect((HOST, PORT))
print('연결성공')

fileName = input('전송할 파일 이름을 입력하시오. : ')
clientSock.send(fileName.encode('utf-8'))

data = clientSock.recv(1024)
data_transferred = 0

if not data:
    print('파일 %s 가 서버에 존재하지 않음' % fileName)
    sys.exit()

nowdir = os.getcwd()
print(nowdir)

with open(nowdir + "\\file-transmission\\" + fileName, "wb") as f:  # 현재 dir에 파일을 받음
    try:
        while data:
            f.write(data)  # 1024byte 씀
            data_transferred += len(data)
            data = clientSock.recv(1024)
    except Exception as ex:
        print(ex)

print('수신완료 %s, 전송량 %d' % (fileName, data_transferred))
