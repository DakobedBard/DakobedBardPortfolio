import json
import boto3
from boto3.dynamodb.conditions import And, Attr

def handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('DakobedTranscriptions')
    userID = event['pathParams']['userID']
    transcriptions = table.scan(FilterExpression=Attr("user").eq(userID))

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers":
                "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods":
                "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
            "Access-Control-Allow-Origin": "*"
        },
        "body": transcriptions['Items'],
    }
