from mido import MidiFile, merge_tracks
from numpy import format_float_positional
import os
import boto3
import numpy as np


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
    return float(format_float_positional(seconds_per_tick, 5))


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
                              format_float_positional(spt * (current_time - note[1]), 2), note[2]))
    return notes


def remove_note(notes_set, note_value):
    '''
    Removes a tuple from a set based on the value of it's first element.
    '''
    for note in notes_set:
        if note[0] == note_value:
            notes_set.remove(note)
            return note

def generate_midi_wav_file_pairs(path):
    folders  =['2013','2011','2006','2017','2015','2008', '2009', '2014', '2018', '2004']
    count = 0
    file_pairs = []

    for folder in folders:
        files = os.listdir("{}/{}".format(path,folder))
        files.sort()
        for i in range(0, len(files), 2):
            if files[i][:-4] == files[i + 1][:-3]:
                file_pairs.append((folder + '/' + files[i], folder + '/' + files[i + 1]))
    return file_pairs


def load_transform_and_annotation(fileID, fft='fft', s3=False):
    '''
    :param id: The fileID
    :param fft: if fft return the stft.npy otherwise return cqt.npy otherwise get the cqt
    :param s3: If True download from S3, otherwise get locally
    :return: spec, annotation
    '''
    if s3:
        spec, annotation = downloadS3(fileID, fft)
        return spec, annotation
    path = 'train/fileID{}/'.format(fileID) if fileID <= 1000 else 'test/fileID{}/'.format(fileID)
    annotation_label = np.load('{}annotation.npy'.format(path), allow_pickle=True)
    # annotation_label = np.load('{}annotation.npy'.format(path), allow_pickle=True)
    spec = np.load('{}stft.npy'.format(path), allow_pickle=True) if fft == 'fft' \
        else np.load('{}cqt.npy'.format(path), allow_pickle=True)
    return spec, annotation_label


def downloadS3(fileID, fft= 'stft'):
    '''
    :param fileID:  File ID
    :param fft:  default downloads the stft transform, otherwise download the .cqt file
    :return:
    '''
    bucketName = 'maestro-transforms'
    s3_resource = boto3.resource('s3')
    prefix = 'train' if fileID <= 1000 else 'test'
    bucket = s3_resource.Bucket(bucketName)
    if fft =='stft':
        bucket.download_file('{}/fileID{}/stft.npy'.format(prefix, fileID),'spec.npy')
    else:
        bucket.download_file('{}/fileID{}/cqt.npy'.format(prefix, fileID), 'spec.npy')
    bucket.download_file('train/fileID{}/annotation_label.npy'.format(fileID), 'annotation.npy')
    spec = np.load('spec.npy', allow_pickle=True)
    annotation = np.load('annotation.npy', allow_pickle=True)
    os.remove('spec.npy')
    os.remove('annotation.npy')
    return spec, annotation