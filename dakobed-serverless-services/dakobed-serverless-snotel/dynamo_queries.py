import boto3

dynamodb = boto3.resource('dynamodb',region_name = 'us-west-2')
table = dynamodb.Table('BasinLocations')
data = table.scan()

dynamodb_client = boto3.client('dynamodb',region_name = 'us-west-2')

response = dynamodb_client.query(
    TableName='Snotel',
    KeyConditionExpression='LocationID = :LocationID and SnotelDate BETWEEN :sdate and :edate',
    ExpressionAttributeValues={
        ':LocationID': {'S': 'Pope Ridge'},
        ':sdate' : {'S':'20140102'},
        ':edate': {'S':'20140105'}
    }
)
