import json
import boto3
import base64
# import requests

def lambda_handler(event, context):
    file_path = 'audio.jpg'
    # eventbody = event
    # When we use custom lambda integration & not the proxy integration we need to create a request mapping
    # that looks like so { "content": "$input.body"}  in the integration request
    #file_content = base64.b64decode(event['body'])
    # file_content = base64.b64decode(event['content'])
    #
    # s3 = boto3.client('s3')
    # s3_response = ''
    # try:
    #     s3_response = s3.put_object(Bucket='dakobed-queries', Key=file_path, Body=file_content)
    # except Exception as e:
    #     s3_response = str(e)
    #     print(e)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': event
    }