import json
import boto3
# import requests

def lambda_handler(event, context):
    dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')

    sdate = event['sdate']
    edate = event['edate']
    location = event['location']

    response = dynamodb_client.query(
        TableName='Snotel',
        KeyConditionExpression='LocationID = :LocationID and SnotelDate BETWEEN :sdate and :edate',
        ExpressionAttributeValues={
            ':LocationID': {'S': 'Pope Ridge'},
            ':sdate': {'S': '20140102'},
            ':edate': {'S': '20140105'}
        }
    )
    return response['Items']

