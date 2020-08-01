import json
import boto3



def launch_instance():
    user_data = '''#!/bin/bash -ex
            exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
            echo BEGIN
            date '+%Y-%m-%d %H:%M:%S'
            aws s3 cp s3://dakobed-transcriptions/script.py
    '''

    ec2 = boto3.resource('ec2', region_name='us-west-2')
    # ami = 'ami-003634241a8fcdec0'

    ami = 'ami-03ecf2760168d28b4'

    instance = ec2.create_instances(
        ImageId=ami,
        MinCount=1,
        MaxCount=1,
        KeyName='corwin',
        InstanceInitiatedShutdownBehavior='terminate',
        IamInstanceProfile={'Name': 'S3fullaccess'},
        InstanceType='t2.micro',
        SecurityGroupIds=['sg-09c4618f69b2e5910'],
        # UserData=user_data
    )



def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    sqs = boto3.client('sqs')
    queue = sqs.get_queue_by_name(QueueName='TransformQueue')

    instance_id = 'i-07b5b982327a4f6f2'

    describe_instances_response_response = ec2.describe_instance_status( InstanceIds=[instance_id])

    try:
        for message in queue.receive_messages():
            data = message.body
            data = json.loads(data)
            user = data['user']
            path = data['path']

            response = queue.send_message( MessageBody=json.dumps({'bucket': 'dakobed-transcriptions', 'user': user, 'path': path}))

            print(data)
            message.delete()
    except Exception as e:
        print(e)

    ec2.start_instances(InstanceIds=['i-07b5b982327a4f6f2'])




