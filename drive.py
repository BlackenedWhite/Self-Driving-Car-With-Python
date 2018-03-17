from directKeys import PressKey, ReleaseKey, W, D, A, S
import time



deviationSpeed = 0.06

def forward():
     PressKey(W)
     ReleaseKey(A)
     ReleaseKey(D)   
     
def left():
     PressKey(W)
     PressKey(A)
     ReleaseKey(D)   
     time.sleep(deviationSpeed)
     ReleaseKey(A)

def right():
     PressKey(W)
     PressKey(D)
     ReleaseKey(A)
     time.sleep(deviationSpeed)
     ReleaseKey(D)     

