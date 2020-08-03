from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Conv2D, MaxPool2D, Flatten, BatchNormalization
from math import floor

import psutil
from keras.callbacks import Callback
from random import shuffle
import numpy as np
from librosa import time_to_frames
import boto3
import os

# model.add(Dropout(.25))
# model.add(Flatten())
# model.add(Dense(128, activation='tanh'))
# model.add(Dropout(.2))
# model.add(Dense(48,kernel_initializer='normal', activation='sigmoid'))



model = Sequential()
model.add(Conv2D(filters = 16, kernel_size = (5,5), kernel_initializer='normal', activation='relu', padding = 'same',input_shape=( 5,144,1)))
model.add(MaxPool2D(  pool_size =(5,5)))
model.add(Dropout(.25))
model.add(BatchNormalization())
model.add(Activation(activation='relu'))
model.compile(loss='binary_crossentropy', optimizer='adam')
model.summary()