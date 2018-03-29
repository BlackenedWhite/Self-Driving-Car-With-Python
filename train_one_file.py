from keras.models import load_model
from keras import optimizers
from keras import callbacks
import numpy as np
import memory_profiler as mem


print('Memory (Before): ' + str(mem.memory_usage()) + 'MB')

# model = load_model("model-016.h5")
model = load_model("./models/model_2.4.5-E003-vloss0.38-vacc0.83.h5")
# adam = optimizers.Adam()
# model.compile(optimizer=adam, loss='categorical_crossentropy',
#               metrics=['accuracy'])

model.summary()

tbCallBack = callbacks.TensorBoard(
    log_dir='./Graphs/graph_2.4.2', histogram_freq=0, write_graph=True, write_images=True, batch_size=20)

checkpoint_name = './models/model_2.4.6-E{epoch:03d}-vloss{val_loss:.2f}-vacc{val_acc:.2f}.h5'
checkpoint = callbacks.ModelCheckpoint(checkpoint_name,
                                       monitor='val_loss',
                                       verbose=2,
                                       save_best_only='true',
                                       mode='auto')

print('Memory (After) : ' + str(mem.memory_usage()) + 'MB')

print("Finished callbacks...")

file_name = 'newData/merged/merged_data-6.npy'
print("loading File...")
data = np.load(file_name)
x = list(data[0])
y = list(data[1])
data = []
x = np.array(x, dtype="float") / 255.0
y = np.array(y)
# print(y[0])
# print(x[0])
print("\nStart Fitting...")
print('Memory (After) : ' + str(mem.memory_usage()) + 'MB')
model.fit(x, y, validation_split=0.20, batch_size=20, epochs=30,
          shuffle=True, verbose=1, callbacks=[tbCallBack, checkpoint])
x = []
y = []

print("Finished Fitting...")
print('......SAVING MODEL......\n')
model.save("./models/model_2.4.6.h5")
print('Memory (After) : ' + str(mem.memory_usage()) + 'MB')

#from keras.utils import plot_model
#plot_model(model, to_file='model.png')
