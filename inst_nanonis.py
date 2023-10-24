import socket

class Itc():
    def __init__(self):
        self.address = "127.0.0.1"
        self.port = 51754
        self.sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        # sock.bind((self.address,self.port))
        self.sock.connect( (self.address , self.port) )

    def handShake(self):
        self.sock.send("abcde")
        return self.sock.recv()

