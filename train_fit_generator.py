# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:46:19 2018
@author: kamel30816462
"""

from keras.models import load_model
from keras import optimizers
from keras import callbacks
import numpy as np
# from Testmodel import build_model
from keras.callbacks import ModelCheckpoint
import memory_profiler as mem

print('Memory (Before) : ' + str(mem.memory_usage()) + 'MB')
model = load_model("./models/model_2.4-E016.h5")
# model = build_model()
# model.compile(optimizer=optimizers.Adam(),
#               loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

tbCallBack = callbacks.TensorBoard(
    log_dir='./Graphs/balanced_data', histogram_freq=0, write_graph=True, write_images=True)

start_file = 1
finish_file = 241
i = start_file
checkpoint_name = './models/balanced_data/model_2.4-E{epoch:03d}-vloss{val_loss:.2f}-vacc{val_acc:.2f}.h5'
checkpoint = ModelCheckpoint(checkpoint_name,
                             monitor='val_loss',
                             verbose=1,
                             save_best_only='true',
                             mode='auto')


def generate_files(start_file, finish_file):
    while True:
        for i in range(start_file, finish_file):
            try:
                file_name = 'newData/balanced/data_balanced-{}.npy'.format(i)
                data = np.load(file_name)
                i += 1
                if(i == finish_file):
                    i = start_file
                yield (np.array(list(data[0])), np.array(list(data[1])))
            except:
                pass


print('Memory (Before) : ' + str(mem.memory_usage()) + 'MB')
print("\nStart Fitting File ...")
model.fit_generator(generate_files(1, 241),
                    validation_data=generate_files(241, 302), validation_steps=60,
                    steps_per_epoch=finish_file - start_file, epochs=30,
                    callbacks=[checkpoint, tbCallBack], verbose=1)
print("Finished Fitting File ...")
print('Memory (Before) : ' + str(mem.memory_usage()) + 'MB')

#from keras.utils import plot_model
#plot_model(model, to_file='model.png')
