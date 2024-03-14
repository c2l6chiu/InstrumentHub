deal with:
    if I remove inst_nanonis
    then if I inst inst_nanonis
    it won't open it


deal with:
    if I restart the inst
    the application will freeze

cntrl-C process:
two type of applicatoin: integrated cosole or hidden console

Integrate matlab to here?
Finish Ardrino / Keithley

Subprocess for instrument and application:
    * monitor the child is alive?
    * kill the child


Application crash:
    application will do destructor only when application shut down on its own. If the communication stuck, how to close the connection?


in application.AppServer.askPort
    handle timeout

in application.Coordinator.ask:
    clear buffer



Instrument:
    *need to be able to deal with failed launch instrument
    *need to deal with the proper way to shut down =>tell the Kernel that instrument is gone before dying
    *Need to be able to force kill the instrument server
    


In kernel AppServer.checkInstrument
    check if instrument is still alive by handshaking


In Kernel deal with bad application connection
    1. attemp to connect to same instrument twice
    3. application froze


Making the CMD console easier to use