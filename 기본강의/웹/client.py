import socket

# 네트워크 통신을 하기 위한 소켓 객체를 생성
# IPv4를 이용한 TCP 통신용 소켓
# 소켓 객체를 통해 서버와 통신
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('DEBUG:::소켓 생성 완료')

# 파일 입/출력시 open을 통해서 입/출력 하기위한 파일 객체를 얻어온 것 처럼
# 통신 입/출력을 하기 위해서 서버와의 객체를 생성
# 소켓 프로그래밍에서는 connect() 를 통해서 가능

serverAddress = socket.gethostbyname('info.cern.ch')
serverPort = 80

sock.connect((serverAddress, serverPort))
print('DEBUG:::connect 완료')

# 서버에 HTML 코드를 요청 => Request Header

request_header = 'GET /index.html HTTP/1.1\r\n'
request_header += 'Host: info.cern.ch\r\n'
request_header += '\r\n'

# 요청대로 처리가 되어서 HTML 코드가 잘 다운로드 되는지 확인

sock.send(request_header.encode())
response = sock.recv(1024)
print(response.decode())


sock.close()
