from multiprocessing.connection import Client


class AppServer():
    inst = dict()
    address = '127.0.0.1'
    port = 5723

    def __init__(self) -> None:

        self.port_app_kern= Client((self.address,self.port), authkey=b'vf@pnml1234')
        pass

    def __del__(self):
        pass
        
    def addInstrument(self,name):
        address,authkey = self.askPort(name)
        coordinator = Coordinator(address,authkey)
        return coordinator

    def askPort(self,name):
        






class Coordinator():
    def __init__(self,link_address,authkey):
        # self.address , self.port = link_address
        self.port_app_inst= Client(link_address, authkey=authkey)

    def set(self,question):
        pass

    def ask(self,question):
        pass
        
    def get(self,question):
        pass

    def query(self,question):
        #working on the timeout issue
        self.port_app_inst.send(question)
        answer = self.port_app_inst.recv()
        return answer
    

