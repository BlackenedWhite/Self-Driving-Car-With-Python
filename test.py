import numpy as np
import cv2

x = np.load('newData/collected_data-66.npy')


img = x[0][0][0]
output = x[0][1][0]


print(output)
cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
