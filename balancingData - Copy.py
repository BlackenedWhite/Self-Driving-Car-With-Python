import numpy as np
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTEENN
import os
import cv2

dic = {8: [1, 0, 0, 0], 4: [0, 1, 0, 0],
       2: [ 0, 0, 1, 0], 1: [0, 0, 0, 1], 0: [0, 0, 0, 0]}
file_num = 1
file_name = 'newData/collected_data-{}'.format(file_num)

ros = RandomOverSampler()

def balance_data(x, y):
    print("start balancing....")
    X = list(x)
    y = list(y)
    print(X[0],y[0])
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
    print("finished .... Saving...")
    np.save('all_data_balanced.npy', collected_data)


while(True):
    file_name = "newData/collected_data-{}".format(file_num)
    print(file_num)
    if (os.path.isfile(file_name + '.npy')):
        data = np.load(file_name + '.npy')
        if file_num == 1:
            all_imgs = np.array(data[0][0])
            all_output = np.array(data[0][1])
        else:
            all_imgs = np.append(all_imgs, data[0][0])
            all_output = np.append(all_output, data[0][1])
        file_num += 1
    else:
        balance_data(all_imgs, all_output)
        print("balanced all data")
        break
