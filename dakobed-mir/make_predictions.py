import keras
import numpy as np


def generate_windowed_samples(spec):
    '''
    This method creates the context window for a sample at time t, Wi-2, Wi-1, Wi, Wi+1,Wi+2
    '''
    windowed_samples = np.zeros((spec.shape[0], 5, spec.shape[1]))
    for i in range(spec.shape[0]):
        if i <= 1:
            windowed_samples[i] = np.zeros((5, spec.shape[1]))
        elif i >= spec.shape[0] - 2:
            windowed_samples[i] = np.zeros((5, spec.shape[1]))
        else:
            windowed_samples[i, 0] = spec[i - 2]
            windowed_samples[i, 1] = spec[i - i]
            windowed_samples[i, 2] = spec[i]
            windowed_samples[i, 3] = spec[i + 1]
            windowed_samples[i, 4] = spec[i + 2]
    return windowed_samples


def preprocess(mean, variance, spectogram):
    spec = generate_windowed_samples(spectogram - mean) / variance
    return np.expand_dims(spec, axis=-1)


mean = np.load('data/guitarset-mean.npy')
var = np.load('data/guitarset-var.npy')
cqt = np.load('data/dakobed-guitarset/fileID0/cqt.npy')
windowed_spectogram = preprocess(mean, var, cqt)

model =  keras.models.load_model('data/model1.h5')
import boto3
s3 = boto3.client('s3')

with open('guitarset-mean.npy', 'wb') as f:
    s3.download_fileobj('dakobed-transcriptions', 'guitarset-mean.npy', f)


s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket('dakobed-transcriptions')
bucket.download_file('model1.h5','model1.h5')
# s3.download_file('dakobed-transcriptions', 'model.h5', f)
import time

start = time.time()

bucket.download_file('model1.h5','model1.h5')
end = time.time()
print("Time consumed in working: ",end - start)


probabilities = model.predict(windowed_spectogram)