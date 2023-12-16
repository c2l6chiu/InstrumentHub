Tcontroll  finish another ITC connection


Pre launch temperature recorder


Finish Ardrino /  RS232 / Keithley



Application crash:
    did the destructor being called correctely?
    if the communication stuck, how to close the connection?


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
    2. application disappear
    3. application froze
    4. need to be able to force delete the application if it got stuck



ext install seanwu.vscode-qt-for-python