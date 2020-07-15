import json

with open('output/cloudformation-output.json') as f:
  data = json.load(f)


outputs = data['Stacks'][0]['Outputs']

securitygroupID = outputs[1]['OutputValue']
publicsubnet1 = outputs[2]['OutputValue']
ecstaskrole = outputs[3]['OutputValue']
privatesubnet2 = outputs[4]['OutputValue']
region = outputs[5]['OutputValue']
vpcID = outputs[6]['OutputValue']
publicsubnet2 = outputs[7]['OutputValue']
codebuildrole = outputs[8]['OutputValue']
codepipelinerole = outputs[9]['OutputValue']
ecsservicerole = outputs[10]['OutputValue']
privatesubnet1 = outputs[11]['OutputValue']


import boto3
client = boto3.client('ecs')

# client.list_clusters()['clusterArns']


instance_list = client.list_container_instances(cluster='DakobedCluster')['containerInstanceArns']

response = client.register_task_definition(
  family='bototask2',
  networkMode='awsvpc',
  taskRoleArn='arn:aws:iam::710339184759:role/dakobed-ecs-dynamo-role',
  executionRoleArn ='arn:aws:iam::710339184759:role/ecsTaskExecutionRole',
  requiresCompatibilities=['FARGATE'],
  cpu='256',

  memory='512',
  containerDefinitions=[
    {
      'name': 'dakobedcontainer',
      'image': '710339184759.dkr.ecr.us-west-2.amazonaws.com/dakobed/services:latest',
      'cpu': 256,
      'memory': 512,
      'memoryReservation': 123,
      'logConfiguration':{
        "logDriver": "awslogs",
        "options":{
          "awslogs-group": "dakobedservice-logs",
          "awslogs-region": "us-west-2",
          "awslogs-stream-prefix": "awslogs-dakobedservice-logs"
        }
      },
      'portMappings': [
        {
          'containerPort': 8080,
          'hostPort': 8080,
          'protocol': 'http'
        },
      ],
      'essential': True,
    },
  ],
)




