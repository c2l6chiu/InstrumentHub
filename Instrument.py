from threading import Thread
from multiprocessing.connection import Listener,Client
from queue import Queue
from InstrumentKernel import InstrumentServer, InstrumentController, ServiceLine
import os

#bootstraping the instrument
######################################
# from XXXX import Inst
# address_InstServer = '127.0.0.1'
# port_InstServer = 7788
# authkey_InstServer = b'vf@pnml5193'
address_boot = '127.0.0.1'
port_boot = 5724
authkey_boot = b'vf@pnml2138'
boot =  Client((address_boot,port_boot),authkey=authkey_boot)
#receive the instrument class
msg = boot.recv()
exec("from " + msg + " import Inst")
print(msg+'\n')
#receive the address
msg = boot.recv()
exec(msg)
print(msg)
#receive the port number
msg = boot.recv()
exec(msg)
print(msg)
#receive the authkey
msg = boot.recv()
print(msg)
exec(msg)
boot.close()
# ######################################

thread_pool = dict()
que_respond = dict()

queue_serviceLine = Queue()
que_command = Queue()

#run the instrument server
instServer = InstrumentServer(queue_serviceLine)
t_instServer = Thread(target=instServer.server, args=((address_InstServer,port_InstServer),
                       authkey_InstServer))
t_instServer.start()


#run the instrument controller
instrument = Inst()
controller = InstrumentController(instrument,que_command,que_respond)
t_controller = Thread(target=controller.run, args=())
t_controller.start()

#maintaining the serviceLine
while True:
    commend , arg = queue_serviceLine.get()

    if commend == "open":
        address_port , authkey = arg
        port = address_port[1]
        que_respond[port] = Queue()
        ser = ServiceLine(address_port,authkey,
                          que_command,que_respond[port])
    #create a thread with port# pieces[1]
        thread = Thread(target=ser.run(), args=(port))
    #save this thread in thread_pool (key = port value = thread)
        thread_pool[port] = thread
    #run the thread
        thread.start()

    elif commend == "close":
        port = arg
        thread = thread_pool[port]
        thread.terminate()
        del thread_pool[port]
        del que_respond[port]


    elif commend == "kill":
        print("kill this instrument")
        eval("a='")
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



