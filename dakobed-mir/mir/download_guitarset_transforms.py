import boto3
import os

for dir in ['data/train', 'data/test','data']:
    try:
        os.removedirs(dir)
    except Exception as e:
        pass

s3_resource = boto3.resource('s3')
bucketName = 'dakobed-guitarset'
bucket = s3_resource.Bucket(bucketName)

os.mkdir('data')
os.mkdir('data/dakobed-guitarset')
for fileID in range(360):
    print(fileID)
    os.mkdir('data/dakobed-guitarset/fileID{}/'.format(fileID))
    path = 'data/dakobed-guitarset/fileID{}'.format(fileID)
    cqtfile = 'fileID{}/cqt.npy'.format(fileID)
    annotation_file = 'fileID{}/binary_annotation.npy'.format(fileID)
    bucket.download_file(cqtfile, path+'/cqt.npy')
    bucket.download_file(annotation_file, path+'/annotation.npy')
    if fileID > 3:
        break