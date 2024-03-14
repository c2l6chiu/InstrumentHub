# #######################################
# ###########  read_channel  ############
# #######################################
print(nanonis.query('read_channel','0','22'))
0: current,.... 22: labview time

# #######################################
# ###########  Z controller  ############
# #######################################
# switch on/off z controller or withdraw
nanonis.query('zctrl_io','on')
on: 'on'; off: 'off'

# query z controller status    
nanonis.query('zctrl_io_q')
return (int)
1: on; 0: off 
    
# set z position (int: nm)
nanonis.query('zctrl_z_set',100)
100nm: 100

# query z position (nm)
nanonis.query('zctrl_z_q')
return (float)XXX 
in nm

# set home absolute (nm)
nanonis.query('zctrl_z_home_absolute',100)
100nm: 100

# set home relative (nm)
nanonis.query('zctrl_z_home_relative',100)
100nm: 100

# set z home
nanonis.query('zctrl_z_home')

# set z setpoint (nA)
nanonis.query('zctrl_setpoint',1.2)
800pA: 0.8

# query z setpoint (nA)
nanonis.query('zctrl_setpoint_q')
return (float)XXX
in nA

# set z PI P(pm) I(mS)
nanonis.query('zctrl_pi',50,1)
P=50pm: 50
I=1ms: 1

# query z PI P(pm) I(ms)
nanonis.query('zctrl_pi_q')
return (str)"P,I"
P in pm
I in ms

# #######################################
# #########  Bias/Bias Spectrum #########
# #######################################
# set bias value (V)
nanonis.query('bias_bias',-0.01)
-10mV: -0.01

# query bias value (V)
nanonis.query('bias_bias_q')
return (float)XXX
in V

# bias pulse (abs V) (S) (Z-hold on/off 1,0)
nanonis.query('bias_pulse' , 1 , 0.01 , 0)
1V: 1
10ms: 0.01
Z-hold-off: 0 (Z-hold off is the common one)

# switch on/off bias spectroscopy (off: stop on: start)
nanonis.query('bias_spec_io','on')
return (str)XXX
["bias, channelXXX, , channelYYY, ..."]

# query bias spectroscopy status (1:running, 0: stopped)
nanonis.query('bias_spec_q')
return (int)X
1: running
0: stopped

# set bias spectroscopy sweeping range (V)
nanonis.query('bias_spec_sweep',-0.2,0.2)
from -200mV: -0.2
to 200mV: 0.2

# query bias spectroscopy sweeping range (V)
nanonis.query('bias_spec_sweep_q')
return (str)"XXX,YYY"
from XXX (V)
to YYY (V)

# set bias spectroscopy sweeping channel (ex: 0,1,2,3)
nanonis.query('bias_spec_channel',0,1,2)
0: current
1, LockinX
2, LockinY

########################################
###############  Current  ##############
########################################

#query current, 1 data (nA)
    def current(self):

# print(nanonis.query("current()"))

########################################
###############  Walker  ###############
########################################

#set walker voltage(V) freuqency(mS)
    def walker_setting(self,volt,freq):

#query walker voltage(V) freuqency(mS)
    def walker_setting_q(self):

#walk bipolar (will NOT hold until finish walking)
    def walker_walk(self,dir,step):

#walk unipolar z (will NOT hold until finish walking)
    def walker_uni_walk(self,dir,step):

#walker stop immediately
    def walker_stop(self):

# print(nanonis.query("walker_setting('123','321')"))
# print(nanonis.query("walker_setting_q()"))
# print(nanonis.query("walker_walk('z-','500')"))
# print(nanonis.query("walker_uni_walk('x-','500')"))
# print(nanonis.query("walker_stop()"))

########################################
###########  Move/Position  ############
########################################

#move to x,y (nm)
    def move_move(self,x,y):

#stop follow me now!
    def move_stop(self):

#query current x,y (nm)
    def move_q(self):

#set moving/scanning speed (nm/s)
    def move_speed(self,speed):      

#querry moving/scanning speed (nm/s)
    def move_speed_q(self,speed):

# print(nanonis.query("move_move('123','321')"))
# print(nanonis.query("move_stop()"))
# print(nanonis.query("move_q()"))
# print(nanonis.query("move_speed('123')"))
# print(nanonis.query("move_speed_q()"))

########################################
################  Scan  ################
########################################

#start scan (action 0:stop 1: start 2: pause 3: resume) (direction 0:up scan 1:down scan)
    def scan_io(self,action,direction):

#query scan status 0: False 1: True
    def scan_io_q(self):

#receive last scanned data (channel: only one) (direction: 1: forward 2: backward) (always down scan:up to down)
    def scan_get(self,channel,direction):

#set scan method (conti 1:on(change dir after scan) 0:off) (bouncy 1:on 0:off) (autoSave 1:on 0: off 2: next)
    def scan_method(self,conti,bouncy,autoSave,name):

#query scan method (conti 1:on 0:off) (bouncy 1: 0:off) file_name
    def scan_method_q(self):

#set scan resolution (#) (#) (channel: 0,1,14 I,dIdV,Z)
    def scan_res(self,pixel,lines,channel):

#query scan resolution (pixel,lines,channel,channel,...,channel)
    def scan_res_q(self):

#set scan position x(nm),y(nm),sizeX(nm),sizeY(nm), angle(deg)
    def scan_pos(self,x,y,sizeX,sizeY,ang):

#query scan position x(nm),y(nm),sizeX(nm),sizeY(nm), angle(deg)
    def scan_pos_q(self):

#set scan speed speed (forward: nm/s backward: nm/s)
    def scan_speed(self,forward,backward):

#query scan speed
    def scan_speed_q(self):

# print(nanonis.query("scan_io('3','1')"))
# print(nanonis.query("scan_io_q()"))
# a = nanonis.query("scan_get('0','2')")
# print(nanonis.query("scan_method(1,0,0,'test')"))
# print(nanonis.query("scan_method_q()"))
# print(nanonis.query("scan_res(32,32,'[0,1,14]')"))
# print(nanonis.query("scan_res_q()"))
# print(nanonis.query("scan_pos(1.1,1.2,13,14,23)"))
# print(nanonis.query("scan_pos_q()"))
# print(nanonis.query("scan_speed(5,4)"))
# print(nanonis.query("scan_speed_q()"))

########################################
################  Grid  ################
########################################


########################################
###############  Lockin  ###############
########################################

#turn on/off the lock in 1:on 0: off
    def lockin_io(self,arg):

#set the setting: amplitude (V), frequency(Hz), phase(deg)
    def lockin_setting(self,amp,frq,phs):

#query the setting: amplitude (V), frequency(Hz), phase(deg)
    def lockin_setting_q(self):

#set the modulation/demodulation channel: mod, demod
    def lockin_channel(self,mod,demod):

#query the modulation/demodulation channel: mod, demod
    def lockin_channel_q(self):

# print(nanonis.query("lockin_io('on')")) 
# print(nanonis.query("lockin_io('off')")) 
# print(nanonis.query("lockin_setting('2.25','2501','-48.448')"))
# print(nanonis.query("lockin_setting_q()")) 
# print(nanonis.query("lockin_channel('0','1')"))
# print(nanonis.query("lockin_channel_q()")) 

