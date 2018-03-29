from getKeys import *
from screenGrap import *
import numpy as np
import time
from extras import *
import cv2
import os

W = [1, 0, 0]
A = [0, 1, 0]
D = [0, 0, 1]
NM = [0, 0, 0]
# S = [0, 0, 1, 0]

output = [0, 0, 0]


WIDTH = 800
HEIGHT = 600


def tansform(out):

    if "D" in out:
        out = D
    elif "A" in out:
        out = A
    # elif "S" in out:
    #     out = S
    # elif "W" in out:
    #     out = W
    else:
        out = W
    return out


def main():
    images = []
    outputs = []
    collected_data = []
    partNumber = 1
    collect = True
    Paused = False

    while(True):
        file_name = "newData/collected_data-{}.npy".format(partNumber)
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
            screen = cv2.resize(screen, (100, 100))
            output = tansform(output)
            images.append(screen)
            outputs.append(output)
#            arr = [screen, output]
#            collected_data.append(arr)
            if len(images) % 100 == 0:
                print(len(images))
            if len(images) == 200:
                collected_data.append([images, outputs])
                print('\tSaving file number {}'.format(partNumber))
                np.save(file_name, collected_data)
                collected_data = []
                images = []
                outputs = []
                partNumber += 1
                file_name = 'newData/collected_data-{}.npy'.format(
                    partNumber)
            # print(time.time() - t)

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
