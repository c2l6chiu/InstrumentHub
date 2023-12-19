# InstrumentHub
A centralized system that manage multiple instruments and applications at the same time


class AppServer():
    address = '127.0.0.1'
    port = 5723

    app_request-new_app-app_name-serial(0~10,000)-instrumen_name

#### environment ####
so I use anoconda to manage package, make sure you add anaconda to your path (so that you can activate your conda environment in cmd.) You should set up a conda environment and update the env under Kernel-> System.env to yours (mine is amoebas)

The package I have:
    * numpy 1.26.2
    * pandas 2.1.4
    * pySerial 3.5
    * pyside6 (PySide6-Addons-6.6.1 PySide6-Essentials-6.6.1 pyside6-6.6.1 shiboken6-6.6.1)
    * matplotlib (contourpy-1.2.0 cycler-0.12.1 fonttools-4.47.0 kiwisolver-1.4.5 
    matplotlib-3.8.2 packaging-23.2 pillow-10.1.0 pyparsing-3.1.1)
    


