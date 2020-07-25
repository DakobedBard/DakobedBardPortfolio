import librosa
import numpy as np
import json
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


def load_wave():
    y,sr = librosa.load("data/maestro/2008/MIDI-Unprocessed_10_R2_2008_01-05_ORIG_MID--AUDIO_10_R2_2008_wav--1.wav")
    return y,sr

def load_notes():
    with open("data/dakobed-maestro/fileID1/fileID119notes.json") as f:
        notes = json.load(f)
    notes_aray = []
    for note in notes:
        notes_aray.append([note['time'],note['duration'], note['midi']])
    return np.asarray(notes_aray, dtype=np.float)


def notes_duration_histogram(notes, y,sr, plot=True):
    noteDurations = notes[:, 1]
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    npoints = 300
    time = np.linspace(0, 2, npoints)
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


notes = load_notes()
y,sr = load_wave()






duration_bins, bins,peaks = notes_duration_histogram(notes,y,sr,True)
