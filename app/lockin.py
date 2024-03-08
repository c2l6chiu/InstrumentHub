import sys , os
import datetime, time
import numpy as np
import pandas as pd

from PySide6.QtGui import QPalette, QColor , QIcon
from PySide6.QtWidgets import (QApplication , QWidget , QGridLayout ,
                QPushButton , QLineEdit , QLabel,
                QScrollArea , QComboBox)
from PySide6.QtCore import Slot , Qt  , QTimer , QTime

from matplotlib.backends.backend_qtagg import FigureCanvas , NavigationToolbar2QT
from matplotlib.figure import Figure
import matplotlib.dates as mdates

from ApplicationKernel import AppServer

class Ui_Widget():
    def __init__(self):
        self.sen_dic = ['1V','500mV','200mV',"100mV",'50mV','20mV',"10mV",'5mV','2mV',"1mV",\
                   '500uV','200uV',"100uV"]
        self.tconst_dic = ['100us','300us','1ms','3ms','10ms',\
                      '30ms','100ms','300ms','1s']

    def setupUi(self, Widget):
        Widget.setObjectName(u"Lockin control")
        Widget.setWindowTitle(Widget.objectName())
        Widget.resize(400, 500)
        app_root = os.getcwd()
        os.chdir("..")
        Widget.setWindowIcon(QIcon(os.getcwd()+"/icon/orange.png"))
        os.chdir(app_root)

        #display
        # self.displayX = QLabel('0.0')
        # self.displayY = QLabel('0.0')
        # self.displayR = QLabel('0.0')
        # self.displayT = QLabel('0.0')

        #preset
        self.preset_zero = QPushButton("Zero")
        self.preset_zero.setFixedHeight(80)
        self.preset_two = QPushButton("2V\n Cap")
        self.preset_two.setFixedHeight(80)
        self.preset_one = QPushButton(".1V\n Cu")
        self.preset_one.setFixedHeight(80)
        self.preset_pointTwo = QPushButton(".02V\n Data")
        self.preset_pointTwo.setFixedHeight(80)

        #control
        self.osc_display =  QLabel("0")
        self.osc_display.setMinimumWidth(80)
        self.osc_display.setAlignment(Qt.AlignCenter)
        self.osc_display.setFixedHeight(40)
        self.osc_input = QLineEdit("0")
        self.osc_input.setFixedWidth(100)
        self.osc_input.setAlignment(Qt.AlignCenter)
        self.osc_enter = QPushButton("Set")
        self.osc_preset = QPushButton("0.02V")

        self.sens_display =  QLabel("0")
        self.sens_display.setAlignment(Qt.AlignCenter)
        self.sens_display.setFixedHeight(40)
        self.sens_input = QComboBox()
        self.sens_input.setMaximumWidth(80)
        self.sens_input.addItems(self.sen_dic)
        self.sens_enter = QPushButton("Set")
        self.sens_preset = QPushButton("20mV")

        self.tconst_display =  QLabel("0")
        self.tconst_display.setAlignment(Qt.AlignCenter)
        self.tconst_display.setFixedHeight(40)
        self.tconst_input = QComboBox()
        self.tconst_input.setMaximumWidth(80)
        self.tconst_input.addItems(self.tconst_dic)
        self.tconst_enter = QPushButton("Set")
        self.tconst_preset = QPushButton("1ms")

        self.freq_display =  QLabel("0")
        self.freq_display.setAlignment(Qt.AlignCenter)
        self.freq_display.setFixedHeight(40)
        self.freq_input = QLineEdit("4000")
        self.freq_input.setFixedWidth(100)
        self.freq_input.setAlignment(Qt.AlignCenter)
        self.freq_input.setMaximumWidth(80)
        self.freq_enter = QPushButton("Set")
        self.freq_preset = QPushButton("4000Hz")

        self.phi_display =  QLabel("0")
        self.phi_display.setAlignment(Qt.AlignCenter)
        self.phi_display.setFixedHeight(40)
        self.phi_input = QLineEdit("-62")
        self.phi_input.setFixedWidth(100)
        self.phi_input.setAlignment(Qt.AlignCenter)
        self.phi_input.setMaximumWidth(80)
        self.phi_enter = QPushButton("Set")
        self.phi_preset = QPushButton("-62")

        self.read_all = QPushButton('Update')
        self.read_all.setFixedHeight(40)

        #advanced
        self.adv_4KHz = QPushButton('4KHz setting')
        self.adv_4KHz.setFixedHeight(40)
        self.adv_1KHz = QPushButton('1KHz setting')
        self.adv_1KHz.setFixedHeight(40)
        self.adv_autoPhase = QPushButton('Auto Phase')
        self.adv_autoPhase.setFixedHeight(40)

        #main layout
        self.mainLayout = QGridLayout(Widget)

        #display session
        self.display = QGridLayout()
        self.display.addWidget(QLabel('Lock-In Controller'),0,0)
        # self.display.addWidget(self.displayX,0,0)
        # self.display.addWidget(self.displayY,0,1)
        # self.display.addWidget(self.displayR,1,0)
        # self.display.addWidget(self.displayT,1,1)

        #preset session
        self.preset = QGridLayout()
        self.preset.addWidget(self.preset_zero , 0 , 0)
        self.preset.addWidget(self.preset_two , 0 , 3)
        self.preset.addWidget(self.preset_one , 0 , 2)
        self.preset.addWidget(self.preset_pointTwo , 0 , 1)

        #control session
        self.control = QGridLayout()
        self.control.addWidget(QLabel("Oscillation (V)") , 0 , 0)
        self.control.addWidget(self.osc_display , 0 , 1)
        self.control.addWidget(self.osc_input , 0 , 2)
        self.control.addWidget(self.osc_enter , 0 , 3)
        self.control.addWidget(self.osc_preset , 0 , 4)
        self.control.addWidget(QLabel("Sensitivity (V)") , 1 , 0)
        self.control.addWidget(self.sens_display , 1 , 1)
        self.control.addWidget(self.sens_input , 1 , 2)
        self.control.addWidget(self.sens_enter , 1 , 3)
        self.control.addWidget(self.sens_preset , 1 , 4)
        self.control.addWidget(QLabel("Time Constant") , 2 , 0)
        self.control.addWidget(self.tconst_display , 2 , 1)
        self.control.addWidget(self.tconst_input , 2 , 2)
        self.control.addWidget(self.tconst_enter , 2 , 3)
        self.control.addWidget(self.tconst_preset , 2 , 4)
        self.control.addWidget(QLabel("Frequency (Hz)") , 3 , 0)
        self.control.addWidget(self.freq_display , 3 , 1)
        self.control.addWidget(self.freq_input , 3 , 2)
        self.control.addWidget(self.freq_enter , 3 , 3)
        self.control.addWidget(self.freq_preset , 3 , 4)
        self.control.addWidget(QLabel("Phase") , 4 , 0)
        self.control.addWidget(self.phi_display , 4 , 1)
        self.control.addWidget(self.phi_input , 4 , 2)
        self.control.addWidget(self.phi_enter , 4 , 3)
        self.control.addWidget(self.phi_preset , 4 , 4)
        self.control.addWidget(self.read_all , 5 , 1)

        #advanced session
        self.advanced = QGridLayout()
        self.advanced.addWidget(self.adv_4KHz,0,0)
        self.advanced.addWidget(self.adv_1KHz,0,1)
        self.advanced.addWidget(self.adv_autoPhase,0,2)

        #overall layout
        self.mainLayout.addLayout(self.display,0,0)
        self.mainLayout.addLayout(self.preset,1,0)
        self.mainLayout.addLayout(self.control,2,0)
        self.mainLayout.addLayout(self.advanced,3,0)
        # print(self.mainLayout.rowStretch(1))
        self.mainLayout.setRowStretch(2,100)

    def connectUi(self, Widget):
        self.preset_zero.clicked.connect(Widget.preset_zero_click)
        self.preset_two.clicked.connect(Widget.preset_two_click)
        self.preset_one.clicked.connect(Widget.preset_one_click)
        self.preset_pointTwo.clicked.connect(Widget.preset_pointTwo_click)
        self.osc_enter.clicked.connect(Widget.osc_enter_click)
        self.osc_preset.clicked.connect(Widget.osc_preset_click)
        self.sens_enter.clicked.connect(Widget.sens_enter_click)
        self.sens_preset.clicked.connect(Widget.sens_preset_click)
        self.tconst_enter.clicked.connect(Widget.tconst_enter_click)
        self.tconst_preset.clicked.connect(Widget.tconst_preset_click)
        self.freq_enter.clicked.connect(Widget.freq_enter_click)
        self.freq_preset.clicked.connect(Widget.freq_preset_click)
        self.phi_enter.clicked.connect(Widget.phi_enter_click)
        self.phi_preset.clicked.connect(Widget.phi_preset_click)
        self.read_all.clicked.connect(Widget.read_all_click)
        self.adv_4KHz.clicked.connect(Widget.adv_4KHz_click)
        self.adv_1KHz.clicked.connect(Widget.adv_1KHz_click)
        self.adv_autoPhase.clicked.connect(Widget.adv_autoPhase_click)
        # self..clicked.connect(Widget.)


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #connect to ITC
        self.app = AppServer("lockin")
        self.inst_SR860 = self.app.addInstrument("inst_SR860")

        #time stamp base (using Labview standard, Easter time)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.connectUi(self)

        self.settingTimer = QTimer()
        self.settingTimer.setInterval(5000)
        self.settingTimer.timeout.connect(self.update)
        self.settingTimer.start()

        self.update()

    def closeEvent(self, event):
        del self.app
        super().closeEvent(event)

    @Slot()
    def preset_zero_click(self):
        self.inst_SR860.query('osc(0)')
        self.inst_SR860.query('sens("1V")')
        self.update()

    @Slot()
    def preset_two_click(self):
        self.inst_SR860.query('osc(2)')
        self.inst_SR860.query('sens("1V")')
        self.update()
        
    @Slot()
    def preset_one_click(self):
        self.inst_SR860.query('osc(0.1)')
        self.inst_SR860.query('sens("1V")')
        self.update()

    @Slot()
    def preset_pointTwo_click(self):
        self.inst_SR860.query('osc(0.02)')
        self.inst_SR860.query('sens("20mV")')
        self.update()

    @Slot()
    def osc_enter_click(self):
        osc = float(self.ui.osc_input.text())
        if osc>2: return
        self.inst_SR860.query('osc('+str(osc)+')')
        self.update()

    @Slot()
    def osc_preset_click(self):
        self.inst_SR860.query('osc(0.02)')
        self.update()
        
    @Slot()
    def sens_enter_click(self):
        sens = self.ui.sen_dic[self.ui.sens_input.currentIndex()]
        self.inst_SR860.query("sens('"+sens+"')")
        self.update()

    @Slot()
    def sens_preset_click(self):
        self.inst_SR860.query("sens('20mV')")
        self.update()
        
    @Slot()
    def tconst_enter_click(self):
        tconst = self.ui.tconst_dic[self.ui.tconst_input.currentIndex()]
        self.inst_SR860.query("tconst('"+tconst+"')")
        self.update()

    @Slot()
    def tconst_preset_click(self):
        self.inst_SR860.query("tconst('1ms')")
        self.update()
        
    @Slot()
    def freq_enter_click(self):
        freq = float(self.ui.freq_input.text())
        self.inst_SR860.query('freq('+str(freq)+')')
        self.update()

    @Slot()
    def freq_preset_click(self):
        self.inst_SR860.query('freq(4000)')
        self.update()
        
    @Slot()
    def phi_enter_click(self):
        phi = float(self.ui.phi_input.text())
        self.inst_SR860.query('phi('+str(phi)+')')
        self.update()

    @Slot()
    def phi_preset_click(self):  
        self.inst_SR860.query('phi(-62)')
        self.update()
        
    @Slot()
    def read_all_click(self):
        self.update()   

    @Slot()
    def adv_4KHz_click(self):
        pass
        
    @Slot()
    def adv_1KHz_click(self):
        pass

    @Slot()
    def adv_autoPhase_click(self):
        self.inst_SR860.query('autoPhase()')
        self.update()

    def update(self):
        osc = float(self.inst_SR860.query("osc_q()"))
        sens = self.inst_SR860.query("sens_q()")
        tconst = self.inst_SR860.query("tconst_q()")
        freq = float(self.inst_SR860.query("freq_q()"))
        phi = float(self.inst_SR860.query("phi_q()"))
        self.ui.osc_display.setText("{0:.2f}".format(osc))
        self.ui.sens_display.setText(sens)
        self.ui.tconst_display.setText(tconst)
        self.ui.freq_display.setText("{0:.2f}".format(freq))
        self.ui.phi_display.setText("{0:.2f}".format(phi))



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




# if __name__ == "__main__":
app = QApplication(sys.argv)
app.setStyle("Fusion")
app.setStyleSheet('QLabel{font-size: 14pt;}\
                  QLabel{font: bold "Arial";}\
                  QLabel{border-color: red;}\
                  QLineEdit{font-size: 16pt;}\
                  QComboBox{font: 12pt;}\
                  QPushButton{font-size: 12pt;}')
# app.setStyleSheet("QPushButton{font-size: 12pt;}")
app.setPalette( get_darkModePalette( app ) )
widget = Widget()
widget.show()

sys.exit(app.exec())


