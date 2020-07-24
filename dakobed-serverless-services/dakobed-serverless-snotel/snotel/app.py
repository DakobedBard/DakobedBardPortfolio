import json
import boto3
# import requests

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('BasinLocations')
    data = table.scan()
    locations = str(data['Items'])
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": locations,
            # "location": ip.text.replace("\n", "")
        }),
    }
