import json
import boto3


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

sts_client = boto3.client('sts')
accountID = sts_client.get_caller_identity()['Account']


def create_code_build_repository(repository_name):
    code_commit_client = boto3.client('codecommit')
    response = code_commit_client.create_repository(
        repositoryName=repository_name
    )
    return response


def create_code_pipeline(code_pipeline_name, code_pipeline_role_arn, artifacts_bucket, repository_name, projects_name, cluster_name, service_name):
    client = boto3.client('codepipeline')
    response = client.create_pipeline(
        pipeline={
            'name': code_pipeline_name,
            'roleArn': code_pipeline_role_arn,
            'artifactStore': {
                'type': 'S3',
                'location': artifacts_bucket,
            },
            'stages': [
                {
                    'name': 'Source',
                    'runOrder':1,
                    "configuration":{ "ProjectName": projects_name},
                    'actions': [
                        {
                            'name': 'string',
                            'actionTypeId': {
                                'category': 'Source' ,
                                'owner': 'AWS' ,
                                'provider': 'CodeCommit',
                                'version': '1'
                            },
                            'runOrder': 1,
                            'configuration': {
                                "BranchName": "master",
                                "RepositoryName": repository_name
                            },
                            'outputArtifacts': [
                                {
                                    'name': 'DakobedService-SourceArtifact'
                                },
                            ],
                            'inputArtifacts': [ {}],
                        },
                    ]
                },
                {
                    'name': 'Build',
                    'runOrder': 1,
                    'actions': [
                        {
                            'name': 'Build',
                            'actionTypeId': {
                                'category': 'Source',
                                'owner': 'AWS',
                                'provider': 'CodeBuild',
                                'version': '1'
                            },
                            'runOrder': 1,
                            'configuration': {
                                "ProjectName":projects_name
                            },
                            'outputArtifacts': [
                                {
                                    'name': 'DakobedService-SourceArtifact'
                                },
                            ],
                            'inputArtifacts': [{
                                "name":"DakobedService-SourceArtifact"
                                }],
                        },
                    ]
                },
                {
                    'name': 'Deploy',
                    'runOrder': 1,
                    "configuration": {"ProjectName": projects_name},
                    'actions': [
                        {
                            'name': 'Deploy',
                            'actionTypeId': {
                                'category': 'Deploy',
                                'owner': 'AWS',
                                'provider': 'ECS',
                                'version': '1'
                            },
                            'runOrder': 1,
                            'configuration': {
                                "ClusterName":cluster_name,
                                "ServiceName": service_name,
                                "FileName": "imagedefinitions.json"
                            },
                            'outputArtifacts': [
                                {
                                    'name': 'DakobedService-SourceArtifact'
                                },
                            ],
                            'inputArtifacts': [{}],
                        },
                    ]
                },
            ],
            'version': 123
        },
    )


def create_code_commit_project(project_name, service_role, account_id):
    code_build_client = boto3.client('codebuild')

    response = code_build_client.create_project(
        name=project_name,
        source={
            'type': 'CODECOMMIT',
            'location': '"https://git-codecommit.us-west-2.amazonaws.com/v1/repos/DakobedServiceRepository"',
        },
        artifacts={
            'type': 'NO_ARTIFACTS',
        },
        environment={
            'type': 'LINUX_CONTAINER',
            'image': 'aws/codebuild/java:openjdk-8',
            'computeType': 'BUILD_GENERAL1_SMALL',
            'environmentVariables': [
                {
                    'name': 'AWS_ACCOUNT_ID',
                    'value': account_id,
                },
                {
                    'name': 'AWS_DEFAULT_REGION',
                    'value': 'us-west-2',
                },
            ],
            'privilegedMode': True,
        },
        serviceRole=service_role,
    )
    return response
create_code_commit_project('dakobed-service-code-commit-project', codebuildrole,accountID )


def create_security_group(vpc_id, sgname):
  ec2 = boto3.client('ec2')
  try:
      response = ec2.create_security_group(GroupName=sgname,
                                           Description='DESCRIPTION',
                                           VpcId=vpcID)
      security_group_id = response['GroupId']
      print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))
      data = ec2.authorize_security_group_ingress(
          GroupId=security_group_id,
          IpPermissions=[
              {'IpProtocol': 'tcp',
               'FromPort': 8080,
               'ToPort': 8080,
               'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
          ])
      print('Ingress Successfully Set %s' % data)
      return response['GroupId']
  except  Exception as e:
      print(e)




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

response = client.create_service(cluster='DakobedCluster',
                                 serviceName='DakobedService',
                                 launchType='FARGATE',
                                 taskDefinition='bototask2',
                                 desiredCount=1,
                                 networkConfiguration ={
                                   "awsvpcConfiguration":{
                                   "assignPublicIp": "ENABLED",
                                    "securityGroups": ["sg-02fb948632fdf200b"],
                                    "subnets":[ publicsubnet1, publicsubnet2, privatesubnet1, privatesubnet2 ]
                                   },
                                 },
                                 deploymentConfiguration={
                                  'maximumPercent': 100,
                                  'minimumHealthyPercent': 50})

sgid = create_security_group(vpcID, 'dakobedsg')

client = boto3.client('elbv2')

nlb_response = client.create_load_balancer(
    Name='dakobed-nlb',
    Subnets=[
        publicsubnet1,publicsubnet2
    ],
    # SubnetMappings=[
    #     {
    #         'SubnetId': publicsubnet1,
    #         'AllocationId': 'string',
    #         'PrivateIPv4Address': 'string'
    #     },
    #   {
    #     'SubnetId': publicsubnet2,
    #     'AllocationId': 'string',
    #     'PrivateIPv4Address': 'string'
    #   },
    # ],
    Scheme='internet-facing',

    Type='network',
    IpAddressType='ipv4'
)


target_group_response = client.create_target_group(
    Name='dakobed-target-group',
    Port=8080,
    Protocol='TCP',
    VpcId=vpcID,
)

load_balancer_arn = nlb_response['LoadBalancers'][0]['LoadBalancerArn']
target_group_arn = target_group_response['TargetGroups'][0]['TargetGroupArn']

listener_response = client.create_listener(
    DefaultActions=[
        {
            'TargetGroupArn': target_group_arn,
            'Type': 'forward',
        },
    ],
    LoadBalancerArn=load_balancer_arn,
    Port=80,
    Protocol='TCP',
)

