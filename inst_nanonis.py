import socket

class Inst():
    def __init__(self):
        self.address = '127.0.0.1'
        self.port = 51758
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect( (self.address , self.port) )

    def __del__(self):
        self.s.close()

    def handShake(self):
        pass
        # self.send("test")
        # return self.s.recv(1024)

#Swithc on/off z controller or withdraw
    def z_zctrl(self,arg):
        if arg in ["on"]: self.send("z_zctrl,1")
        elif arg in ["off"]: self.send("z_zctrl,2")
        elif arg in ["withdraw"]: self.send("z_zctrl,0")
        else: return "error"
        return self.recv()
    
    def z_zctrl_q(self):
        self.send("z_zctrl_q")
        status = self.recv()
        return status

    def send(self,msg):
        n = len(msg)
        self.s.sendall(bytes("{:3}".format(n), encoding='utf8'))
        self.s.sendall(bytes("{}".format(msg), encoding='utf8'))

    def recv(self):
        return(self.s.recv(1024))