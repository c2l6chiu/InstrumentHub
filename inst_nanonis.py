import socket

class Inst():
    def __init__(self):
        self.address = '127.0.0.1'
        self.port = 51758
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect( (self.address , self.port) )
        except Exception as eer:
            print("failed to connect")
            print(eer)
            raise

    def __del__(self):
        self.s.close()

    def handShake(self):
        pass
        # self.send("test")
        # return self.s.recv(1024)

########################################
############  Z controller  ############
########################################
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

########################################
##########  Bias/Bias Spectrum #########
########################################
#set bias value (V)
    def bias_bias(self,msg):
        bias = float(msg)
        if bias > 6 or bias < -6: return "wrong height (>6 or <-6)"
        self.send("bias_bias,"+msg)
        status = self.recv()
        return status

#query bias value (V)
    def bias_bias_q(self):
        self.send("bias_bias_q")
        bias = self.recv()
        return bias

#bias pulse (abs V) (S) (Z-hold on/off 1,0)
    def bias_pulse(self,volt,duration,hold):
        volt_value,duration_value = ( float(volt) , float(duration) )
        if volt_value>6 or volt_value<-6: return "wrong pulse voltage"
        if duration_value>1: return "wrong pulse duration"
        self.send("bias_pulse,"+volt+","+duration+","+hold)
        status = self.recv()
        return status        


#switch on/off bias spectroscopy (off: stop on: start)
    def bias_spec_io(self,arg):
        if arg in ["on"]: self.send("bias_spec_io,1")
        elif arg in ["off"]: self.send("bias_spec_io,0")
        else: return "error"
        return self.recv()        

#query bias spectroscopy status (1:running, 0: stopped)
    def bias_spec_q(self):
        self.send("bias_spec_q")
        status = self.recv()
        return status

#set bias spectroscopy sweeping range (V)
    def bias_spec_sweep(self,fromV,toV):
        from_value , to_value = (float(fromV),float(toV))
        if from_value>2 or from_value<-2 or to_value<-2 or to_value>2: return "wrong sweep range" 
        self.send("bias_spec_sweep,"+fromV+","+toV)
        status = self.recv()
        return status

#query bias spectroscopy sweeping range (V)
    def bias_spec_sweep_q(self):
        self.send("bias_spec_sweep_q")
        message = self.recv()
        return message              

#set bias spectroscopy sweeping channel (ex: 0,1,2,3)
    def bias_spec_channel(self,channel):
        self.send("bias_spec_channel,"+channel)
        status = self.recv()
        return status

########################################
###############  Current  ##############
########################################


    def recv(self):
        return(self.s.recv(1024))

    def send(self,msg):
        n = len(msg)
        self.s.sendall(bytes("{:3}".format(n), encoding='utf8'))
        self.s.sendall(bytes("{}".format(msg), encoding='utf8'))    

