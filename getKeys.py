import keyboard as k
import time


keyList = []
for char in "WASDTQ":
    keyList.append(char)


def getKeys():
    keys = []
    try:
        for key in keyList:
            if(k.is_pressed(key)):
                keys.append(key)
        return keys
    except:
        return keys


def main():
    while True:
        k = getKeys()
        if k:
            print(k)
