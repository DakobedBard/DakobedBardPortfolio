import json
import boto3
import uuid
from dynamo_queries import transcriptions_query
from queries.queries import get_all_users_transcriptions
def handler(event, context):
    dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')
    items = get_all_users_transcriptions('mddarr@gmail.com')
    return {
        'statusCode': 200,
        'body': items
    }

    # variable = get_all_users_transcriptions()
