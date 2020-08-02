import librosa
import numpy as np
import boto3
import json
import os

sqs = boto3.resource('sqs')
s3 = boto3.client('s3')

dakobed_transform_queue = sqs.get_queue_by_name(QueueName='DakobedTransformQueue')
dakobed_transcription_queue = sqs.get_queue_by_name(QueueName="DakobedTranscriptionQueue")

processed_files = []

for message in dakobed_transform_queue.receive_messages():
    try:
        data = message.body
        data = json.loads(data)
        user = data['user']
        path = data['path']
        bucket = data['bucket']
        print("path:")
        print(path)
        with open('audio.wav', 'wb') as f:
            s3.download_fileobj(bucket, path, f)
        y, sr = librosa.load('audio.wav')
        cqt = librosa.amplitude_to_db(
            np.abs(librosa.core.cqt(y, sr=sr, n_bins=144, bins_per_octave=24, fmin=librosa.note_to_hz('C2'), norm=1))).T
        np.save('cqt.npy', cqt)
        s3_cqt_path = path.split('/')[1].split('.')[0] + '.npy'
        print("s3 audio path "+ str(s3_cqt_path))
        with open('cqt.npy', "rb") as f:
            s3.upload_fileobj(f, bucket, '{}/{}'.format(user, s3_cqt_path))

        processed_files.append({'path':s3_cqt_path,'user':user})
        dakobed_transcription_queue.send_message(json.dumps({'user': user, 'path':s3_cqt_path}))
        os.remove('cqt.npy')
        os.remove('audio.wav')
        message.delete()
    except Exception as e:
        print(e)





