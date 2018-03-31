import numpy as np
import os
import cv2

dic = {8: [1,0,0,0],4: [0,1, 0, 0],
       2: [0,0, 1, 0], 1: [0,0, 0, 1], 0: [0,0, 0, 0]}
file_num = 1
file_name = 'newData/collected_data-{}'.format(file_num)
IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 66, 200, 3
INPUT_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)

def random_shadow(image):
    x1, y1 = IMAGE_WIDTH * np.random.rand(), 0
    x2, y2 = IMAGE_WIDTH * np.random.rand(), IMAGE_HEIGHT
    xm, ym = np.mgrid[0:IMAGE_HEIGHT, 0:IMAGE_WIDTH]
    mask = np.zeros_like(image[:, :, 1])
    mask[(ym - y1) * (x2 - x1) - (y2 - y1) * (xm - x1) > 0] = 1

    # choose which side should have shadow and adjust saturation
    cond = mask == np.random.randint(2)
    s_ratio = np.random.uniform(low=0.2, high=0.5)

    # adjust Saturation in HLS(Hue, Light, Saturation)
    hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
    hls[:, :, 1][cond] = hls[:, :, 1][cond] * s_ratio
    return cv2.cvtColor(hls, cv2.COLOR_HLS2RGB)


def random_brightness(image):
    # HSV (Hue, Saturation, Value) is also called HSB ('B' for Brightness).
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    ratio = 1.0 + 0.4 * (np.random.rand() - 0.5)
    hsv[:,:,2] =  hsv[:,:,2] * ratio
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

def balance_data(file_name):
    saved_file = file_name + '.npy'
    print(file_name)
    collected_data = np.load(saved_file)
    data = collected_data[0]
    X = list(data[0])
    y = list(data[1])
    for i in range(len(X)):
        X[i] = cv2.cvtColor(X[i],cv2.COLOR_RGBA2RGB)
    balanced_X, balanced_y = [],[]
    for i in range(len(X)):
        image = X[i]
        image = random_brightness(image)
        balanced_X.append(image)
        balanced_y.append(y[i])
        if (y[i] == dic[4]):
            balanced_X.append(cv2.flip(image, 1))
            balanced_y.append(dic[2])
        elif (y[i] == dic[2]):
           balanced_X.append(cv2.flip(image, 1))
           balanced_y.append(dic[4])
            

    collected_data = []
    collected_data.append([balanced_X, balanced_y])
    
    np.save(file_name + '_balanced.npy', collected_data)
    return collected_data

#b = balance_data(file_name)
while(True):
    file_name = "newData/collected_data-{}".format(file_num)
    if (os.path.isfile(file_name + '.npy')):
        balance_data(file_name)
        file_num += 1
#        if file_num == 2:
#            break
    else:
        print("balanced all data")
        break
