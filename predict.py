import numpy as np
from keras.models import load_model
import cv2
from screenGrap import *
from drive import *
from getKeys import *


model = load_model("new_model.h5")

play = True

file_name = 'collectedData/collected_data-10.npy'
data = np.load(file_name)
x = list(data[0][0])
y = list(data[0][1])
x = np.array(x, dtype="float") / 255.0
#arr = np.array([x])
#result = model.predict(x)
model.summary()


#
#for i in range(5):
#	print(i)
#	time.sleep(1)
#while play:
#    img = grab_screen(800, 600)
#    img = cv2.resize(img, (100, 100))
#    arr = np.array([img])
#    result = model.predict(arr)
#    result = np.argmax(result)
#    print(result)
#    if result == 0:
#        forward()
#    elif result == 1:
#        left()
#    elif result == 3:
#        right()
#    else:
#        print("NO MOOOOOVE..................")
#    keys = getKeys()
#    if 'Q' in keys:
#            print("...END...")
#            play = False
#
#
#
