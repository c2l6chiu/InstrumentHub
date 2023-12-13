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
        Widget.resize(1000, 600)

        #Plot
        canvas = FigureCanvas(Figure())

        #Message
        lineEdit_path = QLineEdit("D:\\temperature record\\")
        scrollArea_message = QScrollArea()
        lable_message = QLabel("Message here\n\n\n\n\n\n\n\n\nand here")
        scrollArea_message.setWidget(lable_message)

        #control
        buttonC = QPushButton("control")

        #For refill
        lable_status = QLabel("One")
        timeEdit_schedule = QTimeEdit()
        spinBox_openTo = QSpinBox()
        button_autoClose = QPushButton("Auto close")
        button_schedule = QPushButton("schedule")
        button_openTo = QPushButton("open to")

        #main layout
        mainLayout = QGridLayout(Widget)

        #left top (temperature)
        LTLayout = QGridLayout()
        LTLayout.addWidget(canvas, 0, 0)
        LTLayout.addWidget(NavigationToolbar(canvas, Widget), 1, 0)
        ax = canvas.figure.subplots()
        t = np.linspace(0, 10, 501)
        ax.plot(t, np.tan(t), ".")


        #left bottom (message)
        LBLayout = QGridLayout()
        LBLayout.addWidget(lineEdit_path, 0, 0)
        LBLayout.addWidget(scrollArea_message, 1, 0)

        #right top (read control)
        RTLayout = QGridLayout()
        RTLayout.addWidget(buttonC, 0, 0)

        #right bottom (refill 1K pot)
        RBLayout = QGridLayout()
        RBLayout.addWidget(lable_status, 0, 0)
        RBLayout.addWidget(timeEdit_schedule, 1, 0)
        RBLayout.addWidget(spinBox_openTo, 2, 0)
        RBLayout.addWidget(button_autoClose, 0, 1)
        RBLayout.addWidget(button_schedule, 1, 1)
        RBLayout.addWidget(button_openTo, 2, 1)


        mainLayout.addLayout(LTLayout,0,0,6,5)
        mainLayout.addLayout(LBLayout,6,0)
        mainLayout.addLayout(RTLayout,0,5)
        mainLayout.addLayout(RBLayout,6,5)



        




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
