import boto3

# cluster_response = client.create_cluster(
#     clusterName='my_cluster',
# )
ecr_client = boto3.client('ecr')
authresp = ecr_client.get_authorization_token(
    registryIds=[
        '710339184759',
    ]
)

client = boto3.client('ecs')
response = client.register_task_definition(
    family='ecs-task-boto',
    taskRoleArn='arn:aws:iam::710339184759:role/ecsTaskExecutionRole',
    executionRoleArn='arn:aws:iam::710339184759:role/ecsTaskExecutionRole',
    networkMode='awsvpc',
    containerDefinitions=[
        {
            'name': 'style-c',
            'image': '710339184759.dkr.ecr.us-west-2.amazonaws.com/dakobed-style:latest',
            'repositoryCredentials': {
                'credentialsParameter': 'string'
            },
            'cpu': 123,
            'memory': 123,
            'memoryReservation': 123,


            'entryPoint': [
                'python3 transfer.py',
            ],

            'environment': [
                {
                    'name': 'style_dir',
                    'value': 'user'
                },
            ],


        },
    ],
    requiresCompatibilities=[
        'FARGATE',
    ],
    # cpu='string',
    # memory='string',
    tags=[
        {
            'key': 'string',
            'value': 'string'
        },
    ],

)
