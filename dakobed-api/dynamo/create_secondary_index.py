import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')

try:
    resp = dynamodb.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "userID",
                "AttributeType": "S"
            },
            {
                "AttributeName": "title",
                "AttributeType": "S"
            },
        ],
        TableName="DakobedGuitarTranscriptions",
        KeySchema=[
            {
                "AttributeName": "userID",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "title",
                "KeyType": "RANGE"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        })
except Exception as e:
    print(e)


client = boto3.client('dynamodb', region_name='us-west-2',endpoint_url='http://localhost:8000')
try:
    resp = client.update_table(
        TableName="DakobedGuitarTranscriptions",
        # Any attributes used in our new global secondary index must be declared in AttributeDefinitions
        AttributeDefinitions=[
            {
                "AttributeName": "Genre",
                "AttributeType": "S"
            },
        ],
        # This is where we add, update, or delete any global secondary indexes on our table.
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    # You need to name your index and specifically refer to it when using it for queries.
                    "IndexName": "GenreIndex",
                    # Like the table itself, you need to specify the key schema for an index.
                    # For a global secondary index, you can do a simple or composite key schema.
                    "KeySchema": [
                        {
                            "AttributeName": "Genre",
                            "KeyType": "HASH"
                        }
                    ],
                    # You can choose to copy only specific attributes from the original item into the index.
                    # You might want to copy only a few attributes to save space.
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    # Global secondary indexes have read and write capacity separate from the underlying table.
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1,
                    }
                }
            }
        ],
    )
    print("Secondary index added!")
except Exception as e:
    print("Error updating table:")
    print(e)
dynamodb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')
table = dynamodb.Table('DakobedGuitarTranscriptions')
with table.batch_writer() as batch:
    batch.put_item(Item={"userID": "mddarr@gmail.com", "artist":"Frank Zappa", "title": "Blues in C", "Genre": "Blues"})
    batch.put_item(Item={"userID": "mddarr@gmail.com", "artist":"Floyd",  "title": "Blues in A Minor", "Genre": "Blues"})
    batch.put_item(Item={"userID": "dsdarr@gmail.com", "artist": "Zeppelin", "title": "Swing in C", "Genre": "Swing"})
    batch.put_item(Item={"userID": "dsdarr@gmail.com", "title": "Bossa Novva in C", "Genre": "Bossa Nova"})
    batch.put_item(Item={"userID": "dsdarr@gmail.com", "title": "Blues in C", "Genre": "Blues"})
