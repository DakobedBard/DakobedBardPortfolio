import boto3

dynamodb_client = boto3.client('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')

location = 'Trinity'
sdate = '20140101'
edate = '20140201'

response = dynamodb_client.query(
    TableName='Snotel',
    KeyConditionExpression='LocationID = :LocationID and SnotelDate BETWEEN :sdate and :edate',
    ExpressionAttributeValues={
        ':LocationID': {'S': location},
        ':sdate': {'S': sdate},
        ':edate': {'S': edate}
    }
)
items = response['Items']

data = []
for i in range(len(items)):
    data_dictionary = {}
    data_dictionary['snotelDate'] = items[i]['SnotelDate']['S']
    data_dictionary['waterCurrent'] = int(items[i]['WaterCurrent']['N'])
    data_dictionary['waterMedian'] = int(items[i]['WaterCurrentAverage']['N'])
    data_dictionary['waterPctMedian'] = int(items[i]['WaterPctAverage']['N'])
    data_dictionary['snowCurrent'] = int(items[i]['SnowCurrent']['N'])
    data_dictionary['snowMedian'] = int(items[i]['SnowMedian']['N'])
    data_dictionary['snowPctMedian'] = int(items[i]['SnowPctMedian']['N'])
    data.append(data_dictionary)

