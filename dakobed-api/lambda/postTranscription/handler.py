import json
import boto3
import uuid

def handler(event, context):
    title = event['title']
    userID = event['userID']
    transcription_type = event['type']

    id_ = uuid.uuid1()
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('DakobedTranscriptions')
    response = table.put_item(
        Item={
            'id': str(id_),
            'title': title,
            'user': userID,
            'type': transcription_type
        }
    )

    return {
        'statusCode': 200,
        'body': title
    }