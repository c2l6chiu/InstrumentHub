import subprocess
import os

cmd = "start conda run --no-capture-output -n amoebas python test.py"
# cmd = "start test.py"

proc = subprocess.Popen(cmd, shell=True ,cwd=os.getcwd()+"/testing")
# import time
# time.sleep(2)
# proc.terminate()

