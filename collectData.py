from getKeys import *
from screenGrap import *
import numpy as np
import time
from extras import *


W = [1, 0, 0, 0, 0]
A = [0, 1, 0, 0, 0]
S = [0, 0, 1, 0, 0]
D = [0, 0, 0, 1, 0]
NOMOVE = [0, 0, 0, 0, 1]


WIDTH = 800
HEIGHT = 600






def tansform(out):

    if "W" in out:
        out = W
    elif "A" in out:
        out = A
    elif "S" in out:
        out = S
    elif "D" in out:
        out = D
    else:
        out = NOMOVE
    return out

def main():
    collected_data = []
    file_name = "collectedData/training_data-{1}"
    partNumber =1
    Paused = False
    countDown(5)
    while (True):
        if not Paused:
            t = time.time()
            output = getKeys()
            screen = grab_screen(WIDTH, HEIGHT)
            output = tansform(output)
            arr = [screen, output]
            collected_data.append(arr)
            if len(collected_data) % 100 == 0:
                print(len(collected_data))
            if len(collected_data) == 100:
                np.save(file_name, collected_data)
                print('SAVED')
                collected_data = []
                partNumber += 1
                file_name = 'collectedData/trainingData-{}.npy'.format(partNumber)
            print(time.time() - t)
    currentKeys = key_check()
    Pause(Paused)
main()
