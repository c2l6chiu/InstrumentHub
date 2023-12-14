from multiprocessing.connection import Client
import random
    
class AppServer():
    address_AppServer = '127.0.0.1'
    port_AppServer = 55723
    authkey_AppServer = b'vf@pnml1234'
    app_name = 'default'
    serial_number = str(random.randrange(1,10000))
    stack_coordinator=[]

    def __init__(self,name):
        self.app_name = name

    def __del__(self):
        self.shutdown()
        message = "app_request-close_app"
        message += '-'+self.app_name+'-'+self.serial_number
        self.ask(message)
        
    def addInstrument(self,name):
        address_serviceLine,authkey_serviceLine = self.askPort(name)
        coordinator = Coordinator(address_serviceLine,authkey_serviceLine)
        self.stack_coordinator.append(coordinator)
        return coordinator

    def askPort(self,inst_name):
        message = "app_request-new_app"
        message += '-'+self.app_name+'-'+self.serial_number
        message += '-'+inst_name
        return self.ask(message)
    
    def ask(self,message):
        port_app_kern =  Client((self.address_AppServer,self.port_AppServer),
                                authkey=self.authkey_AppServer)
        port_app_kern.send(message)
        info = port_app_kern.recv()
        port_app_kern.close()
        return info
    
    def shutdown(self):
        for coor in self.stack_coordinator:
            coor.shutdown()





class Coordinator():
    def __init__(self,link_address,authkey):
        self.port_app_inst= Client(link_address, authkey=authkey)
    
    def shutdown(self):
        self.port_app_inst.close()

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
        if answer == "error!@#":
            print("*******************")
            print("error commend: "+ question)
            print("*******************")
            raise
        return answer
    

