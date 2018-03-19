from keras import optimizers
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dense, Flatten


model = Sequential()
# input layer
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(150, 200, 4)))
# hidden layers
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (5, 5), activation='relu'))
model.add(Flatten())
# output layer
model.add(Dense(5, activation="softmax"))
model.compile(optimizers.Adam(), loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

model.save('first_model.h5')    
