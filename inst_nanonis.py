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

#switch on/off z controller or withdraw
    def zctrl_io(self,arg):
        if arg in ["on"]: self.send("zctrl_io,1")
        elif arg in ["off"]: self.send("zctrl_io,2")
        elif arg in ["withdraw"]: self.send("zctrl_io,0")
        else: return "error"
        return self.recv()

#query z controller status    
    def zctrl_io_q(self):
        self.send("zctrl_io_q")
        status = self.recv()
        return status
    
#set z position (nm)
    def zctrl_z_set(self,msg):
        height = float(msg)
        if height > 150 or height < -150: return "wrong height"
        self.send("zctrl_z_set,"+msg)
        status = self.recv()
        return status

#query z position (nm)
    def zctrl_z_q(self):
        self.send("zctrl_z_q")
        height = self.recv()
        return height

#set home absolute (nm)
    def zctrl_z_home_absolute(self,msg):
        height = float(msg)
        if height > 150 or height < -150: return "wrong height"
        self.send("zctrl_z_home_absolute,"+msg)
        status = self.recv()
        return status

#set home relative (nm)
    def zctrl_z_home_relative(self,msg):
        height = float(msg)
        if height > 150 or height < -150: return "wrong height"
        self.send("zctrl_z_home_relative,"+msg)
        status = self.recv()
        return status  

#set z home
    def zctrl_z_home(self):
        self.send("zctrl_z_home")
        status = self.recv()
        return status

#set z setpoint (nA)
    def zctrl_setpoint(self,msg):
        setpoint = float(msg)
        if setpoint < 0.001 or setpoint > 9.999: return "wrong setpoint"
        self.send("zctrl_setpoint,"+msg)
        status = self.recv()
        print(msg)
        return status

#query z setpoint (nA)
    def zctrl_setpoint_q(self):
        self.send("zctrl_setpoint_q")
        setpoint = self.recv()
        return setpoint       

#set z PI P(pm) I(mS)
    def zctrl_pi(self,p,i):
        p_value , i_value = (float(p),float(i))
        if p_value>100 or p_value<1 or i_value<0.1 or i_value>10: return "wrong P,I" 
        self.send("zctrl_pi,"+p+","+i)
        status = self.recv()
        return status

#query z PI P(pm) I(mS)
    def zctrl_pi_q(self):
        self.send("zctrl_pi_q")
        message = self.recv()
        return message    




    def recv(self):
        return(self.s.recv(1024))

    def send(self,msg):
        n = len(msg)
        self.s.sendall(bytes("{:3}".format(n), encoding='utf8'))
        self.s.sendall(bytes("{}".format(msg), encoding='utf8'))    

