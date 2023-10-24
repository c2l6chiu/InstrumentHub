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