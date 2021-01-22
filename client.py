import socket

HOST = '127.0.0.1'
PORT = 8080

# 소켓 생성 (Address Family, socket type)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect : server에 접속하기 위한 함수 (ip, port)
clientSocket.connect((HOST, PORT))

print('접속 완료')

# encode : 문자열 -> byte로 변환
# 파이썬에서 생성된 객체이므로 적절한 인코딩을 통해야 함
# send : 소켓을 통한 메시지 전송

while True:
    sendMsg = input('>>> ')
    clientSocket.send(sendMsg.encode('utf-8'))

    if sendMsg == 'quit':
        break

    recvMsg = clientSocket.recv(1024)
    print('Received', repr(recvMsg.decode()))


print('클라이언트 종료')
clientSocket.close()