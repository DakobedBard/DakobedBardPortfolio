import json
import boto3
# import requests

def lambda_handler(event, context):
    dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')

    location = 'no location'
    try:
        location = event['queryStringParameters']['location']
    except Exception as e:
        print(e)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "The location is " + location,
            # "location": ip.text.replace("\n", "")
        }),
    }

    # print(event['params']['querystring']['location'])

    # return "Hello"

    # sdate = event['sdate']
    # edate = event['edate']
    # location = event['location']
    #
    # response = dynamodb_client.query(
    #     TableName='Snotel',
    #     KeyConditionExpression='LocationID = :LocationID and SnotelDate BETWEEN :sdate and :edate',
    #     ExpressionAttributeValues={
    #         ':LocationID': {'S': 'Pope Ridge'},
    #         ':sdate': {'S': '20140102'},
    #         ':edate': {'S': '20140105'}
    #     }
    # )
    # return response['Items']

