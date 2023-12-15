import sys
import time
import datetime
import numpy as np
import pandas as pd

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import (QApplication , QWidget , QGridLayout ,
                QPushButton , QTimeEdit , QLineEdit , QSpinBox , QLabel,
                QScrollArea , QCheckBox)
from PySide6.QtCore import Slot , Qt  , QTimer , QTime

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from matplotlib.figure import Figure
import matplotlib.dates as mdates

from ApplicationKernel import AppServer

class Ui_Widget():
    def setupUi(self, Widget):
        Widget.setObjectName(u"Temperture control")
        Widget.setWindowTitle(Widget.objectName())
        Widget.resize(1000, 600)

        #Plot
        self.canvas = FigureCanvas(Figure())

        #Message
        self.lineEdit_path = QLineEdit("D:\\temperature record\\")
        # self.lineEdit_path = QLineEdit("/Users/c2l6chiu/Library/CloudStorage/OneDrive-SharedLibraries-PrincetonUniversity/VFstm - Documents/tmp/")
        self.scrollArea_message = QScrollArea()
        self.lable_message = QLabel()
        self.scrollArea_message.setWidget(self.lable_message)

        #control
        self.lineEdit_ymax = QLineEdit("10")
        self.lineEdit_ymax.setMaximumWidth(80)
        self.lineEdit_ymin = QLineEdit("0")
        self.lineEdit_ymin.setMaximumWidth(80)
        self.checkBox_autoScale = QCheckBox("Auto Scale")
        self.checkBox_autoScale.setChecked(True)
        self.checkBox_manualScale = QCheckBox("Manual Scale")
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
        self.SpinBox_numberDay = QSpinBox()
        self.SpinBox_numberDay.setValue(1)
        self.SpinBox_numberDay.setMinimum (1)
        self.SpinBox_numberDay.setMaximum (14)
        self.lable_NV = QLabel("??")
        self.lable_currentTime = QLabel("??")
        self.pushButton_Update = QPushButton("Update Now")
        self.SpinBox_samplingRate = QSpinBox()
        self.SpinBox_samplingRate.setMinimum(1)
        self.SpinBox_samplingRate.setMaximum(600)
        self.SpinBox_samplingRate.setValue(120)


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
        # t = np.linspace(0, 10, 501)
        # self.ax.plot(t, np.tan(t), ".")

        #left bottom (message)
        self.LBLayout = QGridLayout()
        self.LBLayout.addWidget(self.lineEdit_path, 0, 0)
        self.LBLayout.addWidget(self.scrollArea_message, 1, 0)

        #right top (read control)
        self.RTLayout = QGridLayout()
        self.RTLayout.addWidget(QLabel("T Max"), 0, 0)
        self.RTLayout.addWidget(QLabel("T Min"), 1, 0)
        self.RTLayout.addWidget(self.lineEdit_ymax, 0, 1)
        self.RTLayout.addWidget(self.lineEdit_ymin, 1, 1)
        self.RTLayout.addWidget(self.checkBox_autoScale, 0, 2)
        self.RTLayout.addWidget(self.checkBox_manualScale, 1, 2)
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
        self.RTLayout.addWidget(QLabel("Current NV"), 10, 3)
        self.RTLayout.addWidget(self.lable_NV, 11, 3)
        self.RTLayout.addWidget(self.lable_currentTime,12,3)
        self.RTLayout.addWidget(QLabel("# Days"), 11, 0)
        self.RTLayout.addWidget(self.SpinBox_numberDay, 11, 1)
        self.RTLayout.addWidget(QLabel("sampling rate"), 12, 0)
        self.RTLayout.addWidget(self.SpinBox_samplingRate, 12, 1)
        self.RTLayout.addWidget(QLabel(""), 13, 1)
        

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


        self.mainLayout.addLayout(self.LTLayout,0,0)
        self.mainLayout.addLayout(self.LBLayout,1,0)
        self.mainLayout.addLayout(self.RTLayout,0,1)
        self.mainLayout.addLayout(self.RBLayout,1,1)
        self.mainLayout.setColumnStretch(0, 100)
        self.mainLayout.setRowStretch(0, 10)

    def connectUi(self, Widget):
        self.lineEdit_ymax.textChanged.connect(Widget.change_yScale)
        self.lineEdit_ymin.textChanged.connect(Widget.change_yScale)
        self.checkBox_autoScale.stateChanged.connect(Widget.autoScale)
        self.checkBox_manualScale.stateChanged.connect(Widget.manualScale)
        self.checkBox_1K.stateChanged.connect(Widget.state_1K)
        self.checkBox_SHD_TOP.stateChanged.connect(Widget.state_SHD_TOP)
        self.checkBox_MAG_TOP.stateChanged.connect(Widget.state_MAG_TOP)
        self.checkBox_MAG_BOT.stateChanged.connect(Widget.state_MAG_BOT)
        self.pushButton_Update.clicked.connect(Widget.force_measure)
        self.SpinBox_numberDay.valueChanged.connect(Widget.dayShown)
        self.SpinBox_samplingRate.valueChanged.connect(Widget.changeRate)
        self.CheckBox_schedule.stateChanged.connect(Widget.potSchedule)
        self.button_refill.clicked.connect(Widget.refill)
        self.button_setNV.clicked.connect(Widget.setNV)
        self.button_closeNV.clicked.connect(Widget.closeNV)

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #connect to ITC
        self.app = AppServer("app_Tcontroll")
        self.itc = self.app.addInstrument("inst_itcSIM")

        #time stamp base (using Labview standard, Easter time)
        self.EPOCH_labview = pd.Timestamp('1904-01-01 0:0:0',tz="UTC").tz_convert('US/Eastern').tz_localize(None)
        self.potFullT = 1.5     #filled up temperature
        self.refill_state = False   #whether the 1K pot is filling with monitor on
        self.initail_cool = False

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.connectUi(self)

        #for the first data point
        self.measure()
        self.loadData()
        self.update()
        
        #first message
        self.message=[]
        self.updateMessage("launch temperature control")

        #measuring timer
        self.samplingTimer = QTimer()
        rate = self.ui.SpinBox_samplingRate.value()
        self.samplingTimer.setInterval(rate*1000)
        self.samplingTimer.timeout.connect(self.force_measure)
        self.samplingTimer.start()

        #pot scheduler timer
        self.scheduleTimer = QTimer()
        self.scheduleTimer.setSingleShot(True)
        self.scheduleTimer.timeout.connect(self.timesUp)

        #pot monitor timer (I am using every 5 second for now)
        self.potMonitorTimer = QTimer()
        self.potMonitorTimer.setInterval(10*1000)
        self.potMonitorTimer.timeout.connect(self.refill_monitor)

    def closeEvent(self, event):
        del self.app
        super().closeEvent(event)

    def updateMessage(self,new_msg):
        self.message.append(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M ")) + new_msg)
        if len(self.message) > 100:
            self.message = self.message[10:len(self.message)]
        self.ui.lable_message.setText("\n".join(self.message))
        self.ui.lable_message.adjustSize()
        vbar = self.ui.scrollArea_message.verticalScrollBar()
        vbar.setValue(vbar.maximum())

    def loadData(self):
        n_days = self.ui.SpinBox_numberDay.value()
        first_date = datetime.date.today()-datetime.timedelta(days=n_days-1)
        path_name = []
        for i in range(n_days):
            date = first_date+datetime.timedelta(days=i)
            year , month , day = (date.year%100 , date.month , date.day)
            path_name.append("{0}{1:02d}{2:02d}{3:02d}.txt".format(self.ui.lineEdit_path.text(),year,month,day))

        self.time = np.empty(0)
        self.T_1K = np.empty(0)
        self.T_SHD_TOP = np.empty(0)
        self.T_MAG_TOP = np.empty(0)
        self.T_MAG_BOT = np.empty(0)
        for path_name_ind in path_name:
            try:
                df = pd.read_csv(path_name_ind , header=None)
            except:
                continue
            self.time = np.append(self.time , np.asarray(df[0]))
            self.T_1K = np.append(self.T_1K , np.asarray(df[1]))
            self.T_SHD_TOP = np.append(self.T_SHD_TOP , np.asarray(df[2]))
            self.T_MAG_TOP = np.append(self.T_MAG_TOP , np.asarray(df[3]))
            self.T_MAG_BOT = np.append(self.T_MAG_BOT , np.asarray(df[4]))
        self.time = np.asarray(pd.to_datetime(self.time,unit="s",origin=self.EPOCH_labview))
        self.mostCurrentTime = self.time[-1]
        self.mostCurrentT_1K = self.T_1K[-1]

    def update(self):
        left , right = self.ui.ax.get_xlim()
        bottom , top = self.ui.ax.get_ylim()

        self.loadData()
        self.ui.ax.clear()
        
        if self.ui.checkBox_1K.isChecked():
            self.ui.ax.plot(self.time , self.T_1K)
        if self.ui.checkBox_SHD_TOP.isChecked():
            self.ui.ax.plot(self.time , self.T_SHD_TOP)
        if self.ui.checkBox_MAG_TOP.isChecked():
            self.ui.ax.plot(self.time , self.T_MAG_TOP)
        if self.ui.checkBox_MAG_BOT.isChecked():
            self.ui.ax.plot(self.time , self.T_MAG_BOT)

        if self.ui.checkBox_manualScale.isChecked():
            self.ui.ax.set_xlim(left , right)
            self.ui.ax.set_ylim(bottom , top)
        else:
            self.ui.ax.autoscale()
        dtFmt = mdates.DateFormatter("%m-%d\n%H:%M") # define the formatting
        self.ui.ax.xaxis.set_major_formatter(dtFmt) 
        self.ui.canvas.figure.canvas.draw()

    def measure(self):
        #save data into file only, won't update self.T,self.t
        T_1K = self.itc.query("get_1K()") if self.ui.checkBox_1K.isChecked() else 0.
        T_SHD_TOP = self.itc.query("get_SHD_TOP()") if self.ui.checkBox_SHD_TOP.isChecked() else 0.
        T_MAG_TOP = self.itc.query("get_MAG_TOP()") if self.ui.checkBox_MAG_TOP.isChecked() else 0.
        T_MAG_BOT = self.itc.query("get_MAG_BOT()") if self.ui.checkBox_MAG_BOT.isChecked() else 0.
        time_now = pd.Timestamp.now()-self.EPOCH_labview
        time_now = int(time_now.total_seconds())
        today_date = datetime.date.today()
        year , month , day = (today_date.year%100 , today_date.month , today_date.day)
        path_name = "{0}{1:02d}{2:02d}{3:02d}.txt".format(self.ui.lineEdit_path.text(),year,month,day)

        with open(path_name,'a') as file:
            file.write("{0:d},{1:.4f},{2:.4f},{3:.4f},{4:.4f}\n".format(time_now,T_1K,T_SHD_TOP,T_MAG_TOP,T_MAG_BOT))

        self.ui.LCD_1K.setText("{0:.4f}".format(T_1K))
        self.ui.LCD_SHD_TOP.setText("{0:.4f}".format(T_SHD_TOP))
        self.ui.LCD_MAG_TOP.setText("{0:.4f}".format(T_MAG_TOP))
        self.ui.LCD_MAG_BOT.setText("{0:.4f}".format(T_MAG_BOT))

        #NV position
        self.ui.lable_NV.setText(str(self.itc.query("get_NV()")))
        #current time
        self.ui.lable_currentTime.setText("current time\n "+QTime.currentTime().toString())

    def fill_pot(self):
        self.refill_state = True
        NV = int(self.ui.lineEdit_openTo.text())
        T_threshold = float(self.ui.lineEdit_threshold.text())
        self.ui.button_refill.setStyleSheet("background-color: red")
        self.ui.button_refill.setText("refilling...")
        self.itc.query("set_NV("+str(NV)+")")
        self.refill_monitor_on(T_threshold)

        self.updateMessage("refilling 1K pot NV="+str(NV)+" threshold= "+"{0:.4f}".format(T_threshold))
        self.updateMessage("pot monitor on")

        # if not self.ui.CheckBox_repeat.isChecked(): self.ui.CheckBox_schedule.setChecked(False) 

    def stop_fill_pot(self):
        self.refill_state = False
        self.ui.button_refill.setStyleSheet("background-color: rgb(53, 53, 53)")
        self.ui.button_refill.setText("refill now")
        self.refill_monitor_off()
        self.itc.query("set_NV(0)")

        self.updateMessage("stop filling NV=0")
        self.updateMessage("pot monitor off")

    def refill_monitor_on(self,threshold):
        self.potFullT = threshold

        #check if this is refilling from empty pot
        time_gap = pd.Timedelta(seconds=5)
        time_now = pd.Timestamp.now()
        T1K_now = self.itc.query("get_1K()") if time_now-self.mostCurrentTime > time_gap else self.mostCurrentT_1K

        if T1K_now > self.potFullT-0.01:
            self.initail_cool = True
            self.updateMessage("current temperature higher than threshold...")
        else:
            self.initail_cool = False

        self.potMonitorTimer.start()

    def refill_monitor_off(self):
        self.potMonitorTimer.stop()

    @Slot()
    def refill_monitor(self):
        time_gap = pd.Timedelta(seconds=5)
        time_now = pd.Timestamp.now()
        T1K_now = self.itc.query("get_1K()") if time_now-self.mostCurrentTime > time_gap else self.mostCurrentT_1K
        if self.initail_cool and T1K_now < self.potFullT-0.01:
            self.updateMessage("temperature drop below threshold, start refill monitor")
            self.initail_cool = False

        if (not self.initail_cool) and T1K_now > self.potFullT:
            self.stop_fill_pot()
        # else:
        #     print("not full yet")

    @Slot()
    def change_yScale(self):
        bottom , top = (float(self.ui.lineEdit_ymin.text()) , float(self.ui.lineEdit_ymax.text()))
        self.ui.ax.set_ylim(bottom , top)
        self.update()

    @Slot()
    def autoScale(self):
        if self.ui.checkBox_autoScale.isChecked():
            self.ui.checkBox_manualScale.setChecked(False)
        else:
            self.ui.checkBox_manualScale.setChecked(True)
        self.update()

    @Slot()
    def manualScale(self):
        if self.ui.checkBox_manualScale.isChecked():
            self.ui.checkBox_autoScale.setChecked(False)
        else:
            self.ui.checkBox_autoScale.setChecked(True)
        self.update()

    @Slot()
    def state_1K(self):
        self.update()

    @Slot()
    def state_SHD_TOP(self):
        self.update()

    @Slot()
    def state_MAG_TOP(self):
        self.update()

    @Slot()
    def state_MAG_BOT(self):
        self.update()

    @Slot()
    def force_measure(self):
        self.measure()
        self.loadData()
        self.update()

    @Slot()
    def dayShown(self):
        self.loadData()
        self.update()

    @Slot()
    def changeRate(self):
        rate = self.ui.SpinBox_samplingRate.value()
        self.samplingTimer.setInterval(rate*1000)

    @Slot()
    def potSchedule(self):
        if self.ui.CheckBox_schedule.isChecked() == True:
            time_now = QTime.currentTime()
            time_schedule = self.ui.timeEdit_schedule.time()
            time_remainS = (time_schedule.hour()-time_now.hour())*3600 + \
                            (time_schedule.minute()-time_now.minute())*60 +\
                            (0-time_now.second())
            if time_remainS <= 0:
                time_remainS +=86400
                self.updateMessage("schedule for tomorrow")
            else:
                self.updateMessage("schedule for today")
            self.scheduleTimer.setInterval(time_remainS*1000)
            self.scheduleTimer.start()


            self.updateMessage("schedule refill at " + self.ui.timeEdit_schedule.text() + \
             ", NV to: " + self.ui.lineEdit_openTo.text() + ", threshold: " + self.ui.lineEdit_threshold.text())
        else:
            if not self.refill_state: 
                self.updateMessage("cancel scheduled refill")
            self.scheduleTimer.stop()

    @Slot()
    def timesUp(self):
        self.fill_pot()
        if self.ui.CheckBox_repeat.isChecked():
            self.potSchedule()
        else:
            self.ui.CheckBox_schedule.setChecked(False) 

    @Slot()
    def refill(self):
        if not self.refill_state: self.fill_pot()
        else: self.stop_fill_pot()

    @Slot()
    def setNV(self):
        self.updateMessage("set_NV("+self.ui.lineEdit_setTo.text()+")")
        self.itc.query("set_NV("+self.ui.lineEdit_setTo.text()+")")
        if self.refill_state: self.stop_fill_pot()

    @Slot()
    def closeNV(self):
        self.updateMessage("close NV")
        self.itc.query("set_NV(0)")
        if self.refill_state: self.stop_fill_pot()


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
    # app.exec()
    sys.exit(app.exec())


