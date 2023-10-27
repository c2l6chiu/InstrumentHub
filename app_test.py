from ApplicationKernel import AppServer
import time
import matplotlib.pyplot as plt

app = AppServer("app_test")
# nanonis = app.addInstrument('inst_nanonis')
nanonisUDP = app.addInstrument('inst_nanonisUDP')

# t0 = nanonisUDP.query("flush()")
# # print(t0)
# t1 = nanonisUDP.query("get_time()")
# c1 = nanonisUDP.query("get_current()")
# print(t1-t0)

# c2 = nanonisUDP.query("get_current()")
# t2 = nanonisUDP.query("get_time()")
# print(t2-t1)
# print(float(c2)-float(c1))
# print( nanonisUDP.query("get_all()"))


t0=time.time()
t = []
nanonisUDP.query("flush()")
for i in range(100):
    tmp =float( str(nanonisUDP.query("get_time()")))
    t.append(tmp-t0)
    t0 = tmp
print(t)



# plt.ion()
# fig = plt.figure()
# ax = fig.add_subplot()
# ax.plot(t, 'r-')
# fig.show()



# t = time.time()*1000
# (nanonisUDP.query("get_all()"))
# print(time.time()*1000-t)

# (nanonisUDP.query("get_all()"))
# print(time.time()*1000-t)

# (nanonisUDP.query("get_all()"))
# print(time.time()*1000-t)

# (nanonisUDP.query("get_all()"))
# print(time.time()*1000-t)

# print(nanonis.query("zctrl_io('on')"))
# print(nanonis.query("zctrl_io('off')"))
# print(nanonis.query("zctrl_io('withdraw')"))
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

# print(nanonis.query("bias_bias('-0.4321')"))
# print(nanonis.query("bias_bias_q()"))
# print(nanonis.query("bias_pulse('-5','0.2','0')"))
# print(nanonis.query("bias_spec_io('on')"))
# print(nanonis.query("bias_spec_q()"))
# print(nanonis.query("bias_spec_sweep('-0.1234','0.3210')"))
# print(nanonis.query("bias_spec_sweep_q()"))
# print(nanonis.query("bias_spec_channel('0,1,4')"))

# print(nanonis.query("current()"))

# print(nanonis.query("walker_setting('123','321')"))
# print(nanonis.query("walker_setting_q()"))
# print(nanonis.query("walker_walk('z-','500')"))
# print(nanonis.query("walker_uni_walk('x-','500')"))
# print(nanonis.query("walker_stop()"))

# print(nanonis.query("move_move('13','-321')"))
# print(nanonis.query("move_stop()"))
# print(nanonis.query("move_q()"))
# print(nanonis.query("move_speed('13')"))
# print(nanonis.query("move_speed_q()"))


# print(nanonis.query("lockin_io('on')")) 
# print(nanonis.query("lockin_io('off')")) 
# print(nanonis.query("lockin_setting('2.2','2500','-48.447')"))
# print(nanonis.query("lockin_setting_q()")) 
# print(nanonis.query("lockin_channel('8','3')"))
# print(nanonis.query("lockin_channel_q()")) 



# import time
# from statistics import mean,stdev

# max_diff = 0
# counter = 0
# d = [0. for i in range(1000)]

# while True:
#     counter +=1
#     counter = counter%1000
#     a=str(time.time())
#     # print(a)

#     b = nanonis.query("echo('"+a+"')")
#     c=str(time.time())
    

#     diff = ((float(c)-float(a))*1000)
#     d[counter] = diff


#     max_diff = max(max_diff,diff)
#     if counter % 1000 == 0:
#         print(max_diff)
#         print(mean(d))
#         print(stdev(d))


