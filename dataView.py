import numpy as np
import cv2
from scipy.stats import itemfreq
#collected_data = np.load('collectedData/collected_data-1_balanced.npy')
collected_data = np.load('newData/collected_data-23.npy')
data = collected_data[0]

X = list(data[0])
y = list(data[1])
#
plapla = []

for i in range(len(y)):
    plapla.append(np.argmax(y[i]))
print(itemfreq(plapla))
#for i in range(20):
#    img = X[i+20]
#    output = y[i+20]
#    print(output)
#    cv2.imshow('window', img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
