from keras.models import load_model
from keras import optimizers
from keras import callbacks
import numpy as np


model = load_model("second_model.h5")
model.compile(optimizers.Adam(), loss='categorical_crossentropy',
              metrics=['accuracy'])

tbCallBack = callbacks.TensorBoard(
    log_dir='./graph', histogram_freq=0, write_graph=True, write_images=True)

# model.summary()

for e in range(30):
    for i in range(1, 60):
        file_name = 'collectedData/collected_data-{}.npy'.format(i)
        data = np.load(file_name)
        x = list(data[0][0])
        X = np.array(x, dtype="float") / 255.0
        y = list(data[0][1])
        y = np.array(y)
        print("Start Fitting File {} ...\n".format(i))
        model.fit(X, y, validation_split=0.20, batch_size=10, epochs=1,
                  shuffle=True, verbose=2, callbacks=[tbCallBack])
        print("\nFinished Fitting File {} ...\n".format(i))
        print('......SAVING MODEL......\n\n')
        model.save("first_model.h5")


#from keras.utils import plot_model
#plot_model(model, to_file='model.png')
