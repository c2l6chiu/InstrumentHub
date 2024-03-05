# # Echo server program
# import socket

# HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
# PORT = 50007              # Arbitrary non-privileged port
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen(1)
#     conn, addr = s.accept()
#     print("accepted")
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data: break
#             conn.sendall(data)


from multiprocessing.connection import Listener,Client

address_AppServer = '127.0.0.1'
port_AppServer = 8192
authkey_AppServer = b'vf@pnml1234'

port_AppServer = Listener((address_AppServer,port_AppServer))
# port_AppServer._listener._socket.settimeout(1)

client = port_AppServer.accept()
print('get something')
# msg = client.recv_bytes()
# print(msg)
client.send_bytes(b'f123')