import socket

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
server_address = ('192.168.0.129', 1999)
client_socket.connect(server_address)
print('서버에 연결됨:', server_address)

# 데이터 송신
message = '클라이언트에서 서버로 메시지 전송'
client_socket.sendall(message.encode('utf-8'))

# 데이터 수신
data = client_socket.recv(1024)
print('수신한 데이터:', data.decode('utf-8'))

# 연결 종료
client_socket.close()