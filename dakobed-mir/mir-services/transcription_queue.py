import boto3
import json
sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='TransformQueue', Attributes={'DelaySeconds': '5'})

queue = sqs.get_queue_by_name(QueueName='TransformQueue')

response = queue.send_message(MessageBody= json.dumps( {'bucket':'dakobed-transcriptions', 'path':'first_audio.wav'}))

sqs_client = boto3.client('sqs')

# sqs_client.

def send():
    sqs_client = boto3.client('sqs')
    response = sqs_client.send_message(
        QueueUrl=queue.url,
        DelaySeconds=10,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'John Grisham'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )

def receive():
    sqs = boto3.resource('sqs')
    queue = sqs.create_queue(QueueName='TransformQueue', Attributes={'DelaySeconds': '5'})
    data = []
    try:
        for message in queue.receive_messages():
            data = message.body
            data = json.loads(data)
            message.delete()
    except Exception as e:
        print(e)
        return []
    return data

# response = sqs_client.send_message(
#     QueueUrl=queue.url,
#     DelaySeconds=10,
#     MessageAttributes={
#         'Title': {
#             'DataType': 'String',
#             'StringValue': 'The Whistler'
#         },
#         'Author': {
#             'DataType': 'String',
#             'StringValue': 'John Grisham'
#         },
#         'WeeksOn': {
#             'DataType': 'Number',
#             'StringValue': '6'
#         }
#     },
#     MessageBody=(
#         'Information about current NY Times fiction bestseller for '
#         'week of 12/11/2016.'
#     )
# )
# sqs_client = boto3.client('sqs')
#
# message_received_response = sqs_client.receive_message(
#     QueueUrl=queue.url,
#     AttributeNames=[
#         'SentTimestamp'
#     ],
#     MaxNumberOfMessages=1,
#     MessageAttributeNames=[
#         'All'
#     ],
#     VisibilityTimeout=0,
#     WaitTimeSeconds=0
# )