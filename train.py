from keras.models  import load_model
from keras import optimizers
import numpy as np


model = load_model("first_model.h5")
model.compile(optimizers.Adam(), loss='categorical_crossentropy',
              metrics=['accuracy'])

for i in range(1,60):
    file_name = 'collectedData/collected_data-{}.npy'.format(i)
    data = np.load(file_name)
    x =list(data[0][0])
    X = np.array(x, dtype="float") / 255.0
    
    y = list(data[0][1])
    y = np.array(y)
    model.fit(X,y,batch_size=10, epochs=30, shuffle=True, verbose=2)
    
    if i%5 ==0:
        print('......SAVING MODEL......')
        model.save("first_model.h5")