# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:46:19 2018

@author: kamel30816462
"""

from keras.models import load_model
from keras import optimizers
from keras import callbacks
import numpy as np
from Testmodel import build_model
from keras.callbacks import ModelCheckpoint

#model = load_model("model.h5")
model = build_model()
model.compile(optimizer = optimizers.Adam(), loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.summary()

#tbCallBack = callbacks.TensorBoard(
#    log_dir='./graph_nmodel', histogram_freq=0, write_graph=True, write_images=True)

start_file = 1
finish_file = 4
i = start_file 
checkpoint = ModelCheckpoint('model-{epoch:03d}.h5',
                                 monitor='val_loss',
                                 verbose=0,
                                 save_best_only='true',
                                 mode='auto')
def generate_arrays_from_files(start_file,finish_file):
    while True:
        for i in range(start_file,finish_file):
            file_name = 'collectedData/collected_data-{}.npy'.format(i)
            data = np.load(file_name)
            i+=1
            if(i == finish_file):
                i = start_file
            yield (np.array(list(data[0][0])),  np.array(list(data[0][1])))


print("\nStart Fitting File ...")
model.fit_generator(generate_arrays_from_files(1,4),
                    validation_data = generate_arrays_from_files(4,5),validation_steps=1,
                    steps_per_epoch=finish_file-start_file, epochs=30,
                    callbacks=[checkpoint],verbose=1)
print("Finished Fitting File ...")

#from keras.utils import plot_model
#plot_model(model, to_file='model.png')
