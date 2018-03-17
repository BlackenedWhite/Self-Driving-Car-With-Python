from getKeys import *
from screenGrap import *
import numpy as np
import time
from extras import *
import cv2
import os

W = [1, 0, 0, 0, 0]
A = [0, 1, 0, 0, 0]
S = [0, 0, 1, 0, 0]
D = [0, 0, 0, 1, 0]
NOMOVE = [0, 0, 0, 0, 1]

output = [0, 0, 0, 0, 0]


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
    partNumber = 1
    collect = True
    Paused = False

    while(True):
        file_name = "collectedData/collected_data-{}.npy".format(partNumber)
        if (os.path.isfile(file_name)):
            partNumber += 1
        else:
            print("file don't exist, new partNumber: ", partNumber)
            break

    countDown(5)

    while (collect):
        if not Paused:
            t = time.time()
            output = getKeys()
            screen = grab_screen(WIDTH, HEIGHT)
            screen = cv2.resize(screen, (WIDTH // 4, HEIGHT // 4))
            output = tansform(output)
            arr = [screen, output]
            collected_data.append(arr)
            if len(collected_data) % 100 == 0:
                print(len(collected_data))
            if len(collected_data) == 200:
                print('Saving data......')
                np.save(file_name, collected_data)
                collected_data = []
                partNumber += 1
                file_name = 'collectedData/collected_data-{}.npy'.format(
                    partNumber)
            print(time.time() - t)

        output = getKeys()

        if 'T' in output:
            if Paused:
                print("Rusemed")
                Paused = False
                time.sleep(1)
            else:
                print("Paused")
                Paused = True
                time.sleep(1)

        if 'Q' in output:
            print("...END COLLECTING DATA...")
            collect = False


main()
