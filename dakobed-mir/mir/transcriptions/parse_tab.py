import librosa
import os
import jams
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


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


def jam_to_notes(jam_file):
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


def notes_duration_histogram(notes, y, sr, plot):
    notesArray = np.asarray(notes)
    noteDurations = notesArray[:, 1]
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    npoints = 300
    time = np.linspace(0, 3, npoints)
    duration_histogram = np.histogram(noteDurations, time)
    durations_bins = duration_histogram[0]
    bins = duration_histogram[1][:npoints - 1]
    distance = (npoints*12)/200
    peaks, _ = find_peaks(durations_bins, height=0, distance=distance)
    if plot:
        plt.plot(bins, durations_bins)
        plt.plot(bins[peaks], durations_bins[peaks], "x")
        plt.show()
    return durations_bins, bins, peaks


files = annotation_audio_file_paths()
notes = jam_to_notes(files[4][1])
y, sr = librosa.load(files[4][0])

durations, bins,peaks = notes_duration_histogram(notes,y,sr,True)
