import boto3
import argparse
import json
import logging
import os
import time
import uuid
from os.path import expanduser
from random import randint

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_ecs_cluster(stack_name):
    cf_client = boto3.client('cloudformation')
    ec2_client = boto3.client('ec2')

    filename = './ecs-cluster.cf'
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
                    'ParameterValue': '2',
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
                    'ParameterValue': 'm4.large',
                    'UsePreviousValue': True
                },
                {
                    'ParameterKey': 'DBUsername',
                    'ParameterValue': 'PetClinicDB'
                },
                {
                    'ParameterKey': 'DBPassword',
                    'ParameterValue': 'PetClinicPassw0rd'
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

    stack_create_status = cf_client.describe_stacks(StackName=stack_name)

    resources = cf_client.describe_stack_resources(StackName=stack_name)
    return resources



create_ecs_cluster('dakobed-style-cluster')