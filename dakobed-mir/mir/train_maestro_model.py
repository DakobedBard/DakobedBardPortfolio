from generator import guitarsetGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Conv2D, MaxPool2D, Flatten
from math import floor
import os
import psutil
from keras.callbacks import Callback


class CustomCallback(Callback):
    def on_train_batch_begin(self, batch, logs=None):
        process = psutil.Process(os.getpid())
        print("Training start of batch w/ memory usage {}".format(process.memory_info().rss))


def build_model():
    model = Sequential()
    model.add(Conv2D(filters = 64, kernel_size = (3,3), kernel_initializer='normal', activation='relu', padding = 'same',input_shape=( 5,252,1)))
    model.add(MaxPool2D(pool_size =(2,2)))
    model.add(Dropout(.25))
    model.add(Flatten())
    model.add(Dense(128, activation='tanh'))
    model.add(Dropout(.2))
    model.add(Dense(88,kernel_initializer='normal', activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam')
    return model


batch_size = 32
model = build_model()
num_epochs = 10

model.fit_generator(generator=guitarsetGenerator(32),
                    epochs=num_epochs,
                    steps_per_epoch = floor(8382182/batch_size),
                    verbose=1,
                    use_multiprocessing=True,
                    workers=16,
                    validation_data = guitarsetGenerator(32,False),
                    validation_steps = floor(888281/batch_size),
                    callbacks=[CustomCallback()],
                    max_queue_size=32)
