from multiprocessing.connection import Listener,Client
import subprocess

class System():
    version = "1.0"
    status = True
    n_port_inst_app = 100
    n_port_InstServer = 50

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
    
    #Instrument booting
    address_boot = '127.0.0.1'
    port_boot = 5724
    authkey_boot = b'vf@pnml2138'

    #Instrument status
    Inst_status = dict()  #instrument status (key: instrument value: last respond time)

    #Instrument <-> App
    address_inst_app = '127.0.0.1'
    port_inst_app_available = list(range(8000,8000+n_port_InstServer))
    port_inst_app = dict()  #store key: port, value: app_name+serial-instrumen_name
    authkey_inst_app = b'vf@pnml9876'



    def __init__(self):
        pass

    def kill_InstServ(self,name):
        self.queue_InstServer[name].put(("kill",0))
        print("goaway")
        port = self.port_InstServer[name]
        del self.port_InstServer[name]
        self.port_InstServer_available.append(port)


class Shell():
    def __init__(self,jobs,sys):
        self.jobs = jobs
        self.sys = sys
        print(sys.version)
        

    def run(self):
        while self.sys.status:
            data = str(input())
            self.jobs.put(data)
            if data in ['exit',"quit","stop","exit()" ]: break


class AppServer():
    def __init__(self,sys):
        self.sys = sys

    def server(self):
        port_AppServer = Listener((self.sys.address_AppServer,self.sys.port_AppServer) , 
                                  authkey= self.sys.authkey_AppServer)
        port_AppServer._listener._socket.settimeout(1)

        while self.sys.status:
            try: 
                client = port_AppServer.accept()
                while self.sys.status:
                    try:
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
                            result = ( (self.sys.address_inst_app , port) 
                                        , self.sys.authkey_inst_app)

                        elif pieces[1] == "close_app":  #coming from application's destructor
                            #release port
                            ports,insts = self.searchport([pieces[2] , pieces[3]])
                            self.sys.port_inst_app_available += ports
                            #tell the instrumentServer
                            for i in range(len(ports)):
                                message = ("close",ports[i])
                                self.sys.queue_InstServer[insts[i]].put(message)
                                print("release ports:",ports[i],"from instrument: ", insts[i])

                            #let application know the address , port number, authkey
                            result = "bye"
                        client.send(result)
                    except EOFError:
                        client = port_AppServer.accept()
            except:
                pass


        while self.sys.status:
            try:
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
                    self.sys.port_inst_app_available += ports
                    #tell the instrumentServer
                    for i in range(len(ports)):
                        message = ("close",ports[i])
                        self.sys.queue_InstServer[insts[i]].put(message)
                        print("release ports:",ports[i],"from instrument: ", insts[i])

                    #let application know the address , port number, authkey
                    client.send("bye")

            except EOFError:
                client = port_AppServer.accept()

    def searchport(self,name):
        ports = []
        insts = []
        for port in self.sys.port_inst_app:
            appName = self.sys.port_inst_app[port]
            pieces = appName.split('-')
            app_name,serialN = (pieces[0] , pieces[1])
            if name[0] == app_name and name[1] == serialN:
                ports.append(port)
                insts.append(pieces[2])
        for port in ports:
            del self.sys.port_inst_app[port]

        return (ports,insts)


    def createPort(self,name):
        port = self.sys.port_inst_app_available.pop()
        self.sys.port_inst_app[port] = name
        return port

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
        # self.port.send(("kill",0))
        # print("goaway4")
        self.port.close()

    def server(self):
        while self.sys.status:
            request = self.sys.queue_InstServer[self.name].get()
            # print("goaway2")
            # if request == ("kill",0): break
            self.port.send(request)
            self.port.recv()
            # print("goaway3")
            if request == ("kill",0): break
        print("InstrumentServer: ",self.name, " off")

class BootInstrument():
    def __init__(self,sys,name):
        self.sys = sys
        self.name = name

    def boot(self):
        boot = Listener((self.sys.address_boot,self.sys.port_boot),
                 authkey= self.sys.authkey_boot)
        subprocess.call('start Instrument.py', shell=True)
        client = boot.accept()
        #send instrument class
        client.send(self.name)
        #receive the address
        msg = "address_InstServer = '" + str(self.sys.address_InstServer) + "'"
        client.send(msg)
        #receive the port number
        msg = "port_InstServer = "+ str(self.sys.port_InstServer[self.name])
        client.send(msg)
        #receive the authkey
        msg = "authkey_InstServer = " + str(self.sys.authkey_InstServer)
        client.send(msg)
        boot.close()