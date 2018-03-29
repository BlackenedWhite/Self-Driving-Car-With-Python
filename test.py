import numpy as np
import cv2
from scipy.stats import itemfreq
import time
from collections import Counter
import pandas as pd


x = np.load('newData/balanced/data_balanced-44.npy')
# x = np.load('newData/fixed/collected_data-1.npy')

imgs = x[0]
output = x[1]
x = []

for img, out in zip(imgs, output):
    img = cv2.resize(img, (800, 600))
    cv2.imshow('window', img)
    print(out)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    if cv2.waitKey(25) & 0xFF == ord('t'):
        time.sleep(5)
cv2.destroyAllWindows()
print(imgs.shape[0])

#df = pd.DataFrame(output)
# print(df.head())
# print(Counter(df[0].apply(str)))
