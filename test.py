import numpy as np
import cv2

x = np.load('collectedData/training_data-1.npy')


img = x [5][0]
output = x[5][1]


print(output)
cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
