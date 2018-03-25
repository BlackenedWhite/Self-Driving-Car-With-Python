import numpy as np
from keras.models import load_model
import cv2
from screenGrap import *
from drive import *
from getKeys import *
from scipy.stats import itemfreq


model = load_model("new_model_2.2.h5")
# w = model.get_weights()
play = True
Paused = False

file_name = 'newData/collected_data-50.npy'
data = np.load(file_name)
x = list(data[0][0])
y = list(data[0][1])
x = np.array(x, dtype="float") / 255.0
#arr = np.array([x])
result = model.predict(x)
model.summary()


plapla = []
for i in range(len(y)):
   plapla.append(np.argmax(y[i]))
print(itemfreq(plapla))


plapla = []
for i in range(len(result)):
   plapla.append(np.argmax(result[i]))
print(itemfreq(plapla))


## ...PLAYING... 

# for i in range(5):
#    print(i)
#    time.sleep(1)
#
# while play:
#    if not Paused:
#        img = grab_screen(800, 600)
#        img = cv2.resize(img, (100, 100))
#        arr = np.array([img])
#        result = model.predict(arr)
#        result = np.argmax(result)
#        print(result)
#        if result == 0:
#            forward()
#        elif result == 1:
#            left()
#        elif result == 3:
#            right()
#        else:
#            print("NO MOOOOOVE..................")
#
#    keys = getKeys()
#
#    if 'T' in keys:
#        if Paused:
#            print("Rusemed")
#            Paused = False
#            time.sleep(1)
#        else:
#            release_all()
#            print("Paused")
#            Paused = True
#            time.sleep(1)
#
#    if 'Q' in keys:
#        release_all()
#        print("...END...")
#        play = False
