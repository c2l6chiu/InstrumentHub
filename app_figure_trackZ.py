import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')


from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np
from ApplicationKernel import AppServer

app = AppServer("app_figure_trackZ")
nanonis = app.addInstrument('inst_nanonis')
print(nanonis.query("read_channel('0,22')"))
t0=nanonis.query("read_channel('22')")

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
        self.xdata = np.array([])
        self.ydata = np.array([])
        self.update_plot()

        self.show()

        


        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
    

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.counter+=1
        t1=nanonis.query("read_channel('22')")
        self.xdata = np.append(self.xdata,(t1[0]-t0[0])/1000)
        self.ydata = np.append(self.ydata,nanonis.query("read_channel('14')"))
        if self.counter%50 == 0:
            self.canvas.axes.cla()  # Clear the canvas.
            self.canvas.axes.plot(self.xdata, self.ydata, 'r')
            # Trigger the canvas to update and redraw.
            self.canvas.draw()


widg = QtWidgets.QApplication(sys.argv)
w = MainWindow()
widg.exec_()
