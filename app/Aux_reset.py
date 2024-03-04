import time

from ApplicationKernel import AppServer

app = AppServer("Aux_reset")
ard = app.addInstrument("inst_arduino")

ard.query('Aux_off()')

time.sleep(3)

ard.query('Aux_on()')

print("Aux is reset")