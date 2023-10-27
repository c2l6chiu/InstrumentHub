from ApplicationKernel import AppServer
import time
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
from queue import Queue


app = AppServer("app_T_record")
itc = app.addInstrument('inst_itc')


# print(itc.query("get_t1()"))


x = np.array([])
y = np.array([])

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()


fig = plt.figure()
ax = fig.add_subplot()

line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

counter = 0
d = 4

que = Queue()


class GetT:
    def __init__(self,que) -> None:
        self.que = que
    def run(self):
        while True:
            self.que.put(float(itc.query("get_t1()")))
            time.sleep(1)


getT = GetT(que)
t = Thread(target=getT.run)
t.start()

while True:
    tmp = que.get()
    print(tmp)
    counter+=d
    tmp = itc.query("get_t1()")
    if tmp !=0:
        x = np.append(x,counter)
        y = np.append(y,tmp)

    line1.set_xdata(x)
    line1.set_ydata(y)

    plt.xlim([x.min(),x.max()])
    plt.ylim([y.min(),y.max()])

    fig.canvas.draw()
    fig.canvas.flush_events()



