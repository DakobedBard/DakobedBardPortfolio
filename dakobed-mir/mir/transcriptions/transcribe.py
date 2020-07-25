import librosa
import numpy as np
import json
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import IPython.display as ipd

def load_wave():
    y,sr = librosa.load("data/maestro/2008/MIDI-Unprocessed_11_R2_2008_01-05_ORIG_MID--AUDIO_11_R2_2008_wav--5.wav")
    return y,sr

def load_notes():
    with open("data/dakobed-maestro/fileID173/fileID173notes.json") as f:
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


notes = load_notes()
y,sr = load_wave()
duration_bins, bins,peaks = notes_duration_histogram(notes,y,sr,True)
hop_length = 200 # samples per frame
onset_env = librosa.onset.onset_strength(y, sr=sr, hop_length=hop_length, n_fft=2048)
frames = range(len(onset_env))
t = librosa.frames_to_time(frames, sr=sr, hop_length=hop_length)
plt.plot(t, onset_env)
plt.xlim(0, t.max())
plt.ylim(0)
plt.xlabel('Time (sec)')
plt.title('Novelty Function')