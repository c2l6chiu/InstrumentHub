from multiprocessing.connection import Listener,Client

class System():
    version = "1.0"
    status = True
    n_port_inst_app = 50
    n_port_InstServer = 20

    #AppServer
    address_AppServer = '127.0.0.1'
    port_AppServer = 5723
    authkey_AppServer = b'vf@pnml1234'

    #InstrumentServer
    address_InstServer = '127.0.0.1'
    port_InstServer_available = list(range(9000,9000+n_port_InstServer))
    port_InstServer = dict() #store key: instrument, value: port
    authkey_InstServer = b'vf@pnml5193'
    queue_InstServer = dict() #for app server to talk to (key: instrument value: Queue)
    InstServer_thread_pool = dict() #coordinator thread (key: instrument value: thread)
    
    
    #Instrument
    Inst_status = dict()  #instrument status (key: instrument value: last respond time)

    #instrument <-> App
    address_inst_app = '127.0.0.1'
    port_Inst_app_available = list(range(8000,89000+n_port_InstServer))
    port_inst_app = dict()  #store key: app_name+serial-instrumen_name, value: port
    authkey_inst_app = b'vf@pnml9876'



    def __init__(self):
        pass

    # def generate_port(self):
    #     for i in range(0,self.n_port_inst_app):
    #         self.port_inst_app[self.port_inst_app_base+i] = ['empty']
    #     for i in range(0,self.n_port_InstServer):
    #         self.port_InstServer[self.port_InstServer+i] = ['empty']

class Shell():
    def __init__(self,jobs,sys):
        self.jobs = jobs
        self.sys = sys
        print(sys.version)
        

    def run(self):
        while self.sys.status:
            data = str(input())
            self.jobs.put(data)
            #commend:
            #check port dict
            #


class AppServer():
    def __init__(self,sys):
        self.sys = sys

    def server(self):
        port_AppServer = Listener((self.sys.address_AppServer,self.sys.port_AppServer) , 
                                  authkey= self.sys.authkey_AppServer)

        while self.sys.status:
            try:
                client = port_AppServer.accept()
                msg = client.recv() #msg in app_request-new_app-app_name-serial(0~10,000)-instrumen_name
                pieces = msg.split('-')
                
                if pieces[0] != "app_request": self.errorRequest(msg)

                if pieces[1] == "new_app":
                    #check if the instrument exist
                    if not self.checkInstrument(pieces[4]): self.errorRequest('no such instrument')
                    #prepare a port for application
                    port = self.createPort(pieces[2]+'-'+pieces[3]+'-'+pieces[4])   #app_name - serial

                    #request instrumentServer to coordinate instrument
                    commend = "open"
                    arg = ( ( self.sys.address_inst_app, port) , self.sys.authkey_inst_app)
                    self.sys.queue_InstServer[pieces[4]].put((commend,arg))

                    #let application know the address , port number, authkey
                    client.send(( (self.sys.address_inst_app , port) 
                                 , self.sys.authkey_inst_app))

                elif pieces[1] == "close_app":  #coming from application's destructor
                    #release port
                    ports,insts = self.searchport([pieces[2] , pieces[3]])
                    port_Inst_app_available += ports
                    print("release ports:")
                    print(ports)
                    #tell the instrumentServer
                    for i in range(len(ports)):
                        message = ("close",port[i])
                        self.sys.queue_InstServer[insts[i]].put(message)
                        print("release ports:",ports[i],"from instrument: ", insts[i])

            except EOFError:
                client = port_AppServer.accept()

    def searchport(self,name):
        ports = []
        insts = []
        for port in self.port_inst_app:
            value = self.port_inst_app[port]
            pieces = value.split('-')
            app_name,serialN = (pieces[0] , pieces[1])
            if name[0] == app_name and name[1] == serialN:
                ports.append(port)
                insts.append(pieces[2])
                del self.port_inst_app[port]

        return (ports,insts)


    def createPort(self,name):
        if name in self.port_inst_app:
            print("application attemp to connect to same instrument")
            raise
        self.port_inst_app[name] = self.port_Inst_app_available.pop()
        return self.port_inst_app[name]

    def checkInstrument(self,name):
        #maybe check if the instrument alive
        if name in self.sys.Inst_status: return True
        else: return False

    def errorRequest(self,msg):
        print("AppServer receive error request:")
        print(msg)



class InstrumentMom():
    def __init__(self,sys):
        self.sys = sys    

    def server(self):
        pass

class InstrumentServer():
    def __init__(self,sys,name):
        self.sys = sys
        self.name = name
        self.port = Client((self.sys.address_InstServer,self.sys.port_InstServer[name]),
                                    authkey=self.sys.authkey_InstServer)
        
    def __del__(self):
        self.port.close()

    def server(self):
        while self.sys.status:
            request = self.sys.queue_InstServer[self.name].get()
            self.port.send(request)
            self.port.recv()



