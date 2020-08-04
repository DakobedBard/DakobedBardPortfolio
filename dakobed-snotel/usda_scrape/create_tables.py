import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')

try:
    resp = dynamodb.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "LocationID",
                "AttributeType": "S"
            },
            {
                "AttributeName": "Elevation",
                "AttributeType": "N"
            },
        ],
        TableName="BasinLocations",
        KeySchema=[
            {
                "AttributeName": "LocationID",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "Elevation",
                "KeyType": "RANGE"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        })
except Exception as e:
    print(e)

try:
    resp = dynamodb.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "LocationID",
                "AttributeType": "S"
            },
            {
                "AttributeName": "SnotelDate",
                "AttributeType": "S"
            },
        ],
        TableName="Snotel",
        KeySchema=[
            {
                "AttributeName": "LocationID",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "SnotelDate",
                "KeyType": "RANGE"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )
    print("Snotel Table created successfully!")
except Exception as e:
    print("Error creating table:")
    print(e)
