from multiprocessing.connection import Client
import random

# import atexit
    
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
        address_serviceLine = self.askPort(name)
        #no such instrument?
        if address_serviceLine == ('!!!','!!!'):
            raise Exception("no such instrument: "+name)
        
        coordinator = Coordinator(address_serviceLine)
        self.stack_coordinator.append(coordinator)
        return coordinator

    def askPort(self,inst_name):
        message = "app_request-new_app"
        message += '-'+self.app_name+'-'+self.serial_number
        message += '-'+inst_name
        result = self.ask(message).split('-')
        return (result[0],int(result[1]))
        # return ((result[0],int(result[1])),result[2])     if you want to do authentication
    
    def ask(self,message):
        '''
        low level communication, return string
        '''
        port_app_kern =  Client((self.address_AppServer,self.port_AppServer))
        port_app_kern.send_bytes(message.encode())
        info = str(port_app_kern.recv_bytes() , 'utf-8')
        port_app_kern.close()
        return info
    
    def shutdown(self):
        for coor in self.stack_coordinator:
            coor.shutdown()

    # @atexit.register
    # def goodbye():
    #     print('You are now leaving the Python sector.')





class Coordinator():
    def __init__(self,link_address):
        self.port_app_inst= Client(link_address)
    
    def shutdown(self):
        self.port_app_inst.close()

    def query_old(self,question):
        '''
        old style: query_old(func('arg1','arg2'))
        '''
        #working on the timeout issue
        self.port_app_inst.send_bytes(question.encode())
        answer = str(self.port_app_inst.recv_bytes(),'utf-8')
        typ , result = (answer[0] , answer[1:])

        if typ == 's': result = result
        elif typ == 'i': result = int(result)
        elif typ == 'f': result = float(result)
        else: result = result

        if result == "error!@#":
            print("*******************")
            print("error commend: "+ question)
            print("*******************")
            raise
        return result
    
    def query(self,func,*arg):      #argument can be string,int,float
        '''
        new style: query(func,arg1,arg2)
        but also take old style query
        '''
        if len(arg) == 0 and func[-1] == ')': question = func
        else: question = func + '(' + ','.join(["'"+str(iarg)+"'" for iarg in arg]) + ')'

        self.port_app_inst.send_bytes(question.encode())
        answer = str(self.port_app_inst.recv_bytes(),'utf-8')
        typ , result = (answer[0] , answer[1:])

        if typ == 's': result = result
        elif typ == 'i': result = int(result)
        elif typ == 'f': result = float(result)
        else: result = result

        if typ == 's' and "error!@#" in result:
            print("*******************")
            print("error commend: "+ question)
            print(result)
            print("*******************")
            raise
        return result        
    
    # def set(self,question):
    #     pass

    # def ask(self,question):
    #     pass
        
    # def get(self,question):
    #     pass
    

