import time

def on_exit(sig, func=None):
    print("exit handler")
    time.sleep(10)  # so you can see the message before program exits

import signal

signal.signal(signal.SIGTERM, on_exit)
time.sleep(10)