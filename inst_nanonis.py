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
############  read_channel  ############
########################################
#read channel: 0: current,.... 22: labview time
    def read_channel(self,list):
        self.send("read_channel")
        result=[]
        msg = str(self.recv())
        data = msg.split(",")
        list = list.split(",")
        for c in list:
            if int(c)==0: data[int(c)] = data[int(c)][2:]
            if int(c)==22: data[int(c)] = data[int(c)][:-1]
            if int(c)==21: data[int(c)] = data[int(c)][:-4]
            result+=[float(data[int(c)])]
        return result

########################################
############  Z controller  ############
########################################
#switch on/off z controller or withdraw (on:1 off: 0)
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

########################################
################  Scan  ################
########################################

#start scan (action 0:stop 1: start 2: pause 3: resume) (direction 0:up scan 1:down scan)
    def scan_io(self,action,direction):
        if action in ["start","1"]: action = "1"
        elif action == ["stop","0"]: action = "0"
        elif action == ["pause","2"]: action = "2"
        elif action == ["resume","3"]: action = "3"
        else: return "error action"
        if direction in ["up","0"]: direction = "0"
        elif direction == ["down","1"]: direction = "1"
        else: return "error directoin"     
        self.send("scan_io,"+action+","+direction)
        return self.recv()

#query scan status 0: False 1: True
    def scan_io_q(self):
        self.send("scan_io_q")
        status = self.recv()
        return status

#receive last scanned data (channel: only one) (direction: 1: forward 2: backward) (always down scan:up to down)
    def scan_get(self,channel,direction):
        if not channel in [str(i) for i in range(24)]: return "error channel"
        if direction in ["1","forward"]: direction="1"
        elif direction in ["2","forward"]: direction="2"
        else: return "error direction"
        self.send("scan_get,"+channel+","+direction)
        return self.recv()


#set scan method (conti 1:on 0:off) (bouncy 1:on 0:off) (autoSave 1:on 0: off 2: next)
    def scan_method(self,conti,bouncy,autoSave,name):
        if conti in ["on","1"]: action = "1"
        elif conti == ["off","0"]: action = "0"
        else: return "wrong conti setting"
        if bouncy in ["on","1"]: action = "1"
        elif bouncy == ["off","0"]: action = "0"
        else: "wrong bouncy setting"
        if autoSave in ["on","1"]: action = "1"
        elif autoSave == ["off","0"]: action = "0"
        elif autoSave == ["next","2"]: action = "2"
        else: "wrong autoSave setting"
        self.send("scan_method,"+conti+","+bouncy+","+autoSave+","+name)
        return self.recv()

#query scan method (conti 1:on 0:off) (bouncy 1:on 0:off) file_name
    def scan_method_q(self):
        self.send("zctrl_io_q")
        status = self.recv()
        return status

#set scan resolution (#) (#) (channel: 0,1,14 I,dIdV,Z)
    def scan_res(self,pixel,lines,channel):
        self.send("scan_res,"+pixel+","+lines+","+channel)
        return self.recv()

#query scan resolution (pixel,lines,channel,channel,...,channel)
    def scan_res_q(self):
        self.send("scan_res_q")
        status = self.recv()
        return status

#set scan position x(nm),y(nm),sizeX(nm),sizeY(nm), angle(deg)
    def scan_pos(self,x,y,sizeX,sizeY,ang):
        self.send("scan_pos,"+x+","+y+","+sizeX+","+sizeY+","+ang)
        return self.recv()

#query scan position x(nm),y(nm),sizeX(nm),sizeY(nm), angle(deg)
    def scan_pos_q(self):
        self.send("scan_pos_q")
        status = self.recv()
        return status

#set scan speed speed (forward: nm/s backward: nm/s)
    def scan_speed_q(self,forward,backward):
        self.send("scan_pos,"+forward+","+backward)
        return self.recv()

#query scan speed
    def scan_speed(self):
        self.send("scan_pos_q")
        status = self.recv()
        return status


########################################
#############  Grid/Line  ##############
########################################

#switch on/off/pause grid 0: stop 1: start 2: pause 3: resume
    def grid_io(self,arg):
        if arg in ["stop",'0']: self.send("grid_io,0")
        elif arg in ["start",'1']: self.send("grid_io,1")
        elif arg in ["pause","2"]: self.send("grid_io,2")
        elif arg in ["resume","3"]: self.send("grid_io,3")
        else: return "error"
        return self.recv()

#query grid/line status
    def grid_io_q(self):
        self.send("grid_io_q")
        status = self.recv()
        return status

#set grid setting (nm)
    def grid_setting(self,centerX,centerY,width,height,angle,pointX,pointY):
        self.send("grid_setting,"+centerX+","+centerY+","+width+","+height+","+angle+","+pointX+","+pointY)
        return self.recv()

#query grid setting (no implementation in labview)
    def grid_setting_q(self):
        self.send("grid_setting_q")
        status = self.recv()
        return status        

#set line setting (nm)
    def line_setting(self,startX,startY,endX,endY,point):
        self.send("grid_setting,"+startX+","+startY+","+endX+","+endY+","+point)
        return self.recv()

#query line setting (no implementation in labview)
    def line_setting_q(self):
        self.send("line_setting_q")
        status = self.recv()
        return status    

########################################
###############  Lockin  ###############
########################################

#turn on/off the lock in 1:on 0: off
    def lockin_io(self,arg):
        if arg in ["on"]: self.send("lockin_io,1")
        elif arg in ["off"]: self.send("lockin_io,0")
        else: return "error"
        return self.recv()

#set the setting: amplitude (V), frequency(Hz), phase(deg)
    def lockin_setting(self,amp,frq,phs):
        amp_value , frq_value , phs_value = (float(amp),float(frq),float(phs))
        if amp_value>5 or amp_value<0: return "wrong amplitude" 
        if frq_value<1 or frq_value>10000: return "wrong amplitude"
        if phs_value<-360 or phs_value>360: return "wrong phase" 
        self.send("lockin_setting,"+amp+","+frq+","+phs)
        status = self.recv()
        return status

#query the setting: amplitude (V), frequency(Hz), phase(deg)
    def lockin_setting_q(self):
        self.send("lockin_setting_q")
        message = self.recv()
        return message    


#set the modulation/demodulation channel: mod, demod
    def lockin_channel(self,mod,demod):
        mod_value , demod_value = (int(mod),int(demod))
        if min(mod_value,demod_value)<0 or max(mod_value,demod_value)>23: return "wrong channel range" 
        self.send("lockin_channel,"+mod+","+demod)
        status = self.recv()
        return status

#query the modulation/demodulation channel: mod, demod
    def lockin_channel_q(self):
        self.send("lockin_channel_q")
        message = self.recv()
        return message    



    def recv(self):
        return(self.s.recv(1024))

    def send(self,msg):
        n = len(msg)
        self.s.sendall(bytes("{:3}".format(n), encoding='utf8'))
        self.s.sendall(bytes("{}".format(msg), encoding='utf8'))    

