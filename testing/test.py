import numpy as np
import pandas as pd

a = np.empty((5,3))
# print(a)

a[0,:] = [1,2,3]
# a = np.append(a,[1,2,3,4,5])
print(a)
j=1
np.savetxt("C:\\Users\\VFSTM-PC3\\Documents\\InstrumentHub\\InstrumentHub\\data\\data{0}.csv".format(j), a, delimiter=",")

