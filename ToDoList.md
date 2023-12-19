Subprocess:
    * monitor the child is alive?
    * kill the child


Finish Ardrino / Keithley



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



############ launch via batch ##########
@echo OFF
rem How to run a Python script in a given conda environment from a batch file.

rem It doesn't require:
rem - conda to be in the PATH
rem - cmd.exe to be initialized with conda init

rem Define here the path to your conda installation
set CONDAPATH=C:\ProgramData\Miniconda3
rem Define here the name of the environment
set ENVNAME=someenv

rem The following command activates the base environment.
rem call C:\ProgramData\Miniconda3\Scripts\activate.bat C:\ProgramData\Miniconda3
if %ENVNAME%==base (set ENVPATH=%CONDAPATH%) else (set ENVPATH=%CONDAPATH%\envs\%ENVNAME%)

rem Activate the conda environment
rem Using call is required here, see: https://stackoverflow.com/questions/24678144/conda-environments-and-bat-files
call %CONDAPATH%\Scripts\activate.bat %ENVPATH%

rem Run a python script in that environment
python script.py

rem Deactivate the environment
call conda deactivate

rem If conda is directly available from the command line then the following code works.
rem call activate someenv
rem python script.py
rem conda deactivate

rem One could also use the conda run command
rem conda run -n someenv python script.py