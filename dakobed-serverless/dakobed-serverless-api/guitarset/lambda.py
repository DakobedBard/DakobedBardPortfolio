import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Dakobed-GuitarSet')
    data = table.scan()
    guitarset = data['Items']
    return {
        "statusCode": 200,
        "body": guitarset,
    }
