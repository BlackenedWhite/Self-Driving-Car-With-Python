import numpy as np
import os

OW = [1, 0, 0, 0]
OA = [0, 1, 0, 0]
OS = [0, 0, 1, 0]
OD = [0, 0, 0, 1]
ONOMOVE = [0, 0, 0, 0]

W = [1, 0, 0]
A = [0, 1, 0]
D = [0, 0, 1]
NM = [0, 0, 0]


def fix_data(outputs):
    new_output = np.array([[]], dtype=int)
    new_output.shape = (0, 3)
    print("Start fixing..")
    for out in outputs:
        # print(out)
        if out == OA:
            new_output = np.append(new_output, [A], axis=0)
        elif out == OD:
            new_output = np.append(new_output, [D], axis=0)
        else:
            new_output = np.append(new_output, [W], axis=0)
    return new_output


def conv(outputs):
    new_output = np.array([[]], dtype=int)
    new_output.shape = (0, 3)
    for out in outputs:
        new_output = np.append(new_output, [np.array(out)], axis=0)
    return new_output


for i in range(90, 302):
    file_name = "newData/balanced/data_balanced-{}.npy".format(i)
    print(i)
    data = np.load(file_name)
    imgs = data[0]
    outputs = data[1]
    data = []
    print("file loaded..")
    # outputs = fix_data(outputs)
    # outputs = conv(outputs)
    print('data fixed...')
    # shuffle
    s = np.arange(imgs.shape[0])
    np.random.shuffle(s)
    imgs = list(imgs[s])
    outputs = list(outputs[s])
    print("data shuflled...")
    print("Saving data...")
    data = [imgs, outputs]
    np.save("newData/balanced/data_balanced-{}.npy".format(i), data)
    data = []
    imgs = []
    outputs = []
