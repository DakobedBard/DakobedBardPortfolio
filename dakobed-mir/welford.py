from pytest import approx
import numpy as np
import boto3


def load_transform(fileID):
    cqt = np.load('data/dakobed-guitarset/fileID{}/cqt.npy'.format(fileID))
    return cqt


def welford_files(file_range=260, frequency_bins = 144):
    '''
    This method will compute the variance and the mean over a range of arrays which are loaded in files
    :param file_range:  Compute the variance over the first file_range number of files for each column in the spectograms
    :param cqt:
    :return:THe runn
    '''
    n = 0
    delta = np.zeros(frequency_bins)
    mean = np.zeros(frequency_bins)
    M2 = np.zeros(frequency_bins)
    fileids = set(range(file_range))
    # fileids.remove(835)
    while fileids:
        id_ = fileids.pop()
        print("file {}".format(id_))
        data = load_transform(id_)
        for row in data:
            n = n + 1
            delta = row - mean
            mean = mean + delta / n
            M2 = M2 + delta * (row - mean)
    welford_variance = M2 / (n - 1)
    return welford_variance, mean

var, mean = welford_files()
np.save(arr=var, file='data/guitarset-var.npy')
np.save(arr=mean, file='data/guitarset-mean.npy')
bucket = 'dakobed-guitarset'
s3 = boto3.client('s3')

with open('data/guitarset-var.npy', "rb") as f:
    a = s3.upload_fileobj(f, bucket, 'guitarset-var.npy')
with open('data/guitarset-mean.npy', "rb") as f:
    s3.upload_fileobj(f, bucket, 'guitarset-mean.npy')


def test_welford():
    '''
    Test that the calculated variances are accurate
    :return:
    '''
    spec1 = np.load('../train/fileID0/cqt.npy')
    spec2 = np.load('../train/fileID1/cqt.npy')
    concat = np.concatenate((spec1, spec2), axis=0)

    concat_variance = concat.var(axis=0)
    concat_mean = concat.mean(axis=0)
    var, mean = welford_files(2)
    assert var == approx(concat_variance, rel=1e-1)
    assert mean == approx(concat_mean, rel=1e-1)




