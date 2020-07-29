import json
import boto3
import uuid

def handler(event, context):
    title = event['title']
    userID = event['userID']

    id_ = uuid.uuid1()
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('DakobedGuitarTranscriptions')
    response = table.put_item(
        Item={
            'id': str(id_),
            'title': title,
            'user': userID,
        }
    )
    return {
        'statusCode': 200,
        'body': title
    }