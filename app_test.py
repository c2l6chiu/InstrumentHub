from ApplicationKernel import AppServer


app = AppServer("app_test")
nanonis = app.addInstrument('inst_nanonis')

print(nanonis.query("zctrl_io('on')e"))
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
