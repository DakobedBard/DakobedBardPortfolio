import os
import numpy as np
import boto3


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


def create_guitarset_pieces_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2') #, endpoint_url='http://localhost:8000/')
    try:
        resp = dynamodb.create_table(
            AttributeDefinitions=[
                {
                    "AttributeName": "fileID",
                    "AttributeType": "S" },
            ],
            TableName="DakobedGuitarSet",
            KeySchema=[
                {
                    "AttributeName": "fileID",
                    "KeyType": "HASH"
                },
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            })

    except Exception as e:
        print(e)

create_guitarset_pieces_table()
# files = annotation_audio_file_paths()
# dict = {}
# for i in range(len(files)):
#     wav, jam = files[i]
#     title = wav.split('/')[-1].split('.wav')[0][3:-4]
#     print(title)
#     dict[title] = 1
#


