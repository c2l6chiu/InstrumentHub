in application.AppServer
    make sure that I don't need to close the connection to allow other connection

reduce recv() to avoid dead end


deal with corrupted application
    try to recover the corrupted instrument


in application.AppServer.askPort
    handle timeout

in application.Coordinator.ask:
    clear buffer

in application.Coordinator.query:
    handle time out error





Instrumentation:
    need to deal with the proper way to shut down
    =>tell the Kernel that instrument is gone before dying


In kernel AppServer.checkInstrument
    check if instrument is still alive by handshaking

In Kernel deal with bad application connection
    1. attemp to connect to same instrument twice
    2. application disappear
    3. application froze