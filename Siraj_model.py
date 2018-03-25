# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:07:42 2018

@author: kamel30816462
"""
from keras import optimizers
from keras.models import Sequential
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten
def build_model():
    model = Sequential()
    model.add(Conv2D(24, 5, 5, activation='relu',subsample=(2, 2),input_shape=(100, 100, 4)))
    model.add(Conv2D(36, 5, 5, activation='relu',subsample=(2, 2)))
    model.add(Conv2D(48, 5, 5, activation='relu',subsample=(2, 2)))
    model.add(Conv2D(64, 3, 3, activation='relu'))
    model.add(Conv2D(64, 3, 3, activation='relu'))
    model.add(Dropout(.5))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(4,activation = 'sigmoid'))
    return model
