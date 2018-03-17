import numpy as np
import cv2
from imblearn.over_sampling import RandomOverSampler
collected_data = np.load('collectedData/collected_data-1.npy')
data = collected_data[0]
X = list(data[0])
y = list(data[1])
ros = RandomOverSampler()
#X_resampled, y_resampled = ros.fit_sample(X, y)
for i in range(20):
    img = X[i+20]
    output = y[i+20]
    print(output)
    cv2.imshow('window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
