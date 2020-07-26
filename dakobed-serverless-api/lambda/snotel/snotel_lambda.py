import json
import boto3


def lambda_handler(event, context):
    dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')


    items = []
    try:
        location = event['queryParams']['location']
        sdate = event['queryParams']['sdate']
        edate = event['queryParams']['edate']

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
        "body": items,
    }


