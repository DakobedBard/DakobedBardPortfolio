import boto3

def get_all_users_transcriptions(userID):
    dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')
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
        for item in response['Items']:
            print(item)
    except Exception as e:
        print(e)
