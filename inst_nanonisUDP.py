import socket

class Inst():
    def __init__(self):
        self.address = '127.0.0.1'
        self.port = 51795
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.s.bind( (self.address , self.port) )
        except Exception as eer:
            print("failed to connect")
            print(eer)
            raise

    def flush(self):
        self.s.settimeout(0.001)
        self.t0=0
        while True:
            try:
                # data , addr = self.s.recvfrom(65535)
                self.t0 = self.get_time()
            except:
                self.s.settimeout(0.1)
                return self.t0
#time(mS)
    def get_time(self):
        str = self.get_all()
        data = str.split(",")
        time = data[0]
        return float(time[2:])

#Current (A)    
    def get_current(self):
        str = self.get_all()
        data = str.split(",")
        return data[1]

#LockIn X (V)    
    def get_lockin_2x(self):
        str = self.get_all()
        data = str.split(",")
        return data[2]

#LockIn Y (m)    
    def get_lockin_y(self):
        str = self.get_all()
        data = str.split(",")
        return data[3]

#LockIn 2X (m)    
    def get_lockin_2x(self):
        str = self.get_all()
        data = str.split(",")
        return data[5]

#LockIn 2Y (m)    
    def get_lockin_2y(self):
        str = self.get_all()
        data = str.split(",")
        return data[6]
#X (m)    
    def get_x(self):
        str = self.get_all()
        data = str.split(",")
        return data[13]
    
#Y (m)    
    def get_y(self):
        str = self.get_all()
        data = str.split(",")
        return data[14]

#Z (m)    
    def get_z(self):
        str = self.get_all()
        data = str.split(",")
        return data[15]
        
#X LockIn (m)    
    def get_x_lockin(self):
        str = self.get_all()
        data = str.split(",")
        return data[21]

    def get_all(self):
        data , addr = self.s.recvfrom(256)
        return(str(data))