import numpy as np
import cv2

x = np.load('collectedData/trainingData-2.npy')
for i in range(20):
    img = x[i+20][0]
    output = x[i+20][1]
    print(output)
    cv2.imshow('window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
