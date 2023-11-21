import socket

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓을 특정 주소와 포트에 바인딩
server_address = ('192.168.0.129', 1999)
server_socket.bind(server_address)

# 연결 대기
server_socket.listen(1)
print('서버가 연결을 기다리고 있습니다.')

# 클라이언트와의 연결 수락
client_socket, client_address = server_socket.accept()
print('클라이언트와 연결됨:', client_address)

# 데이터 수신 및 송신
data = client_socket.recv(1024)
print('수신한 데이터:', data.decode('utf-8'))

message = '1,E53STC33'
client_socket.sendall(message.encode('utf-8'))

# 연결 종료
client_socket.close()
server_socket.close()