import numpy as np
import pandas as pd

from ApplicationKernel import AppServer

app = AppServer("tipTrack")
nanonis = app.addInstrument("inst_nanonis")


'''
0: current
12: X
13: Y
14: Z
22: time
'''


sampling = 10000
buffer = np.empty((sampling,5))

for j in range(100):
    for i in range(sampling):
        str = nanonis.query("read_channel('0,12,13,14,22')")
        buffer[i,:] = str


    np.savetxt("C:\\Users\\VFSTM-PC3\\Documents\\InstrumentHub\\InstrumentHub\\data\\data{0}.csv".format(j), buffer, delimiter=",")


