########################################
############  Z controller  ############
########################################
#switch on/off z controller or withdraw
    def zctrl_io(self,arg):

#query z controller status    
    def zctrl_io_q(self):
    
#set z position (nm)
    def zctrl_z_set(self,msg):

#query z position (nm)
    def zctrl_z_q(self):

#set home absolute (nm)
    def zctrl_z_home_absolute(self,msg):

#set home relative (nm)
    def zctrl_z_home_relative(self,msg):

#set z home
    def zctrl_z_home(self):

#set z setpoint (nA)
    def zctrl_setpoint(self,msg):

#query z setpoint (nA)
    def zctrl_setpoint_q(self):

#set z PI P(pm) I(mS)
    def zctrl_pi(self):

#query z PI P(pm) I(mS)
    def zctrl_pi(self):

# print(nanonis.query("zctrl_io('on')"))
# print(nanonis.query("zctrl_io('off')"))
# print(nanonis.query("zctrl_io_q()"))
# print(nanonis.query("zctrl_z_set('12')"))
# print(nanonis.query("zctrl_z_q()"))
# print(nanonis.query("zctrl_z_home()"))
# print(nanonis.query("zctrl_z_home_absolute('32')"))
# print(nanonis.query("zctrl_z_home_relative('2')"))
# print(nanonis.query("zctrl_setpoint('0.012112121')"))
# print(nanonis.query("zctrl_setpoint_q()"))
# print(nanonis.query("zctrl_pi('30','1.0')"))
# print(nanonis.query("zctrl_pi_q()"))

########################################
##########  Bias/Bias Spectrum #########
########################################
#set bias value (V)
    def bias_bias(self,msg):

#query bias value (V)
    def bias_bias_q(self,msg):

#bias pulse (abs V) (S) (Z-hold on/off 1,0)
    def bias_pulse(self,volt,duration,hold):

#switch on/off bias spectroscopy (off: stop on: start)
    def bias_spec_io(self,arg):

#query bias spectroscopy status (1:running, 0: stopped)
    def bias_spec_q(self):

#set bias spectroscopy sweeping range (V)
    def bias_spec_sweep(self,fromV,toV):

#query bias spectroscopy sweeping range (V)
    def bias_spec_sweep_q(self):

#set bias spectroscopy sweeping channel (ex: 0,1,2,3)
    def bias_spec_channel(self,channel):

# print(nanonis.query("bias_bias('-0.4321')"))
# print(nanonis.query("bias_bias_q()"))
# print(nanonis.query("bias_pulse('-0.5','0.2',0)"))
# print(nanonis.query("bias_spec_io('on')"))
# print(nanonis.query("bias_spec_q()"))
# print(nanonis.query("bias_spec_sweep('-0.1234','0.3210')"))
# print(nanonis.query("bias_spec_sweep_q('')"))
# print(nanonis.query("bias_spec_channel('0,1,2,4')"))

########################################
###############  Current  ##############
########################################




########################################
###############  Walker  ###############
########################################







########################################
##########  Move/Drift/Tilt  ###########
########################################







########################################
################  Scan  ################
########################################



########################################
################  Grid  ################
########################################



########################################
###############  LockIn  ###############
########################################