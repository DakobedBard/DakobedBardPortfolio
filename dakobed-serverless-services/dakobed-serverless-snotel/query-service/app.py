import json
import boto3
# import requests

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('BasinLocations')
    data = table.scan()

    return {
        "statusCode": 200,
        "body": data['Items']}
