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
    new_output = np.array([[0, 0, 0]])
    print("Start fixing..")
    for out in outputs:
        print(out)
        if out == OA:
            new_output = np.append(new_output, [A], axis=0)
        elif out == OD:
            new_output = np.append(new_output, [D], axis=0)
        else:
            new_output = np.append(new_output, [W], axis=0)
    return new_output


file_num = 1
while(True):
    file_name = "newData/collected_data-{}.npy".format(file_num)
    print(file_num)
    if (os.path.isfile(file_name)):
        data = np.load(file_name)
        if file_num == 1:
            all_imgs = np.array(data[0][0])
            all_output = np.array(data[0][1])
        else:
            all_imgs = np.append(all_imgs, data[0][0], axis=0)
            all_output = np.append(all_output, data[0][1], axis=0)
        file_num += 1
    else:
        print("Merged all data")
        print("Fixing....")
        all_output = fix_data(all_output)
        all_output = np.delete(all_output, 0, axis=0)
        all_output = list(all_output)
        all_data = [all_imgs, all_output]
        print("Saving File...")
        np.save("newData/fixed_data.npy", all_data)
        break
