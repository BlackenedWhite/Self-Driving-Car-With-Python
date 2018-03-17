import numpy as np
from imblearn.over_sampling import RandomOverSampler
from imblearn.combine import SMOTEENN
import os
dic = {16:[1,0,0,0,0],8:[0,1,0,0,0],4:[0,0,1,0,0],2:[0,0,0,1,0],1:[0,0,0,0,1],0:[0,0,0,0,0]}
file_num = 1
file_name = 'collectedData/collected_data-{}.npy'.format(file_num)
ros = RandomOverSampler()

def balance_data(file_name):
    print(file_name)
    collected_data = np.load(file_name)
    data = collected_data[0]
    X = list(data[0])
    y = list(data[1])
    for i in range(len(X)):
        X[i] = X[i].reshape(120000)
        y[i] = int(int(''.join(str(j) for j in y[i]),2))
    X_resampled, y_resampled = ros.fit_sample(X, y)
    balanced_y = []
    balanced_X = []
    for i in range(len(y_resampled)):
        balanced_y.append(dic[y_resampled[i]])
        balanced_X.append(X_resampled[i].reshape(150,200,4))
    collected_data = []
    collected_data.append([balanced_X,balanced_y])
    np.save(file_name, collected_data)

while(True):
    file_name = "collectedData/collected_data-{}.npy".format(file_num)
    if (os.path.isfile(file_name)):
        balance_data(file_name)
        file_num+=1
    else:
        print("balanced all data")
        break