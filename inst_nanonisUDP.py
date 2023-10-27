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

    def get_channel(self,list):
        result=[]
        str = self.get_all()
        data = str.split(",")
        list = list.split(",")
        for c in list:
            if int(c)==0: data[int(c)] = data[int(c)][2:]
            if int(c)==22: data[int(c)] = data[int(c)][:-1]
            if int(c)==21: data[int(c)] = data[int(c)][:-4]
            result+=[float(data[int(c)])]
        return result

#time(mS)
    def get_time(self):
        str = self.get_all()
        data = str.split(",")
        pre = data[22]
        return float(pre[:-1])
    
#Current (A)    
    def get_current(self):
        str = self.get_all()
        data = str.split(",")
        pre = data[0]
        return float(pre[2:])

#LockIn X (V)    
    def get_lockin_2x(self):
        str = self.get_all()
        data = str.split(",")
        return data[1]

#LockIn Y (m)    
    def get_lockin_y(self):
        str = self.get_all()
        data = str.split(",")
        return data[2]

#LockIn 2X (m)    
    def get_lockin_2x(self):
        str = self.get_all()
        data = str.split(",")
        return data[4]

#LockIn 2Y (m)    
    def get_lockin_2y(self):
        str = self.get_all()
        data = str.split(",")
        return data[5]
#X (m)    
    def get_x(self):
        str = self.get_all()
        data = str.split(",")
        return data[12]
    
#Y (m)    
    def get_y(self):
        str = self.get_all()
        data = str.split(",")
        return data[13]

#Z (m)    
    def get_z(self):
        str = self.get_all()
        data = str.split(",")
        return data[14]
        
#X LockIn (m)    
    def get_x_lockin(self):
        str = self.get_all()
        data = str.split(",")
        return data[20]

    def get_all(self):
        data , addr = self.s.recvfrom(512)
        return(str(data))