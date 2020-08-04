import boto3
import json


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
                    'actions': [
                        {
                            'name': 'Source',
                            'runOrder': 1,
                            'actionTypeId': {
                                'category': 'Source' ,
                                'owner': 'AWS' ,
                                'provider': 'CodeCommit',
                                'version': '1'
                            },
                            'configuration': {
                                "BranchName": "master",
                                "RepositoryName": repository_name
                            },
                            'outputArtifacts': [
                                {
                                    'name': 'DakobedService-SourceArtifact'
                                },
                            ],

                        },
                    ]
                },
                {
                    'name': 'Build',

                    'actions': [
                        {
                            'name': 'Build',
                            'actionTypeId': {
                                'category': 'Build',
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
                                    'name': 'DakobedService-BuildArtifact'
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
                    'actions': [
                        {
                            'name': 'Deploy',
                            'actionTypeId': {
                                'category': 'Deploy',
                                'owner': 'AWS',
                                'provider': 'ECS',
                                'version': '1'
                            },

                            'configuration': {
                                "ClusterName":cluster_name,
                                "ServiceName": service_name,
                                "FileName": "imagedefinitions.json"
                            },

                            'inputArtifacts': [{'name':'DakobedService-BuildArtifact'}],
                        },
                    ]
                },
            ],
            'version': 123
        },
    )


def create_code_build_project(project_name, service_role, account_id):
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

def update_repository_policy():
    client = boto3.client('ecr')
    with open('ecr_policy.json', 'r') as f:
        ecr_policy = f.read()
        client.set_repository_policy(repositoryName='dakobed/services',policyText=ecr_policy)


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


code_build_repository = 'DakobedCodeBuildRepository'
artifacts_bucket = 'dakobed-cicid-artifacts'
project_name = 'dakobed-service-code-commit-project'
cluster_name = 'DakobedCluster'

service_name ='dakobedservice'


# create_repository_response = create_code_build_repository(code_build_repository)
#
# create_code_build_project(project_name, stack['codebuildrole'] , stack['accountID'])

create_code_pipeline('DakobedCodePipeline',stack['codepipelinerole'],artifacts_bucket,code_build_repository,project_name, cluster_name,service_name)
