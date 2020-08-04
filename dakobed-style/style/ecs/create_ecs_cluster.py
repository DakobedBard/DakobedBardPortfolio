import boto3
import json
import os
import logging
import uuid
import time
import argparse
import botocore
from os.path import expanduser
from random import randint

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def delete_ecs_cluster(stack_name):
    cf_client = boto3.client('cloudformation')
    ec2_client = boto3.client('ec2')

    try:
        response = cf_client.delete_stack(StackName=stack_name)
        stack_delete_status = cf_client.describe_stacks(StackName=stack_name)
        logger.info("Delete stack: " + json.dumps(response))
        while stack_delete_status['Stacks'][0]['StackStatus'] == 'DELETE_IN_PROGRESS':
            time.sleep(10)
            stack_delete_status = cf_client.describe_stacks(StackName=stack_name)
            logger.info("Delete stack status: " + stack_delete_status['Stacks'][0]['StackStatus'])
            if stack_delete_status['Stacks'][0]['StackStatus'] == 'DELETE_FAILED':
                logger.warning('Delete failed. Retry delete')
                resources = cf_client.delete_stack(StackName=stack_name)
                return resources
            elif stack_delete_status['Stacks'][0]['StackStatus'] == 'DELETE_IN_PROGRESS':
                continue
            else:
                logger.info("Delete cluster complete")
    except Exception as e:
        logger.error(e)

    try:
        response = ec2_client.delete_key_pair(KeyName=stack_name + 'key')
        logger.info("Delete key: " + json.dumps(response))
    except Exception as e:
        logger.error(e)


def create_ecs_cluster(stack_name):
    cf_client = boto3.client('cloudformation')
    ec2_client = boto3.client('ec2')

    filename = './cloudformation/style.cf'
    with open(filename, 'r+') as f:
        cloudformation_json = json.load(f)

    describe_images_response = ec2_client.describe_images(
        DryRun=False,
        Owners=[
            'amazon',
        ],
        Filters=[
            {
                'Name': 'name',
                'Values': [
                    'amzn-ami-2016.09.f-amazon-ecs-optimized',
                ]
            },
        ]
    )
    try:
        ec2_client.create_key_pair(
            DryRun=False,
            KeyName=stack_name + 'key'
        )
    except Exception as e:
        pass

    try:
        response = cf_client.create_stack(
            StackName=stack_name,
            TemplateBody=json.dumps(cloudformation_json),
            Parameters=[
                {
                    'ParameterKey': 'AsgMaxSize',
                    'ParameterValue': '3',
                    'UsePreviousValue': True
                },
                {
                    'ParameterKey': 'EcsAmiId',
                    'ParameterValue': describe_images_response['Images'][0]['ImageId'],
                    'UsePreviousValue': True
                },
                {
                    'ParameterKey': 'EcsClusterName',
                    'ParameterValue': stack_name,
                    'UsePreviousValue': True
                },
                {
                    'ParameterKey': 'KeyName',
                    'ParameterValue': stack_name + 'key',
                    'UsePreviousValue': True
                },
                {
                    'ParameterKey': 'EcsInstanceType',
                    'ParameterValue': 't2.nano',
                    'UsePreviousValue': True
                },
                {
                    'ParameterKey': 'DBUsername',
                    'ParameterValue': 'postgres'
                },
                {
                    'ParameterKey': 'DBPassword',
                    'ParameterValue': 'iksarman'
                }
            ],
            TimeoutInMinutes=123,
            Capabilities=[
                'CAPABILITY_IAM',
            ],
            OnFailure='DELETE',
            Tags=[
                {
                    'Key': 'Name',
                    'Value': stack_name
                },
            ]
        )
    except cf_client.exceptions.AlreadyExistsException:
        logger.warning("CF Stack already exists")
        pass

    resources = cf_client.describe_stack_resources(StackName=stack_name)
    return resources
resources = create_ecs_cluster('style-transfer-cluster')