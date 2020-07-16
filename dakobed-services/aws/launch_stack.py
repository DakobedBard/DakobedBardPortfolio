import boto3
import json


def launch_stack():
    cloud_formation_client = boto3.client('cloudformation')
    with open('stack.yml', 'r') as cf_file:
        cft_template = cf_file.read()
        cloud_formation_client.create_stack(StackName='DakobedStack', TemplateBody=cft_template, Capabilities=['CAPABILITY_NAMED_IAM'])
    waiter =cloud_formation_client.get_waiter('stack_create_complete')
    print("...waiting for stack to be ready...")
    waiter.wait(StackName='DakobedStack')

    stack_json = cloud_formation_client.describe_stacks(StackName='DakobedStack')

    with open('output/stack_output.json', 'w') as fp:
        json.dump(stack_json, fp, default=str)


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


def create_security_group(vpcID, sgname):
  ec2 = boto3.client('ec2')
  try:
      response = ec2.create_security_group(GroupName=sgname,
                                           Description='DESCRIPTION',
                                           VpcId=vpcID)
      security_group_id = response['GroupId']
      print('Security Group Created %s in vpc %s.' % (security_group_id, vpcID))
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


def register_ecs_task(task_name):
    client = boto3.client('ecs')

    # client.list_clusters()['clusterArns']
    instance_list = client.list_container_instances(cluster='DakobedCluster')['containerInstanceArns']
    response = client.register_task_definition(
        family=task_name,
        networkMode='awsvpc',
        taskRoleArn='arn:aws:iam::710339184759:role/dakobed-ecs-dynamo-role',
        executionRoleArn='arn:aws:iam::710339184759:role/ecsTaskExecutionRole',
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
                'logConfiguration': {
                    "logDriver": "awslogs",
                    "options": {
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


def create_ecs_service(service_name, task_name, subnets, security_group_id, target_group_arn):

    client = boto3.client('ecs')
    response = client.create_service(cluster='DakobedCluster',
                                     serviceName=service_name,
                                     launchType='FARGATE',
                                     taskDefinition=task_name,
                                     desiredCount=1,
                                     networkConfiguration={
                                         "awsvpcConfiguration": {
                                             "assignPublicIp": "ENABLED",
                                             "securityGroups": [security_group_id],
                                             "subnets": [subnets['public1'],subnets['public2'], subnets['private1'], subnets['private2']]# publicsubnet2, privatesubnet1, privatesubnet2]
                                         },
                                     },
                                     deploymentConfiguration={
                                         'maximumPercent': 100,
                                         'minimumHealthyPercent': 50},
                                    loadBalancers = [
                                        {"containerName":"dakobedcontainer",
                                         "containerPort":8080,
                                         "targetGroupArn":target_group_arn
                                        }
                                    ]),

    return response

def create_network_load_balancer(load_balancer_name, publicsubnet1, publicsubnet2):
    client = boto3.client('elbv2')
    nlb_response = client.create_load_balancer(
        Name=load_balancer_name,
        Subnets=[
            publicsubnet1, publicsubnet2
        ],
        Scheme='internet-facing',
        Type='network',
        IpAddressType='ipv4'
    )
    return  nlb_response
    #eturn nlb_response['LoadBalancers'][0]['LoadBalancerArn']

def create_application_load_balancer(load_balancer_name, publicsubnet1, publicsubnet2):
    client = boto3.client('elbv2')
    nlb_response = client.create_load_balancer(
        Name=load_balancer_name,
        Subnets=[
            publicsubnet1, publicsubnet2
        ],
        Scheme='internet-facing',
        Type='network',
        IpAddressType='ipv4'
    )
    return  nlb_response


def create_target_group(target_group_name, vpcID):
    client = boto3.client('elbv2')
    target_group_response = client.create_target_group(
        Name=target_group_name,
        Port=8080,
        Protocol='TCP',
        VpcId=vpcID,
        TargetType='ip'
    )
    return target_group_response['TargetGroups'][0]['TargetGroupArn']

def create_network_load_balancer_listener(load_balancer_arn, target_group_arn):
    client = boto3.client('elbv2')
    # target_group_arn = target_group_response['TargetGroups'][0]['TargetGroupArn']
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
    return listener_response

def create_application_load_balancer_listener(application_load_balancer_arn, target_group_arn):
    client = boto3.client('elbv2')
    # target_group_arn = target_group_response['TargetGroups'][0]['TargetGroupArn']
    listener_response = client.create_listener(
        DefaultActions=[
            {
                'TargetGroupArn': target_group_arn,
                'Type': 'forward',
            },
        ],
        LoadBalancerArn=application_load_balancer_arn,
        Port=80,
        Protocol='TCP',
    )
    return listener_response


with open('output/stack_output.json') as f:
  data = json.load(f)

outputs = data['Stacks'][0]['Outputs']

stack = {}
stack['accountID'] = outputs[0]['OutputValue']
stack['securitygroupID'] = outputs[1]['OutputValue']
stack['publicsubnet1'] = outputs[2]['OutputValue']
stack['ecstaskrole'] = outputs[3]['OutputValue']
stack['privatesubnet2'] = outputs[4]['OutputValue']
stack['region'] = outputs[5]['OutputValue']
stack['vpcID'] = outputs[6]['OutputValue']
stack['publicsubnet2'] = outputs[7]['OutputValue']
stack['codebuildrole'] = outputs[8]['OutputValue']
stack['codepipelinerole'] = outputs[9]['OutputValue']
stack['ecsservicerole'] = outputs[10]['OutputValue']
stack['privatesubnet1'] = outputs[11]['OutputValue']


security_group_id = create_security_group(stack['vpcID'], 'dakobed-sg')

task_name = 'DakobedServiceTask'
service_name ='DakobedEcsService'

register_ecs_task(task_name)

subnets = {'public1':stack['publicsubnet1'], 'public2':stack['publicsubnet2'], 'private1':stack['privatesubnet1'], 'private2':stack['privatesubnet2']}

### Application Load Balancer

application_load_balancer_response = create_application_load_balancer('dakobedapplicationlb', stack['publicsubnet1'], stack['publicsubnet2'])
application_load_balancer_arn = application_load_balancer_response['LoadBalancers'][0]['LoadBalancerArn']
load_balancer_dns = application_load_balancer_response['LoadBalancers'][0]['DNSName']

target_group_arn = create_target_group('dakobed-target-group',stack['vpcID'])

create_application_load_balancer_listener(application_load_balancer_arn, target_group_arn)

service_response =  create_ecs_service(service_name, task_name, subnets, security_group_id, target_group_arn)


# code_build_repository = 'DakobedCodeBuildRepository'
# artifacts_bucket = 'dakobed-cicid-artifacts'
# project_name = 'dakobed-service-code-commit-project'
# cluster_name = 'DakobedCluster'
# response = create_code_build_repository(code_build_repository)
#
# create_code_commit_project(project_name, stack['codebuildrole'] , stack['accountID'])
#
# create_code_pipeline('DakobedCodePipeline',stack['codepipelinerole'],artifacts_bucket,code_build_repository,project_name, cluster_name,service_name)