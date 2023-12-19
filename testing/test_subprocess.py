import subprocess
import os

cmd = "start conda activate amoebas && test.py"
# cmd = "test.py"

subprocess.Popen(cmd, shell=True ,cwd=os.getcwd()+"/testing")

