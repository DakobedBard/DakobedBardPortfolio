import json
import base64
import boto3
# import requests

BUCKET_NAME = 'dakobed-transcriptions'

def lambda_handler(event, context):
    file_content = base64.b64decode(event['content'])
    file_path = 'audio.wav'
    s3 = boto3.client('s3')
    try:
        s3_response = s3.put_object(Bucket=BUCKET_NAME, Key=file_path, Body=file_content)
    except Exception as e:
        return {
            'statusCode': 200,
            'body': {
                'file_path': file_path
            }
        }
    return {
        'statusCode': 503,
        'body': {
            'file_path': file_path
        }
    }