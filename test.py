import socket

address = '127.0.0.1'
port = 51795
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( (address , port) )
data , addr = s.recvfrom(1024)
print(data)
# data , addr = s.recvfrom(65535)
# print(data)
# data , addr = s.recvfrom(65535)
# print(data)
# data , addr = s.recvfrom(65535)
# print(data)
# data , addr = s.recvfrom(65535)
# print(data)