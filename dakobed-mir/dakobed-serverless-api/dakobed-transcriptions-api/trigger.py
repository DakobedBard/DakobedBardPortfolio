import boto3
import json


## This will trigger the Lambda function..




sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='DakobedEC2Transforms')
queue.send_message( MessageBody=json.dumps({'bucket': 'dakobed-transcriptions', 'user': 'mddarr', 'path': 'mddarr/blues.wav'}))


sqs = boto3.resource('sqs')
transform_queue = sqs.get_queue_by_name(QueueName="DakobedTransformQueue")
transform_queue.send_message( MessageBody=json.dumps({'bucket': 'dakobed-transcriptions', 'user': 'mddarr', 'path': 'mddarr/funk.wav'}))


