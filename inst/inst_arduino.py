import serial
import time

class Inst():
    def __init__(self):
        self.ser=serial.Serial(port='COM10',baudrate=9600)
        self.ser.readline()

    def SendCom_Arduino(self,command):

        # ser=serial.Serial(port='COM3',baudrate=9600)
        if(self.ser.isOpen()):
            print('send command to Arduino : '+command)
            command=command+"\r\n"
            self.ser.write(command.encode())
            print(self.ser.readline())
            return True
        else:
            print('Fail to send a commend! Check communication lines')
            return False

    def Aux_on(self): self.SendCom_Arduino('AUX_ON')
    def Aux_off(self): self.SendCom_Arduino('AUX_OFF')


