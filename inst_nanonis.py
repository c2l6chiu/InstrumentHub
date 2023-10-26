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

    def echo(self,msg):
        return(msg)
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

#query current (nA)
    def current(self):
        self.send("current")
        message = self.recv()
        return message      

########################################
###############  Walker  ###############
########################################

#set walker voltage(V) freuqency(mS)
    def walker_setting(self,volt,freq):
        volt_value , i_freq = (float(volt),float(freq))
        if volt_value>390 or volt_value<10 or i_freq<10 or i_freq>400: return "wrong walker setting" 
        self.send("walker_setting,"+volt+","+freq)
        status = self.recv()
        return status

#query walker voltage(V) freuqency(mS)
    def walker_setting_q(self):
        self.send("walker_setting_q")
        status = self.recv()
        return status
    
#walk bipolar (will NOT hold until finish walking)
    def walker_walk(self,dir,step):
        dir = dir.lower()
        dir_dict = ["+x","x+","-x","x-","+y","y+","-y","y-","+z","z+","-z","z-"]
        step_value = int(step)
        if dir not in dir_dict: return "error direction"
        dir_ind = (dir_dict.index(dir))//2+1
        if abs(step_value)>1001: return "too many steps"
        self.send("walker_walk,"+str(dir_ind)+','+step)
        status = self.recv()
        return status   

#walk unipolar z (will NOT hold until finish walking)
    def walker_uni_walk(self,dir,step):
        dir = dir.lower()
        dir_dict = ["+x","x+","-x","x-","+y","y+","-y","y-","+z","z+","-z","z-"]
        step_value = int(step)
        if dir not in dir_dict: return "error direction"
        if dir not in dir_dict[8:12]: return "only allow uni- in z"
        dir_ind = (dir_dict.index(dir))//2+1
        if abs(step_value)>1001: return "too many steps"
        self.send("walker_uni_walk,"+str(dir_ind)+','+step)
        status = self.recv()
        return status

#walker stop immediately
    def walker_stop(self):
        self.send("walker_stop")
        status = self.recv()
        return status
       
########################################
###########  Move/Position  ############
########################################

#move to x,y (nm) (using scanning speed, set by move_speed)
#!!!Watch out the tip speed setting!!! 
#Suggest using move_speed to set speed up before using it
    def move_move(self,x,y):
        x_value , y_value = (float(x),float(y))
        if max(abs(x_value) , abs(y_value)) > 1000: return "wrong position" 
        self.send("move_move,"+x+","+y)
        status = self.recv()
        return status

#stop follow me now!
    def move_stop(self):
        self.send("move_stop")
        status = self.recv()
        return status       

#query current x,y (nm)
    def move_q(self):
        self.send("move_q")
        setpoint = self.recv()
        return setpoint
    
#set moving/scanning speed (nm/s)
    def move_speed(self,speed):
        speed_value = float(speed)
        if speed_value <=0.1 or speed_value > 5000: return "wrong speed"
        self.send("move_speed,"+speed)
        status = self.recv()
        return status          

#querry moving/scanning speed (nm/s)
    def move_speed_q(self):
        self.send("move_speed_q")
        setpoint = self.recv()
        return setpoint


























    def recv(self):
        return(self.s.recv(1024))

    def send(self,msg):
        n = len(msg)
        self.s.sendall(bytes("{:3}".format(n), encoding='utf8'))
        self.s.sendall(bytes("{}".format(msg), encoding='utf8'))    

