import time
from getKeys import *


def countDown(n):
    for i in range(n,0,-1):
        print(i)
        time.sleep(1)
def Pause(Paused):    
    if 'T' in keys:
        if Paused:
            Paused = False
            time.sleep(1)
        else:
            Paused = True
            ReleaseKey(A)
            ReleaseKey(W)
            ReleaseKey(D)
            time.sleep(1)
