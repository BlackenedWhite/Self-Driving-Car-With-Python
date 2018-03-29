import numpy as np
import os

file_count = 1
step = 20
for i in range(110, 301, step):
    start = i
    end = i + step
    for file_num in range(start, end):
        file_name = "newData/collected_data-{}.npy".format(file_num)
        print(file_num)
        if (os.path.isfile(file_name)):
            data = np.load(file_name)
            if file_num == start:
                all_imgs = np.array(data[0][0])
                all_output = np.array(data[0][1])
            else:
                all_imgs = np.append(all_imgs, data[0][0])
                all_output = np.append(all_output, data[0][1])
            data = []

    print("Merged all data")
    print("shuffling...")
    s = np.arange(all_imgs.shape[0])
    np.random.shuffle(s)
    all_imgs = all_imgs[s]
    all_output = all_output[s]
    all_data = [all_imgs, all_output]
    print("Saving File...")
    np.save("newData/merged/merged_data-{}.npy".format(file_count), all_data)
    all_data = []
    file_count += 1
