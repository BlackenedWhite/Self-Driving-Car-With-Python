from keras.models import load_model
from keras import optimizers
from keras import callbacks
import numpy as np


model = load_model("new_model_2.2.h5")
adam = optimizers.Adam(lr=0.001)
model.compile(optimizer = adam, loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.summary()

tbCallBack = callbacks.TensorBoard(
    log_dir='./graph_nmodel_2.2', histogram_freq=0, write_graph=True, write_images=True, batch_size=10)

start_file = 50
finish_file = 78

for i in range(start_file, finish_file):
    file_name = 'newData/collected_data-{}.npy'.format(i)
    data = np.load(file_name)
    x = list(data[0][0])
    X = np.array(x, dtype="float") / 255.0
    y = list(data[0][1])
    y = np.array(y)
    print("\nStart Fitting File {} ...".format(i))
    model.fit(X, y, validation_split=0.20, batch_size=10, epochs=30,
              shuffle=True, verbose=1, callbacks=[tbCallBack])
    print("Finished Fitting File {} ...".format(i))
    print('......SAVING MODEL......\n')
    model.save("new_model_2.2.h5")


#from keras.utils import plot_model
#plot_model(model, to_file='model.png')
