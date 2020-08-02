import boto3
import json


def handler(event, context):
    instance_id = 'i-07b5b982327a4f6f2'
    ec2_resource = boto3.resource('ec2')
    instance = ec2_resource.Instance(instance_id)
    instance_state = instance.state['Name']
    ec2_client = boto3.client('ec2')

    try:
        if instance_state != 'running' or instance_state != 'pending':
            ec2_response = ec2_client.start_instances(InstanceIds=[instance_id])
            print(ec2_response)
    except Exception as e:
        print(e)

    guitarset = 'hello'

    return {
        "statusCode": 200,
        "body": guitarset,
    }
