import json
import boto3
import uuid
from dynamo_queries import transcriptions_query

def handler(event, context):
    variable = transcriptions_query()
    return {
        'statusCode': 200,
        'body': variable
    }