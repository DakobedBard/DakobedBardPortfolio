import librosa
import numpy as np
import boto3
import json

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='TransformQueue')

s3 = boto3.client('s3')

user = 'mddarr'
fileID = 1

with open('audio.wav', 'wb') as f:
    s3.download_fileobj('dakobed-guitarset', '{}/auido{}.wav'.format(user, fileID), f)

y, sr = librosa.load('audio.wav')
cqt = librosa.amplitude_to_db( np.abs(librosa.core.cqt(y, sr=sr, n_bins=144, bins_per_octave=24, fmin=librosa.note_to_hz('C2'), norm=1))).T
np.save('cqt.npy',cqt)

with open('cqt.npy', "rb") as f:
    s3.upload_fileobj(f, 'dakobed-transcriptions', '{}/cqt{}.npy'.format(user, fileID))


