import json
import boto3



def lambda_handler(event, context):

    records = event['Records'][0]
    body = records['body']
    parsed_json = json.loads(body)
    bucket = parsed_json['bucket']
    user = parsed_json['user']
    path = parsed_json['path']

    ec2 = boto3.client('ec2')
    sqs = boto3.resource('sqs',region_name ='us-west-2')
    queue = sqs.Queue(url='https://sqs.us-west-2.amazonaws.com/710339184759/TransformQueue')
    instance_id = 'i-07b5b982327a4f6f2'

    try:
        response = queue.send_message( MessageBody=json.dumps({'bucket': bucket, 'user': user, 'path': path}))
        print(response)
        # ec2_response = ec2.start_instances(InstanceIds=[instance_id])
        # print(ec2_response)

    except Exception as e:
        print(e)






