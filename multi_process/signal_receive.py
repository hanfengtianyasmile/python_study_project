import os,signal
from time import sleep

os.kill(13987,signal.SIGTERM)
os.kill(13987,signal.SIGUSR1)

