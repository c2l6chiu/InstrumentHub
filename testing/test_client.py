# # Echo client program
# import socket

# HOST = '127.0.0.1'    # The remote host
# PORT = 51758            # The same port as used by the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# # while True:
# # s.send(b'abc')
# # data = s.recv(1024)
# # print('Received', data)
# # s.close()

from multiprocessing.connection import Client

address_AppServer = '127.0.0.1'
port_AppServer = 8192
authkey_AppServer = b'vf@pnml1234'

port_AppServer = Client((address_AppServer,port_AppServer) , 
                                  authkey= authkey_AppServer)

