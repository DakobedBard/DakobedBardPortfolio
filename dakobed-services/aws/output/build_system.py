import boto3
#
# s3_client = boto3.client('s3')
# s3_client.create_bucket(Bucket='dakobed-services-artifacts-bucket')


code_commit_client = boto3.client('codecommit')

response = code_commit_client.create_repository(
    repositoryName='BotoDakobedRepository'
)
code_build_client = boto3.client('codebuild')
