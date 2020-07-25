#!/bin/bash -ex
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
echo BEGIN
date '+%Y-%m-%d %H:%M:%S'
cd /home/ubuntu

pip install librosa
aws s3 cp s3://dakobed-guitarset/train_guitarset_model.py .
aws s3 cp s3://dakobed-guitarset/subkeras.py .

python3 /subkeras.py train_guitarset_model.py
echo END