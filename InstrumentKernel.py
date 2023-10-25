from threading import Thread
from multiprocessing.connection import Listener,Client
import socket
from queue import Queue

time_out = 1

class ServiceLine():
    def __init__(self,address,authkey_serviceLine,que_command,que_respond):
        self.address = address
        self.port = address[1]
        self.authkey_serviceLine = authkey_serviceLine
        self.que_command = que_command
        self.que_respond = que_respond
        self.status = True
    
    def __del__(self):
        # self.port_inst_app.close()
        pass
    
    def run(self):
        self.port_inst_app = Listener(self.address , authkey= self.authkey_serviceLine)
        self.port_inst_app._listener._socket.settimeout(time_out)
        
        while self.status:
            try:
                client = self.port_inst_app.accept()
                while self.status:
                    try:
                        msg = client.recv()
                        self.que_command.put((self.port,msg))
                        client.send(self.que_respond.get())
                    except EOFError:
                        client = self.port_inst_app.accept()
            except: #TimeoutError
                pass

class InstrumentController():
    def __init__(self,the_instrument,qc,qr) -> None:
        self.inst = the_instrument
        self.queue_commend = qc
        self.queue_respond = qr

    def run(self):
        while True:
            port ,commend = self.queue_commend.get()
            if port == -1 and commend == "stop": break
            try:
                self.queue_respond[port].put(eval("self.inst."+commend))    #exec()
            except Exception as eer:
                self.queue_respond[port].put("error!@#")
                print(eer)
                print("error commend: "+commend)


class InstrumentServer():
    def __init__(self,queue):
        self.queue = queue
        self.status = True
        pass

    def server(self,address,authkey_InstServer):
        port_InstServer = Listener(address , authkey= authkey_InstServer)
        port_InstServer._listener._socket.settimeout(time_out)

        while self.status:
            try:
                client = port_InstServer.accept()
                while self.status:
                    try:
                        msg = client.recv()
                        self.queue.put(msg)
                        # print("Instrument server receive: ",msg)
                        #message ex: open-1242
                        client.send(msg)
                    except EOFError:
                        client = port_InstServer.accept()
            except: #TimeoutError
                pass
