import json
import boto3
# import requests

def lambda_handler(event, context):
    dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')
    location = 'no location'
    sdate ='20140101'
    edate ='20140103'
    items = []
    try:
        location = event['queryStringParameters']['location']
        sdate = event['queryStringParameters']['sdate']
        edate = event['queryStringParameters']['edate']

        response = dynamodb_client.query(
            TableName='Snotel',
            KeyConditionExpression='LocationID = :LocationID and SnotelDate BETWEEN :sdate and :edate',
            ExpressionAttributeValues={
                ':LocationID': {'S': location},
                ':sdate': {'S': sdate},
                ':edate': {'S': edate}
            }
        )
        items = response['Items']

    except Exception as e:
        print(e)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": items,
        }),
    }


