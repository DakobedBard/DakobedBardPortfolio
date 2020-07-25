import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa
import boto3
from mido import MidiFile, merge_tracks
import pandas as  pd
import json


def seconds_per_tick(mid):
    '''
    Returns the second per tick for the midi files
    :param mid:
    :return:
    '''
    ticks_per_quarter = mid.ticks_per_beat
    microsecond_per_quarter = mid.tracks[0][0].tempo
    microsecond_per_tick = microsecond_per_quarter / ticks_per_quarter
    seconds_per_tick = microsecond_per_tick / 1000000
    return float(np.format_float_positional(seconds_per_tick, 5))


def remove_note(notes_set, note_value):
    '''
    Removes a tuple from a set based on the value of it's first element.
    '''
    for note in notes_set:
        if note[0] == note_value:
            notes_set.remove(note)
            return note


def extract_notes(midi_file):
    '''
    Return a list of notes extracted from the MIDI file
    :param midi_file:
    :return:
    '''
    mid = MidiFile(midi_file)
    spt = seconds_per_tick(mid)
    current_time = 0
    current_notes = set()
    notes = []
    for msg in merge_tracks(mid.tracks):
        current_time += msg.time
        if msg.type == 'note_on':
            if msg.velocity != 0:
                current_notes.add((msg.note, current_time, msg.velocity))
            else:
                note = remove_note(current_notes, msg.note)
                notes.append((msg.note, spt * note[1], spt * current_time,
                              np.format_float_positional(spt * (current_time - note[1]), 2), note[2]))
    return notes

def load_wave():
    y,sr = librosa.load("data/maestro/2011/MIDI-Unprocessed_10_R2_2011_MID--AUDIO_R2-D3_10_Track10_wav.wav")
    return y,sr

def load_notes():
    with open("data/dakobed-maestro/fileID316/fileID316notes.json") as f:
        data = json.load(f)
    return data
y,sr = load_wave()
notes = load_notes()





# Tempo is beats per minute.
# If we assume 4/4 timing, that would mean that we have tempo/4 measures per minute


# files = annotation_audio_file_paths()
# notes = extract_notes(files[0][1])
# y, sr = librosa.load(files[0][0])
#
# onset_env = librosa.onset.onset_strength(y, sr=sr)
# tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
# nmeasures = tempo/4
#
# notesArray = np.asarray(notes)
# noteDurations = notesArray[:,1]

import findpeaks

# Find some peaks using the smoothing parameter.
# out = findpeaks.fit(notesArray, lookahead=1, smooth=10)
# duration_histogram = np.histogram(noteDurations, np.linspace(0,3,200))
#
# durations_bins = duration_histogram[0]
# bins = duration_histogram[1][:199]

# out = findpeaks.fit(durations_bins, lookahead=1, smooth=10)
# findpeaks.plot(out)
# plt.plot(bins, durations_bins)
# plt.show()
# from scipy.signal import find_peaks
#
# peaks, _ = find_peaks(durations_bins, height=0, distance=18)
# plt.plot(bins, durations_bins)
#
# plt.plot(bins[peaks],durations_bins[peaks], "x")
# plt.show()
#

# Tempo is beats per minute.
# If we assume 4/4 timing, that would mean that we have tempo/4 measures per minute


# files = annotation_audio_file_paths()
#
# y, sr = librosa.load(files[0][0])
#
# onset_env = librosa.onset.onset_strength(y, sr=sr)
# tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
# nmeasures = tempo/4
#
# notesArray = np.asarray(notes)
# noteDurations = notesArray[:,1]
#
# import findpeaks

# Find some peaks using the smoothing parameter.
# out = findpeaks.fit(notesArray, lookahead=1, smooth=10)
# duration_histogram = np.histogram(noteDurations, np.linspace(0,3,200))
#
# durations_bins = duration_histogram[0]
# bins = duration_histogram[1][:199]

# out = findpeaks.fit(durations_bins, lookahead=1, smooth=10)
# findpeaks.plot(out)
# plt.plot(bins, durations_bins)
# plt.show()
# from scipy.signal import find_peaks
#
# peaks, _ = find_peaks(durations_bins, height=0, distance=18)
# plt.plot(bins, durations_bins)
#
# plt.plot(bins[peaks],durations_bins[peaks], "x")
# plt.show()
#
# #