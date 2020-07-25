import json
import boto3
import librosa

# class GuitarTab:

def jam_to_notes_matrix(jam_file):
    annotation = (jams.load(jam_file)).annotations
    # annotation['value'] = annotation['value'].apply(round_midi_numers)
    lowE = annotation[1]
    A = annotation[3]
    D = annotation[5]
    G = annotation[7]
    B = annotation[9]
    highE = annotation[11]
    notes = []
    for i,string in enumerate([lowE, A, D,G,B, highE]):
        for datapoint in string.data:
            notes.append([datapoint[0], datapoint[1], datapoint[2], i])
    notes.sort(key=lambda x: x[0])
    return notes



def generate_guitar_tab(fileID):
    s3 = boto3.resource('s3')
    obj = s3.Object('dakobed-tabs', 'fileID{}/{}notes.json'.format(fileID, fileID))
    body = obj.get()['Body'].read()
    with open(body) as f:
        data = json.load(f)
    return data

def load_wav_file_librosa(fileID):
    s3 = boto3.resource('s3')
    obj = s3.Object('dakobed-tabs', 'fileID{}/audio.wav'.format(fileID, fileID))
    body = obj.get()['Body'].read()
    y, sr = librosa.load(obj)
    return y,sr


# tab = generate_guitar_tab(0)

y, sr = librosa.load(load_wav_file_librosa(0))