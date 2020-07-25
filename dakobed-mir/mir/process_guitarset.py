import os
import numpy as np
import librosa
import jams
import boto3
import json


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
    return np.asarray(notes, dtype=np.float32)


def notes_matrix_to_annotation(notes, nframes):
    binary_annotation_matrix = np.zeros((48, nframes))
    full_annotation_matrix = np.zeros((48,nframes, 6))
    for note in notes:
        starting_frame = librosa.time_to_frames(note[0])
        duration_frames = librosa.time_to_frames(note[1])
        ending_frame = starting_frame + duration_frames
        note_value, string = int(note[2])-35, int(note[3])
        binary_annotation_matrix[note_value ,starting_frame:ending_frame] = 1
        full_annotation_matrix[note_value , starting_frame:ending_frame, string]  = 1

    return binary_annotation_matrix, full_annotation_matrix


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


def process_wav_jam_pair(jam, wav, i):
    bucket = 'dakobed-guitarset'
    s3 = boto3.client('s3')
    os.mkdir('data/dakobed-guitarset/fileID{}'.format(i))

    y, sr = librosa.load(wav)
    cqt = librosa.amplitude_to_db(
        np.abs(librosa.core.cqt(y, sr=sr, n_bins=252, bins_per_octave=36, fmin=librosa.note_to_hz('C2'), norm=1))).T
    notes = jam_to_notes_matrix(jam)
    jsonNotes = []
    for note in notes:
        jsonNotes.append({'time': note[0], 'duration': note[1], 'midi': round(note[2]), 'velocity': note[3]})

    # with open('data/dakobed-guitarset/fileID{}/fileID{}notes.json'.format(i, i), 'w') as outfile:
    #     json.dump(jsonNotes, outfile)

    binary_annotation, multivariate_annotation = notes_matrix_to_annotation(notes, cqt.shape[0])

    for file, array, s3path in [('data/dakobed-guitarset/fileID{}/cqt.npy'.format(i), cqt, 'fileID{}/cqt.npy'.format(i)),
                                ('data/dakobed-guitarset/fileID{}/binary_annotation.npy'.format(i), multivariate_annotation,'fileID{}/binary_annotation.npy'.format(i)),
                                ('data/dakobed-guitarset/fileID{}/multivariate_annotation.npy'.format(i), multivariate_annotation,'fileID{}/multivariate_annotation.npy'.format(i))]:
        np.save(file, arr=array)
        with open(file, "rb") as f:
            s3.upload_fileobj(f, bucket, s3path)

    with open('data/dakobed-tabs/fileID{}.json'.format(i), "rb") as f:
        s3.upload_fileobj(f, bucket, "fileID{}/{}notes.json".format(i, i))
    with open(wav, "rb") as f:
        s3.upload_fileobj(f, bucket, "fileID{}/{}audio.wav".format(i, i))


def save_transforms_and_annotations():
    for fileID, filepair in enumerate(annotation_audio_file_paths()):
        process_wav_jam_pair(filepair[1], filepair[0], fileID)
        print("Processed filepair " + str(fileID))


save_transforms_and_annotations()
