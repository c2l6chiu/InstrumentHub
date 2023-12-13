import sys
import time
import numpy as np

# from ApplicationKernel import AppServer
# app = AppServer("app_T_record")
# itc = app.addInstrument('inst_itcGPIB')

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import (QApplication , QWidget , QGridLayout ,
                QPushButton , QTimeEdit , QLineEdit , QSpinBox , QLabel,
                QScrollArea , QLCDNumber , QCheckBox)
from PySide6.QtCore import Signal , Slot , Qt 

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
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
        self.lineEdit_ymax = QLineEdit("0")
        self.lineEdit_ymax.setMaximumWidth(80)
        self.lineEdit_ymin = QLineEdit("10")
        self.lineEdit_ymin.setMaximumWidth(80)
        self.button_autoScale = QPushButton("Auto Scale")
        self.button_manualScale = QPushButton("Manual Scale")
        self.label_1K = QLabel("1K pot")
        self.label_SHD_TOP = QLabel("SHD TOP")
        self.label_MAG_TOP = QLabel("MAG TOP")
        self.label_MAG_BOT = QLabel("MAG BOT")
        self.LCD_1K = QLabel("+0.00")
        self.LCD_SHD_TOP = QLabel("+0.00")
        self.LCD_MAG_TOP = QLabel("+0.00")
        self.LCD_MAG_BOT = QLabel("+0.00")
        self.checkBox_1K = QCheckBox()
        self.checkBox_1K.setChecked(True)
        self.checkBox_SHD_TOP = QCheckBox()
        self.checkBox_MAG_TOP = QCheckBox()
        self.checkBox_MAG_BOT = QCheckBox()
        self.lable_1K = QLabel("+0.00")
        self.lable_SHD_TOP = QLabel("+0.00")
        self.lable_MAG_TOP = QLabel("+0.00")
        self.lable_MAG_BOT = QLabel("+0.00")
        self.lable_numberDay = QLabel("# Days")
        self.SpinBox_numberDay = QSpinBox()
        self.SpinBox_numberDay.setValue(1)
        self.SpinBox_numberDay.setMinimum (1)
        self.pushButton_Update = QPushButton("Update Now")


        #For refill
        self.CheckBox_schedule = QCheckBox("schedule")
        self.CheckBox_repeat = QCheckBox("repeat?")
        self.button_refill = QPushButton("refill now")
        self.timeEdit_schedule = QTimeEdit()
        self.timeEdit_schedule.setMaximumWidth(80)
        self.lineEdit_openTo = QLineEdit("40")
        self.lineEdit_openTo.setMaximumWidth(80)
        self.lineEdit_threshold = QLineEdit("1.5")
        self.lineEdit_threshold.setMaximumWidth(80)
        self.button_setNV = QPushButton("set NV to:")
        self.lineEdit_setTo = QLineEdit("40")
        self.lineEdit_setTo.setMaximumWidth(80)
        self.button_closeNV = QPushButton("close NV")

        #main layout
        self.mainLayout = QGridLayout(Widget)

        #left top (temperature)
        self.LTLayout = QGridLayout()
        self.LTLayout.addWidget(self.canvas, 0, 0)
        self.LTLayout.addWidget(NavigationToolbar2QT(self.canvas, Widget), 1, 0)
        self.ax = self.canvas.figure.subplots()
        t = np.linspace(0, 10, 501)
        self.ax.plot(t, np.tan(t), ".")

        #left bottom (message)
        self.LBLayout = QGridLayout()
        self.LBLayout.addWidget(self.lineEdit_path, 0, 0)
        self.LBLayout.addWidget(self.scrollArea_message, 1, 0)

        #right top (read control)
        self.RTLayout = QGridLayout()
        self.RTLayout.addWidget(self.lineEdit_ymin, 0, 0)
        self.RTLayout.addWidget(self.lineEdit_ymax, 1, 0)
        self.RTLayout.addWidget(self.button_autoScale, 0, 2)
        self.RTLayout.addWidget(self.button_manualScale, 1, 1)
        self.RTLayout.addWidget(QLabel(""), 2, 1)
        self.RTLayout.addWidget(QLabel("Temperature"), 3, 1)
        self.RTLayout.addWidget(QLabel("On/Off"), 3, 2)
        self.RTLayout.addWidget(QLabel("rate (K/min)"), 3, 3)
        self.RTLayout.addWidget(self.label_1K, 4, 0)
        self.RTLayout.addWidget(self.label_SHD_TOP, 5, 0)
        self.RTLayout.addWidget(self.label_MAG_TOP, 6, 0)
        self.RTLayout.addWidget(self.label_MAG_BOT, 7, 0)
        self.RTLayout.addWidget(self.LCD_1K, 4, 1)
        self.RTLayout.addWidget(self.LCD_SHD_TOP, 5, 1)
        self.RTLayout.addWidget(self.LCD_MAG_TOP, 6, 1)
        self.RTLayout.addWidget(self.LCD_MAG_BOT, 7, 1)
        self.RTLayout.addWidget(self.checkBox_1K, 4, 2)
        self.RTLayout.addWidget(self.checkBox_SHD_TOP, 5, 2)
        self.RTLayout.addWidget(self.checkBox_MAG_TOP, 6, 2)
        self.RTLayout.addWidget(self.checkBox_MAG_BOT, 7, 2)
        self.RTLayout.addWidget(self.lable_1K, 4, 3)
        self.RTLayout.addWidget(self.lable_SHD_TOP, 5, 3)
        self.RTLayout.addWidget(self.lable_MAG_TOP, 6, 3)
        self.RTLayout.addWidget(self.lable_MAG_BOT, 7, 3)
        self.RTLayout.addWidget(self.pushButton_Update, 8, 1)
        self.RTLayout.addWidget(QLabel(""), 9, 1)
        self.RTLayout.addWidget(QLabel("Display"), 10, 1)
        self.RTLayout.addWidget(self.lable_numberDay, 11, 0)
        self.RTLayout.addWidget(self.SpinBox_numberDay, 11, 1)
        

        #right bottom (refill 1K pot)
        self.RBLayout = QGridLayout()
        self.RBLayout.addWidget(self.CheckBox_schedule, 0, 0)
        self.RBLayout.addWidget(self.CheckBox_repeat, 0, 1)
        self.RBLayout.addWidget(self.button_refill, 0, 2)
        self.RBLayout.addWidget(QLabel("time"), 1, 0)
        self.RBLayout.addWidget(QLabel("open to"), 1, 1)
        self.RBLayout.addWidget(QLabel("threshold"), 1, 2)
        self.RBLayout.addWidget(self.timeEdit_schedule, 2, 0)
        self.RBLayout.addWidget(self.lineEdit_openTo, 2, 1)
        self.RBLayout.addWidget(self.lineEdit_threshold, 2, 2)
        self.RBLayout.addWidget(QLabel("value"), 3, 1)
        self.RBLayout.addWidget(self.button_setNV, 4, 0)
        self.RBLayout.addWidget(self.lineEdit_setTo, 4, 1)
        self.RBLayout.addWidget(self.button_closeNV, 4, 2)


        self.mainLayout.addLayout(self.LTLayout,0,0,3,5)
        self.mainLayout.addLayout(self.LBLayout,3,0)
        self.mainLayout.addLayout(self.RTLayout,0,5)
        self.mainLayout.addLayout(self.RBLayout,3,5)

    def connectUi(self, Widget):
        self.button_autoScale.clicked.connect(Widget.autoScale)
        self.button_manualScale.clicked.connect(Widget.manualScale)
        self.checkBox_1K.stateChanged.connect(Widget.state_1K)
        self.checkBox_SHD_TOP.stateChanged.connect(Widget.state_SHD_TOP)
        self.checkBox_MAG_TOP.stateChanged.connect(Widget.state_MAG_TOP)
        self.checkBox_MAG_BOT.stateChanged.connect(Widget.state_MAG_BOT)
        self.pushButton_Update.clicked.connect(Widget.update)
        self.SpinBox_numberDay.valueChanged.connect(Widget.dayShown)
        self.CheckBox_schedule.stateChanged.connect(Widget.potSchedule)
        self.CheckBox_repeat.stateChanged.connect(Widget.potRepeate)
        self.button_refill.clicked.connect(Widget.refill)
        self.button_setNV.clicked.connect(Widget.setNV)
        self.button_closeNV.clicked.connect(Widget.closeNV)

        

# def stateChanged (arg__1)
# def checkState ()


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()

        self.ui.setupUi(self)
        self.ui.connectUi(self)

        

    @Slot()
    def autoScale(self):
        print("autoscale")

    @Slot()
    def manualScale(self):
        print("manualScale")

    @Slot()
    def state_1K(self):
        print("1K state: ",self.ui.checkBox_1K.isChecked())

    @Slot()
    def state_SHD_TOP(self):
        print("SHD_TOP state: ",self.ui.checkBox_SHD_TOP.isChecked())

    @Slot()
    def state_MAG_TOP(self):
        print("MAG_TOP state: ",self.ui.checkBox_MAG_TOP.isChecked())
    @Slot()
    def state_MAG_BOT(self):
        print("MAG_BOT state: ",self.ui.checkBox_MAG_BOT.isChecked())

    @Slot()
    def update(self):
        print("update")

    @Slot()
    def dayShown(self):
        print("showing",self.ui.SpinBox_numberDay.value())

    @Slot()
    def potSchedule(self):
        print("pot scheduled",self.ui.CheckBox_schedule.isChecked())
        print(self.ui.timeEdit_schedule.text() , " to: " , self.ui.lineEdit_openTo.text() , " threshold: " , self.ui.lineEdit_threshold.text())

    @Slot()
    def potRepeate(self):
        print("pot scheduled",self.ui.CheckBox_repeat.isChecked())

    @Slot()
    def refill(self):
        print("refill")

    @Slot()
    def setNV(self):
        print("set NV to: " , self.ui.lineEdit_setTo.text())

    @Slot()
    def closeNV(self):
        print("closeNV")


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
