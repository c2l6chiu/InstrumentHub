from ApplicationKernel import AppServer


app = AppServer("app_test")
nanonis = app.addInstrument('inst_nanonis')

print(nanonis.query("z_zctrl_q()"))
# print(nanonis.query("handShake()"))