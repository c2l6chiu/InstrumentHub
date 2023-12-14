import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')


from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np
from ApplicationKernel import AppServer

app = AppServer("app_figure_test")
itc = app.addInstrument('inst_itcSIM')
print(itc.query("get_1K()"))



x = np.array([])
y = np.array([])


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
    


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self , *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.counter = 0
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)
        n_data = 50
        self.xdata = x = np.array([])
        self.ydata = y = np.array([])
        self.update_plot()

        self.show()

        


        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(4000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def closeEvent(self, event):
        # here you can terminate your threads and do other stuff
        app.__del__()
        itc.__del__()
        # and afterwards call the closeEvent of the super-class
        super().closeEvent(event)
    

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.counter+=1
        self.xdata = np.append(self.xdata,self.counter)
        self.ydata = np.append(self.ydata,itc.query("get_1K()"))
        itc.query("get_1K()")
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


widg = QtWidgets.QApplication(sys.argv)
w = MainWindow()
widg.exec_()
# print(float(itc.query("get_t1()")))