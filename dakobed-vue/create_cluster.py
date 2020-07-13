import boto3
import json
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

stack_name = 'dakobed-fargate-cluster'
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


