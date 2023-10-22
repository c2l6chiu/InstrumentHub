
from threading import Thread
from multiprocessing.connection import Listener,Client
from queue import Queue

class ServiceLine():
    def __init__(self,address,authkey_serviceLine,que_command,que_respond):
        self.address = address
        self.port = address[1]
        self.authkey_serviceLine = authkey_serviceLine
        self.que_command = que_command
        self.que_respond = que_respond
    
    def __del__(self):
        self.port_inst_app.close()
    
    def run(self):
        self.port_inst_app = Listener(self.address , authkey= self.authkey_serviceLine)
        client = self.port_inst_app.accept()
        while True:
            try:
                msg = client.recv()
                self.que_command.put((self.port,msg))
                client.send(self.que_respond.get())
            except EOFError:
                client = self.port_inst_app.accept()


class InstrumentController():
    def __init__(self,the_instrument,qc,qr) -> None:
        self.inst = the_instrument
        self.queue_commend = qc
        self.queue_respond = qr

    def run(self):
        while True:
            port ,commend = self.queue_commend.get()
            self.queue_respond[port].put(eval("self.inst."+commend))



class InstrumentServer():
    def __init__(self,queue):
        self.queue = queue
        pass

    def server(self,address,authkey_InstServer):
        port_InstServer = Listener(address , authkey= authkey_InstServer)
        client = port_InstServer.accept()
        while True:
            try:
                msg = client.recv()
                # print("new connectoin"+str(address))
                self.queue.put(msg)
                #message ex: open-1242
                # answer = self.anylyze(msg)
                client.send(msg)
            except EOFError:
                client = port_InstServer.accept()
