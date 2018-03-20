from getKeys import *
from screengrap import *
import numpy as np
import time

W = [1, 0, 0, 0, 0]
A = [0, 1, 0, 0, 0]
S = [0, 0, 1, 0, 0]
D = [0, 0, 0, 1, 0]
NOMOVE = [0, 0, 0, 0, 1]


WIDTH = 800
HEIGHT = 600

collected_data = []
file_name = "collected_data.npy"


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

    for i in range(100):
        t = time.time()
        output = getKeys()
        screen = grab_screen(WIDTH, HEIGHT)
        output = tansform(output)
        arr = [screen, output]
        collected_data.append(arr)
        if len(collected_data) % 100 == 0:
            print(len(collected_data))
            np.save(file_name, collected_data)
            print('SAVED')
        print(time.time() - t)
#    exit()

    # print(arr)

for i in range(5):
    print(i)
    time.sleep(1)
    
main()
