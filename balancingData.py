import numpy as np
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTEENN
import os
import cv2

dic = {8: [1, 0, 0, 0], 4: [0, 1, 0, 0],
       2: [ 0, 0, 1, 0], 1: [0, 0, 0, 1], 0: [0, 0, 0, 0]}
file_num = 1
file_name = 'collectedData/collected_data-{}'.format(file_num)

ros = RandomOverSampler()

def balance_data(file_name):
    saved_file = file_name + '.npy'
    print(file_name)
    collected_data = np.load(saved_file)
    data = collected_data[0]
    X = list(data[0])
    y = list(data[1])
    for i in range(len(X)):
        X[i] = cv2.cvtColor(X[i],cv2.COLOR_RGBA2RGB)
    shape = X[0].shape
    dim = shape[0]*shape[1]*shape[2]
    print(shape)
    print(dim)
    for i in range(len(X)):
        X[i] = X[i].reshape(dim)
        y[i] = int(int(''.join(str(j) for j in y[i]), 2))
    X = np.array(X)
    y = np.array(y)
    rus = RandomUnderSampler()
    X_resampled, y_resampled = rus.fit_sample(X, y)
    balanced_y = []
    balanced_X = []

    for i in range(len(y_resampled)):
        balanced_y.append(dic[y_resampled[i]])
        balanced_X.append(X_resampled[i].reshape(shape[0], shape[1], shape[2]))

    collected_data = []
    collected_data.append([balanced_X, balanced_y])
    np.save(file_name + '_balanced.npy', collected_data)


while(True):
    file_name = "collectedData/collected_data-{}".format(file_num)
    if (os.path.isfile(file_name + '.npy')):
        balance_data(file_name)
        file_num += 1
    else:
        print("balanced all data")
        break
