from ApplicationKernel import AppServer
import time
import datetime

app = AppServer("app_T_record")
itc = app.addInstrument('inst_itcGPIB')



percent = 0
th_temperature = 1.52
delay = 2

startTime = datetime.datetime.today()
startTemperature = itc.query("get_t1()")

print('start time: '+startTime.strftime('%d/%m/%y %H:%M:%S'))  
print('start temperature: %2.3f' % startTemperature)

itc.query("set_nv(25)")
print('opened needlevalve '+str(percent)+' percent')
print('filling 1K pot ...')

# wait until temperature reach the threshhold temperature
currentTemperature = itc.query("get_t1()")
if currentTemperature > th_temperature:
    print('Current temperaure is higher than threshhold temperature')
    while currentTemperature > (th_temperature-0.005):
        time.sleep(delay)
        currentTemperature = itc.query("get_t1()")
        currentTime = datetime.datetime.today()
    print('temperaure is lower than the threshhold temperature now')

#fill pot until temperature raise above threshold
currentTemperature = itc.query("get_t1()")
while currentTemperature < th_temperature:
    time.sleep(delay)
    currentTemperature = itc.query("get_t1()")
    currentTime = datetime.datetime.today()
itc.query("set_nv(0)")

# display current time and temperature
finishTime = datetime.datetime.today()
print('finish time: '+finishTime.strftime('%d/%m/%y %H:%M:%S'))
print('total filling time: %d mins' % round((finishTime-startTime).seconds / 60))