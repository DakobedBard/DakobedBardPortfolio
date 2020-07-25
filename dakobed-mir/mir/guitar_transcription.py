import os
import boto3
import librosa
import numpy as np
import json
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import librosa.display
import jams
from numpy import format_float_positional


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
    return np.asarray(notes, dtype=np.float32)


def detect_tempo_for_audio_segment(audioseg, sample_rate, window, plot=True):
    tempo, beat_times = librosa.beat.beat_track(audioseg, sr=sample_rate, start_bpm=60, units='time')
    beat_times_diff = np.diff(beat_times)

    if plot:
        plt.figure(figsize=(14, 5))
        librosa.display.waveplot(audioseg, alpha=0.6)
        plt.vlines(beat_times, -1, 1, color='r')
        plt.ylim(-1, 1)
        plt.plot(window, [0]*len(window), 'x', color='black');
        plt.show()
    return tempo, beat_times, beat_times_diff


def splice_window_notes(notes, window_time_begin, window_time_end,i):
    window = []
    for i in range(i, len(notes)):
        note = notes[i]
        if note > window_time_begin and note< window_time_end:
            window.append(note)
        if note > window_time_end:
            break
    return np.asarray(window), i


def beat_audio_process(y, sr, notes):
    seconds_per_window = 20
    nsamples = seconds_per_window * sr
    n10windows = y.shape[0] // nsamples+1
    index = 0
    windows = []
    means = []

    window_note_times, index = splice_window_notes(notes, seconds_per_window * i, seconds_per_window * (i + 1), index)
    swindow = i*nsamples
    ewindow = (i*nsamples) + nsamples
    ywindow = y[swindow:ewindow]
    tempo, beat_times, beat_times_diff = detect_tempo_for_audio_segment(
        ywindow, sr, window_note_times - (seconds_per_window * i), True)
    means.append(beat_times_diff.mean())
    windows.append(window_note_times)

    beat_times_array = np.array([])
    for window in windows:
        beat_times_array = np.concatenate((beat_times_array, window))
    return beat_times_array, means


def plot_full_waveform_beats_notes(y,sr,notes):
    librosa.display.waveplot(y, alpha=0.6)
    tempo, beat_times = librosa.beat.beat_track(y, sr=sr, start_bpm=60, units='time')
    beats_list = [float(format_float_positional(beat, 3)) for beat in beat_times]
    beats = np.asarray(beats_list)
    beat_times_diff = np.diff(beat_times)
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(y, alpha=0.6)
    plt.vlines(beats, -1, 1, color='r')
    plt.ylim(-1, 1)
    plt.plot(notes, [0] * len(notes), 'x', color='black');
    plt.show()


class Transcription:
    def __init__(self, wav, notes , type):
        self.type = type
        y, sr = librosa.load(wav)
        tempo, beat_times = librosa.beat.beat_track(y, sr=sr, start_bpm=60, units='time')
        self.beats = [float(format_float_positional(beat, 3)) for beat in beat_times]
        self.assign_notes_to_measures(notes)
        self.processMeasures()
        self.generate_transcription_json()

    def processMeasures(self):
        measures = []
        for i, notes in enumerate(self.measures_notes):
            measures.append(Measure(notes, i))
        self.measures = measures

    def getMeasures(self):
        return self.measures

    def assign_notes_to_measures(self, notes):
        measures_end_times = self.beats[0::4]
        nmeasures = len(self.beats) // 4
        if len(self.beats) % 4 != 0:
            nmeasures += 1
        measures = [[] for i in range(nmeasures)]
        measure_index = 0
        current_measure_end = measures_end_times[measure_index]

        for note in notes:
            note[0] = format_float_positional(note[0], 2)

        for note in notes:
            if note[0] > current_measure_end:
                measure_index += 1
                if measure_index >= len(measures):
                    break
                measures[measure_index].append((note))
                current_measure_end = measures_end_times[measure_index]
            else:
                measures[measure_index].append(list(note))
        self.measures_notes = measures

    def generate_transcription_json(self):
        transcription = []
        for m, measure in enumerate(self.measures):
            notes = measure.notes
            beats = measure.note_beats
            durations = measure.note_durations
            for i in range(len(notes)):
                note_dictionary = {'measure':str(m),'midi': str(notes[i][2]), 'string': str(notes[i][3]), 'beat':str(beats[i])}
                transcription.append(note_dictionary)
        with open('data/transcription.json', 'w') as outfile:
            json.dump(transcription, outfile)

class Measure:
    def __init__(self, notes, index):
        start_of_measure = notes[0][0]
        end_of_measure = notes[-1][0]
        measureduration = notes[-1][0] -notes[0][0]
        sixteenth_note_duration = measureduration/16
        sixteenth_note_buckets = np.linspace(start_of_measure, end_of_measure, 16)

        # This will only be relevant when I am processing piano transcriptions.  An array containing the
        # durations of 1/16, 1/8th, 1/4, quarter dot, 1/2, 1/2 dot & whote notes for this measure.  I w

        note_durations = np.array([sixteenth_note_duration, sixteenth_note_duration*2, sixteenth_note_duration*4,
                                   sixteenth_note_duration*6, sixteenth_note_duration * 8, sixteenth_note_duration * 12,
                                   sixteenth_note_duration*16])

        processed_note_beats = []
        processed_note_durations = []

        for note in notes:
            absolute_val_beat_times_array = np.abs(sixteenth_note_buckets - note[0])
            note_beat = absolute_val_beat_times_array.argmin()
            processed_note_beats.append(note_beat)

            absolute_val_note_durations_array = np.abs(note_durations - note[1])
            duration = absolute_val_note_durations_array.argmin()
            processed_note_durations.append(duration)

        self.note_durations = processed_note_durations
        self.note_beats = processed_note_beats
        self.notes = notes

files = annotation_audio_file_paths()
wav = files[2][0]
jam = files[2][1]

y, sr = librosa.load(wav)
notes = jam_to_notes_matrix(jam)
tempo, beat_times = librosa.beat.beat_track(y, sr=sr, start_bpm=60, units='time')
beats_list = [float(format_float_positional(beat, 3)) for beat in beat_times]
tab = Transcription(wav, notes, 'guitar')
for i in range(n10windows):
    window_note_times, index = splice_window_notes(notes, seconds_per_window * i, seconds_per_window * (i + 1), index)
    swindow = i*nsamples
    ewindow = (i*nsamples) + nsamples
    ywindow = y[swindow:ewindow]
    tempo, beat_times, beat_times_diff = detect_tempo_for_audio_segment(
        ywindow, sr, window_note_times - (seconds_per_window * i), True)
    means.append(beat_times_diff.mean())
    windows.append(window_note_times)

beat_times_array = np.array([])
for window in windows:
    beat_times_array = np.concatenate((beat_times_array, window))
return beat_times_array, means


def plot_full_waveform_beats_notes(y,sr,notes):
    librosa.display.waveplot(y, alpha=0.6)
    tempo, beat_times = librosa.beat.beat_track(y, sr=sr, start_bpm=60, units='time')
    beats_list = [float(format_float_positional(beat, 3)) for beat in beat_times]
    beats = np.asarray(beats_list)
    beat_times_diff = np.diff(beat_times)
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(y, alpha=0.6)
    plt.vlines(beats, -1, 1, color='r')
    plt.ylim(-1, 1)
    plt.plot(notes, [0] * len(notes), 'x', color='black');
    plt.show()


class Transcription:
    def __init__(self, wav, notes , type):
        self.type = type
        y, sr = librosa.load(wav)
        tempo, beat_times = librosa.beat.beat_track(y, sr=sr, start_bpm=60, units='time')
        self.beats = [float(format_float_positional(beat, 3)) for beat in beat_times]
        self.assign_notes_to_measures(notes)
        self.processMeasures()
        self.generate_transcription_json()

    def processMeasures(self):
        measures = []
        for i, notes in enumerate(self.measures_notes):
            measures.append(Measure(notes, i))
        self.measures = measures

    def getMeasures(self):
        return self.measures

    def assign_notes_to_measures(self, notes):
        measures_end_times = self.beats[0::4]
        nmeasures = len(self.beats) // 4
        if len(self.beats) % 4 != 0:
            nmeasures += 1
        measures = [[] for i in range(nmeasures)]
        measure_index = 0
        current_measure_end = measures_end_times[measure_index]

        for note in notes:
            note[0] = format_float_positional(note[0], 2)

        for note in notes:
            if note[0] > current_measure_end:
                measure_index += 1
                if measure_index >= len(measures):
                    break
                measures[measure_index].append((note))
                current_measure_end = measures_end_times[measure_index]
            else:
                measures[measure_index].append(list(note))
        self.measures_notes = measures

    def generate_transcription_json(self):
        transcription = []
        for m, measure in enumerate(self.measures):
            notes = measure.notes
            beats = measure.note_beats
            durations = measure.note_durations
            for i in range(len(notes)):
                note_dictionary = {'measure':str(m),'midi': str(notes[i][2]), 'string': str(notes[i][3]), 'beat':str(beats[i])}
                transcription.append(note_dictionary)
        with open('data/transcription.json', 'w') as outfile:
            json.dump(transcription, outfile)

class Measure:
    def __init__(self, notes, index):
        start_of_measure = notes[0][0]
        end_of_measure = notes[-1][0]
        measureduration = notes[-1][0] -notes[0][0]
        sixteenth_note_duration = measureduration/16
        sixteenth_note_buckets = np.linspace(start_of_measure, end_of_measure, 16)

        # This will only be relevant when I am processing piano transcriptions.  An array containing the
        # durations of 1/16, 1/8th, 1/4, quarter dot, 1/2, 1/2 dot & whote notes for this measure.  I w

        note_durations = np.array([sixteenth_note_duration, sixteenth_note_duration*2, sixteenth_note_duration*4,
                                   sixteenth_note_duration*6, sixteenth_note_duration * 8, sixteenth_note_duration * 12,
                                   sixteenth_note_duration*16])

        processed_note_beats = []
        processed_note_durations = []

        for note in notes:
            absolute_val_beat_times_array = np.abs(sixteenth_note_buckets - note[0])
            note_beat = absolute_val_beat_times_array.argmin()
            processed_note_beats.append(note_beat)

            absolute_val_note_durations_array = np.abs(note_durations - note[1])
            duration = absolute_val_note_durations_array.argmin()
            processed_note_durations.append(duration)

        self.note_durations = processed_note_durations
        self.note_beats = processed_note_beats
        self.notes = notes

files = annotation_audio_file_paths()
wav = files[2][0]
jam = files[2][1]

y, sr = librosa.load(wav)
notes = jam_to_notes_matrix(jam)
tempo, beat_times = librosa.beat.beat_track(y, sr=sr, start_bpm=60, units='time')
beats_list = [float(format_float_positional(beat, 3)) for beat in beat_times]
tab = Transcription(wav, notes, 'guitar')