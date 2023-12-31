from threading import Thread
from multiprocessing.connection import Listener,Client
from queue import Queue
from InstrumentKernel import InstrumentServer, InstrumentController, ServiceLine
import time

#bootstraping the instrument
######################################
# from XXXX import Inst
# address_InstServer = '127.0.0.1'
# port_InstServer = 7788
# authkey_InstServer = b'vf@pnml5193'
address_boot = '127.0.0.1'
port_boot = 55724
authkey_boot = b'vf@pnml2138'
boot =  Client((address_boot,port_boot),authkey=authkey_boot)
#receive the instrument class
msg_inst = boot.recv()
#receive the address
msg_add = boot.recv()
#receive the port number
msg_port = boot.recv()
#receive the authkey
msg_auth = boot.recv()

exec("from " + msg_inst + " import Inst")
print(msg_inst+'\n')
exec(msg_add)
print(msg_add)
exec(msg_port)
print(msg_port)
exec(msg_auth)
print(msg_auth)
#load instrument
try:
    instrument = Inst()
    boot.send("success")
    boot.close()
except Exception as eer:
    boot.send("failed")
    print(eer)
    boot.close()
    exec("exit()")
#######################################

#for Service lines 
ser_pool = dict()
que_respond = dict()
que_command = Queue()

#run the instrument server
queue_InstServer = Queue()
instServer = InstrumentServer(queue_InstServer)
t_instServer = Thread(target=instServer.server, args=((address_InstServer,port_InstServer),
                    authkey_InstServer))
t_instServer.start()

#run the instrument controller
controller = InstrumentController(instrument,que_command,que_respond)
t_controller = Thread(target=controller.run, args=())
t_controller.start()


#maintaining the serviceLine
while True:
    commend , arg = queue_InstServer.get()

    if commend == "open":
        address_port , authkey = arg
        port = address_port[1]
        que_respond[port] = Queue()
        ser = ServiceLine(address_port,authkey,
                          que_command,que_respond[port])
    #create a thread with port# pieces[1]
        thread = Thread(target=ser.run, args=())
    #save this thread in thread_pool (key = port value = thread)
        ser_pool[port] = ser
    #run the thread
        thread.start()

    elif commend == "close":
        port = arg
        ser_pool[port].status = False
        # ser = ser_pool[port]
        # del ser
        # ser_pool[port].shutdown()
        del ser_pool[port]
        del que_respond[port]


    elif commend == "kill":
        print("shut down this instrument")
        #shutdown Insturment Controller
        que_command.put((-1,"stop"))
        #Shutdown Instrument server
        instServer.status = False
        #shutdown off all the serviceline
        for port in ser_pool:
            ser_pool[port].status = False

        exec("exit()")
    #implement the shut down here
    #stop controller
    #stop all the serviceLine
    #stop coordinator
    #break the while loop

    elif commend == "test":
        print("roger that!")

    else:
        print("error message: ")
        print(commend,arg)
        raise  



