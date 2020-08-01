import boto3
import json

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='DakobedEC2Transforms')
queue.send_message( MessageBody=json.dumps({'bucket': 'dakobed-transcriptions', 'user': 'mddarr', 'path': 'mddarr/audio.wav'}))

sqs = boto3.resource('sqs')
queue = sqs.Queue(url ='https://sqs.us-west-2.amazonaws.com/710339184759/TransformQueue')