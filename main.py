from drive import *
from extras import *

def main():
    Paused = False
    countDown(3)
    while True:
        if not Paused:

            forward()
            right()
            left()
            forward()
            right()
            left()    
            forward()
            right()
            left()
            forward()
            right()
            left()
            forward()
            right()
            left()
    Pause(Paused)
main()
