import boto3
from boto3.dynamodb.conditions import Key, Attr


def query_table_primary_key(userID):
    dynamodb_client = boto3.client('dynamodb', region_name='us-west-2',endpoint_url='http://localhost:8000')
    items = []
    try:
        response = dynamodb_client.query(
            TableName='DakobedGuitarTranscriptions',
            KeyConditionExpression='userID = :userID',
            ExpressionAttributeValues={
                ':userID': {'S': userID}
            }
        )
        items = response['Items']

    except Exception as e:
        print(e)


dynamodb_client = boto3.client('dynamodb', region_name='us-west-2',endpoint_url='http://localhost:8000')
items = []
try:
    response = dynamodb_client.query(
        TableName='DakobedGuitarTranscriptions',
        KeyConditionExpression='userID = :userID',
        FilterExpression=Attr('artist').eq("Frank Zappa"),
        ExpressionAttributeValues={
            ':userID': {'S': 'mddarr@gmail.com'}
        }
    )
    items = response['Items']
    for item in response['Items']:
        print(item)

except Exception as e:
    print(e)






# dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
# table = dynamodb.Table('DakobedGuitarTranscriptions')
# resp = table.query(
#     # Add the name of the index you want to use in your query.
#     IndexName="GenreIndex",
#     KeyConditionExpression='Genre = :Genre and userID = :userID',
#     FilterExpression="attribute_not_exists(artist) ",
#     ExpressionAttributeValues={
#         ':Genre': 'Blues',
#         ':userID':'dsdarr@gmail.com'
#     }
# )

print("The query returned the following items:")
for item in resp['Items']:
    print(item)



#Key('Genre').eq('Blues'),