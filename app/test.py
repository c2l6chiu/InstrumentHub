# import subprocess
# import os
# # subprocess.Popen("conda run -n VFstm python "+os.getcwd()+"/app/app_Tpot.py", shell=True)


# from ApplicationKernel import AppServer

# app = AppServer("TPot")
# itc = app.addInstrument("inst_itc")
# SR = app.addInstrument('inst_SR860')

# print(itc.query("get_1K"))
# SR.query('osc',0.0)

# for i in range(100):
#     result = itc.query("get_1K()")
#     if float(result) == 0:
#         print('zero')

# # print("yo")


# # import pandas

# # import time
# # time.sleep(5)



# from ApplicationKernel import AppServer

# app = AppServer("TPot")
# SR = app.addInstrument('inst_SR860')

# print(SR.query("harm('1')"))
# print(SR.query("harm_q()"))

from ApplicationKernel import AppServer

app = AppServer("TPot")
nanonis = app.addInstrument('inst_nanonis')
a = \
nanonis.query('move_speed_q')

print(a)