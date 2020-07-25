import os
import jams
import json
import boto3
import numpy as np
import librosa


def annotation_audio_file_paths(audio_dir='data/guitarset/audio/', annotation_dir='data/guitarset/annotations' ):

    audio_files = os.listdir(audio_dir)
    audio_files = [os.path.join(audio_dir, file) for file in audio_files]
    annotation_files = os.listdir(annotation_dir)
    annotation_files = [os.path.join(annotation_dir, file) for file in annotation_files]

    file_pairs = []

    for annotation in annotation_files:
        annotation_file = annotation.split('/')[-1].split('.')[0]
        for audio_file in audio_files:
            if audio_file.split('/')[-1].split('.')[0][:-4] == annotation_file:
                file_pairs.append((audio_file, annotation))
    return file_pairs


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


def process_wav_jam_pair(jam, wav, filedID):
    bucket = "dakobed-tabs"
    notes = jam_to_notes_matrix(jam)
    s3 = boto3.client('s3')
    jsonNotes = []

    for note in notes:
        jsonNotes.append({'time': note[0], 'duration': note[1], 'midi': round(note[2]), 'string': note[3]})

    with open('data/dakobed-tabs/fileID{}.json'.format(filedID), 'w') as outfile:
        json.dump(jsonNotes, outfile)
    with open('data/dakobed-tabs/fileID{}.json'.format(filedID), "rb") as f:
        s3.upload_fileobj(f, bucket, "fileID{}/{}notes.json".format(filedID,filedID))
    with open(wav, "rb") as f:
        s3.upload_fileobj(f, bucket, "fileID{}/".format(i)+ wav.split('/')[-1])

    path_ = 'data/guitarset/fileID{}'.format(filedID)
    if not os.path.isdir(path_):
        os.mkdir(path_)

    y, sr = librosa.load(wav)
    cqt =  librosa.amplitude_to_db(np.abs(librosa.core.cqt(y, sr=sr, n_bins=144, bins_per_octave=36, fmin=librosa.note_to_hz('C2'), norm=1))).T
    notes = jam_to_notes_matrix(jam)
    binary_annotation_matrix, multivariable_annotation_matrix = (notes, y.shape[0])

    uploadfiles = [('data/guitarset/fileID{}/cqt.npy'.format(filedID),cqt), ('data/guitarset/fileID{}/binary_annotation.npy'.format(filedID), binary_annotation_matrix),
                   ('data/guitarset/fileID{}/multivariable_annotation.npy'.format(filedID), multivariable_annotation_matrix)]
    for file, array in uploadfiles:
        np.save(file, arr=array)
        with open(file, "rb") as f:
            s3.upload_fileobj(f, bucket, file)


def save_transforms_and_annotations():
    for fileID, filepair in enumerate(annotation_audio_file_paths()):
        process_wav_jam_pair(filepair[1], filepair[0], fileID)
        print("Processed filepair " + str(fileID))


files = annotation_audio_file_paths()
s3 = boto3.client('s3')
bucket = 'dakobed-tabs'

for i, filePair in enumerate(files):
    wav = filePair[0]
    jam = filePair[1]
    notes = jam_to_notes_matrix(jam)
    jsonNotes = []
    for note in notes:
        jsonNotes.append({'time': note[0], 'duration': note[1], 'midi': round(note[2]), 'string': note[3]})
    with open('data/dakobed-tabs/fileID{}.json'.format(i), 'w') as outfile:
        json.dump(jsonNotes, outfile)
    new_notes_json = "fileID{}/fileID{}Notes.json".format(i,i)
    with open('data/dakobed-tabs/fileID{}.json'.format(i), "rb") as f:
        s3.upload_fileobj(f, bucket, "fileID{}/{}notes.json".format(i,i))
    with open(wav, "rb") as f:
        s3.upload_fileobj(f, bucket, "fileID{}/audio.wav".format(i))

    path_ = 'data/guitarset/fileID{}'.format(i)
    if not os.path.isdir(path_):
        os.mkdir(path_)
    print("Saved notes JSON & wav file {}".format(i))

    y, sr = librosa.load(wav)
    cqt = librosa.amplitude_to_db(
        np.abs(librosa.core.cqt(y, sr=sr, n_bins=144, bins_per_octave=36, fmin=librosa.note_to_hz('C2'), norm=1))).T
    notes = jam_to_notes_matrix(jam)
    binary_annotation_matrix, multivariable_annotation_matrix = (notes, y.shape[0])

    uploadfiles = [('data/guitarset/fileID{}/cqt.npy'.format(i), cqt, 'fileID{}/cqt.npy'.format(i)),
                   ('data/guitarset/fileID{}/binary_annotation.npy'.format(i), binary_annotation_matrix, 'fileID{}/binaryAnnotation.npy'.format(i)),
                   ('data/guitarset/fileID{}/multivariable_annotation.npy'.format(i), multivariable_annotation_matrix, 'fileID{}/multivarAnnotaion.npy'.format(i))]


    for upload in uploadfiles:

        file, array, s3path = upload[0], upload[1],upload[2]
        np.save(file, arr=array)
        with open(file, "rb") as f:
            s3.upload_fileobj(f, bucket, s3path)
    print("saved transforms")
