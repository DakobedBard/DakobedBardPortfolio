import json
import base64
import boto3
# import requests

BUCKET_NAME = 'dakobed-transcriptions'

def lambda_handler(event, context):
    file_path = 'audio.jpg'
    # eventbody = event
    # print('The event is ' + event['body'])
    file_content = base64.b64decode(event['body'])

    s3 = boto3.client('s3')
    s3_response = ''
    try:
        s3_response = s3.put_object(Bucket='dakobed-transcriptions', Key=file_path, Body=file_content)
    except Exception as e:
        s3_response = str(e)
        print(e)

    return {
        'statusCode': 200,
        'body': json.dumps("You did it.. ")
    }


