import json
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-west-2')
    ec2.start_instances(InstanceIds=['i-07b5b982327a4f6f2'])