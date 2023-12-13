import sys
import time
import numpy as np

# from ApplicationKernel import AppServer
# app = AppServer("app_T_record")
# itc = app.addInstrument('inst_itcGPIB')

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import (QApplication , QWidget , QGridLayout ,
                QPushButton , QTimeEdit , QLineEdit , QSpinBox , QLabel,
                QScrollArea)
from PySide6.QtCore import Signal , Qt 

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class Ui_Widget():
    def setupUi(self, Widget):
        Widget.setObjectName(u"Temperture control")
        Widget.setWindowTitle(Widget.objectName())
        Widget.resize(1000, 500)

        #Plot
        self.canvas = FigureCanvas(Figure())

        #Message
        self.lineEdit_path = QLineEdit("D:\\temperature record\\")
        self.scrollArea_message = QScrollArea()
        self.lable_message = QLabel("Message here\n\n\n\n\n\n\n\n\nand here")
        self.scrollArea_message.setWidget(self.lable_message)

        #control
        self.buttonC = QPushButton("control")

        #For refill
        self.lable_status = QLabel("One")
        self.timeEdit_schedule = QTimeEdit()
        self.spinBox_openTo = QSpinBox()
        self.button_autoClose = QPushButton("Auto close")
        self.button_schedule = QPushButton("schedule")
        self.button_openTo = QPushButton("open to")

        #main layout
        self.mainLayout = QGridLayout(Widget)

        #left top (temperature)
        self.LTLayout = QGridLayout()
        self.LTLayout.addWidget(self.canvas, 0, 0)
        self.LTLayout.addWidget(NavigationToolbar(self.canvas, Widget), 1, 0)
        self.ax = self.canvas.figure.subplots()
        t = np.linspace(0, 10, 501)
        self.ax.plot(t, np.tan(t), ".")


        #left bottom (message)
        self.LBLayout = QGridLayout()
        self.LBLayout.addWidget(self.lineEdit_path, 0, 0)
        self.LBLayout.addWidget(self.scrollArea_message, 1, 0)

        #right top (read control)
        self.RTLayout = QGridLayout()
        self.RTLayout.addWidget(self.buttonC, 0, 0)

        #right bottom (refill 1K pot)
        self.RBLayout = QGridLayout()
        self.RBLayout.addWidget(self.lable_status, 0, 0)
        self.RBLayout.addWidget(self.timeEdit_schedule, 1, 0)
        self.RBLayout.addWidget(self.spinBox_openTo, 2, 0)
        self.RBLayout.addWidget(self.button_autoClose, 0, 1)
        self.RBLayout.addWidget(self.button_schedule, 1, 1)
        self.RBLayout.addWidget(self.button_openTo, 2, 1)


        self.mainLayout.addLayout(self.LTLayout,0,0,3,5)
        self.mainLayout.addLayout(self.LBLayout,3,0)
        self.mainLayout.addLayout(self.RTLayout,0,5)
        self.mainLayout.addLayout(self.RBLayout,3,5)



        




class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

def get_darkModePalette( app=None ) :
    darkPalette = app.palette()
    darkPalette.setColor( QPalette.Window, QColor( 53, 53, 53 ) )
    darkPalette.setColor( QPalette.WindowText, Qt.white )
    darkPalette.setColor( QPalette.Disabled, QPalette.WindowText, QColor( 127, 127, 127 ) )
    darkPalette.setColor( QPalette.Base, QColor( 42, 42, 42 ) )
    darkPalette.setColor( QPalette.AlternateBase, QColor( 66, 66, 66 ) )
    darkPalette.setColor( QPalette.ToolTipBase, Qt.white )
    darkPalette.setColor( QPalette.ToolTipText, Qt.white )
    darkPalette.setColor( QPalette.Text, Qt.white )
    darkPalette.setColor( QPalette.Disabled, QPalette.Text, QColor( 127, 127, 127 ) )
    darkPalette.setColor( QPalette.Dark, QColor( 35, 35, 35 ) )
    darkPalette.setColor( QPalette.Shadow, QColor( 20, 20, 20 ) )
    darkPalette.setColor( QPalette.Button, QColor( 53, 53, 53 ) )
    darkPalette.setColor( QPalette.ButtonText, Qt.white )
    darkPalette.setColor( QPalette.Disabled, QPalette.ButtonText, QColor( 127, 127, 127 ) )
    darkPalette.setColor( QPalette.BrightText, Qt.red )
    darkPalette.setColor( QPalette.Link, QColor( 42, 130, 218 ) )
    darkPalette.setColor( QPalette.Highlight, QColor( 42, 130, 218 ) )
    darkPalette.setColor( QPalette.Disabled, QPalette.Highlight, QColor( 80, 80, 80 ) )
    darkPalette.setColor( QPalette.HighlightedText, Qt.white )
    darkPalette.setColor( QPalette.Disabled, QPalette.HighlightedText, QColor( 127, 127, 127 ), )
    return darkPalette

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette( get_darkModePalette( app ) )
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
