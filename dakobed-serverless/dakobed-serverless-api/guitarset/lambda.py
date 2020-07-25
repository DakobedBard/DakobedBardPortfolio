import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('Dakobed-GuitarSet')
    data = table.scan()
    guitarset = str(data['Items'])
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": guitarset,
            # "location": ip.text.replace("\n", "")
        }),
    }
