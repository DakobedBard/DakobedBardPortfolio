import boto3
import time

user_data = '''
#!/bin/bash
sudo apt install awscli
aws s3 cp s3://dakobed-guitarset/fileID0/audio.wav .
sudo apt install python3-pip
pip3 install librosa
'''

ec2 = boto3.resource('ec2', region_name='us-west-2')
ami = 'ami-003634241a8fcdec0'

instance = ec2.create_instances(
    ImageId=ami,
    MinCount=1,
    MaxCount=1,
    KeyName='corwin',
    InstanceInitiatedShutdownBehavior='terminate',
    IamInstanceProfile={'Name': 'S3fullaccess'},
    InstanceType='t2.micro',
    SecurityGroupIds=['sg-09c4618f69b2e5910'],
    UserData=user_data
)
time.sleep(10)
dns = instance[0].id

