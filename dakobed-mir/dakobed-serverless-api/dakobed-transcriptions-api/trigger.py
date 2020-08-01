import boto3
import json

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='DakobedEC2Transforms')

queue.send_message( MessageBody=json.dumps({'bucket': 'dakobed-transcriptions', 'user': 'mddarr', 'path': 'mddarr/audio.wav'}))
