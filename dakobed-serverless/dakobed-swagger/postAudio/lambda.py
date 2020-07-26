import json
import boto3
import base64
# import requests


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': 'hooray'
    }