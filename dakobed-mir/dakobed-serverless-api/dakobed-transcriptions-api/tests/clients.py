import boto3


def get_s3_client():
    return boto3.client('s3')

def get_sqs_client():
    return boto3.client('sqs')

def get_ec2_client():
    return boto3.client('ec2')