import boto3
from boto3.dynamodb.conditions import Key, Attr





dynamodb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')
table = dynamodb.Table('DakobedGuitarTranscriptions')

response = table.scan(
    FilterExpression=Attr('artist').eq("Floyd")
)

for item in response['Items']:
    print(item)

