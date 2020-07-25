import os
from mido import MidiFile, merge_tracks
import pandas as pd
import boto3
import librosa
import numpy as np
import json
import librosa.display
from numpy import format_float_positional


def generate_annotation_matrix(notes, frames):
    '''
    This function will return a one hot encoded matrix of notes being played
    The annotation matrix will start w/ note 25 at index 0 and go up to note 100
    The highest and lowest values that I saw in the annotations seemed to be arounnd 29-96 so give a little leeway
    :return:
    '''
    annotation_matrix = np.zeros((88, frames))
    for note in notes:
        starting_frame = librosa.time_to_frames(note[0])
        duration_frames = librosa.time_to_frames(note[0] + float(note[1]))
        note_value = note[2]
        annotation_matrix[note_value - 25][starting_frame:starting_frame + duration_frames] = 1
    return annotation_matrix.T


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


def extract_notes_midi(midi_file):
    '''
    Return a list of notes extracted from the MIDI file
    Leave some dang comments!!! Output notes array will have midi value first, then tim
    onset time,,
    duration,
    midi value
    note velocity
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
                current_notes.add((msg.note, current_time))
            else:
                note = remove_note(current_notes, msg.note)
                notes.append((spt * note[1], np.format_float_positional(spt * (current_time - note[1]), 2), msg.note))
    notes.sort(key=lambda x:x[0])
    return notes


def process_midi_wav_file_pair(wav, midi, i, s3, bucket ):
    os.mkdir('data/dakobed-maestro/fileID{}'.format(i))
    y, sr = librosa.load(wav)
    cqt = librosa.amplitude_to_db(
        np.abs(librosa.core.cqt(y, sr=sr, n_bins=252, bins_per_octave=36, fmin=librosa.note_to_hz('C2'), norm=1))).T
    notes = extract_notes_midi(midi)
    # jsonNotes = []
    # for note in notes:
    #     jsonNotes.append({'time': note[0], 'duration': note[1], 'midi': round(note[2]), 'velocity': note[3]})
    #
    # with open('data/dakobed-maestro/fileID{}/fileID{}notes.json'.format(i, i), 'w') as outfile:
    #     json.dump(jsonNotes, outfile)

    annotation = generate_annotation_matrix(notes, cqt.shape[0])

    for file, array, s3path in [('data/dakobed-maestro/fileID{}/cqt.npy'.format(i), cqt, 'fileID{}/cqt.npy'.format(i)),
                                ('data/dakobed-maestro/fileID{}/annotation.npy'.format(i), annotation, 'fileID{}/annotation.npy'.format(i))]:
        np.save(file, arr=array)
        with open(file, "rb") as f:
            s3.upload_fileobj(f, bucket, s3path)

    # with open('data/dakobed-tabs/fileID{}.json'.format(i), "rb") as f:
    #     s3.upload_fileobj(f, bucket, "fileID{}/{}notes.json".format(i, i))
    with open(wav, "rb") as f:
        s3.upload_fileobj(f, bucket, "fileID{}/audio.wav".format(i))


class Transcription:
    def __init__(self, wav, notes, fileID ):
        y, sr = librosa.load(wav)

        tempo, beat_times = librosa.beat.beat_track(y, sr=sr, start_bpm=60, units='time')
        self.fileID = fileID
        self.s3client = s3client
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
        notesArray = []
        for note in notes:
            notesArray.append([format_float_positional(note[0], 2), note[1], note[2]])

        for note in notesArray:
            if float(note[0]) > current_measure_end:
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
                note_dictionary = {'measure':str(m),'midi': str(notes[i][2]), 'duration': str(durations[i]), 'beat':str(beats[i])}
                transcription.append(note_dictionary)
        with open('data/dakobed-maestro/fileID{}/transcription.json'.format(self.fileID), 'w') as outfile:
            json.dump(transcription, outfile)
        s3client = boto3.client('s3')
        bucket = 'dakobed-maestro'
        with open('data/dakobed-maestro/fileID{}/transcription.json'.format(self.fileID), "rb") as f:
            s3client.upload_fileobj(f, bucket, "fileID{}/transcription.json".format(self.fileID))

class Measure:
    def __init__(self, notes, index):
        self.notes = notes
        start_of_measure = float(notes[0][0])
        end_of_measure = float(notes[-1][0])
        measureduration = float(notes[-1][0]) -float(notes[0][0])
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
            absolute_val_beat_times_array = np.abs(sixteenth_note_buckets - float(note[0]))
            note_beat = absolute_val_beat_times_array.argmin()
            processed_note_beats.append(note_beat)

            absolute_val_note_durations_array = np.abs(note_durations - float(note[1]))
            duration = absolute_val_note_durations_array.argmin()
            processed_note_durations.append(duration)

        self.note_durations = processed_note_durations
        self.note_beats = processed_note_beats
        self.notes = notes


def create_maestro_pieces_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2') #, endpoint_url='http://localhost:8000/')
    try:
        resp = dynamodb.create_table(
            AttributeDefinitions=[
                {
                    "AttributeName": "PieceID",
                    "AttributeType": "S" },
            ],
            TableName="Dakobed-Maestro",
            KeySchema=[
                {
                    "AttributeName": "PieceID",
                    "KeyType": "HASH"
                },
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            })

    except Exception as e:
        print(e)
create_maestro_pieces_table()

maestro_df = pd.read_csv('maestro-v2.0.0.csv')
s3client = boto3.client('s3')
bucket = 'dakobed-maestro'


for fileID in range(4,1282):
    row = maestro_df.iloc[fileID]
    if row['year'] == 2018:
        continue
    print("Processing fileID {}".format(fileID))
    wav = 'data/maestro/' + row['audio_filename']
    midi = 'data/maestro/' + row['midi_filename']

    dynamoDB = boto3.client('dynamodb', region_name='us-west-2')
    try:
        dynamoDB.put_item(
            TableName="Dakobed-Maestro",
            Item={
                "PieceID" : {"S":str(fileID)},
                "PieceName": {"S":row['canonical_title']},
                "Composer":{"S":row['canonical_composer']}
            }
        )
    except Exception as e:
        print(e)

    try:
        process_midi_wav_file_pair(wav, midi, fileID, s3client, bucket)
        notes = extract_notes_midi(midi)
        #tab = Transcription(wav, notes, fileID)
    except Exception as e:
        print(e)

