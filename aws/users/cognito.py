import boto3

cognito_id_provider_client = boto3.client('cognito-idp')
cognito_id_provider_client.create_user_pool(PoolName='DakobedUserPool',AutoVerifiedAttributes=['email'])

user_pool_id = 'us-west-2_rrVhZsufQ'
user_pool_arn = 'arn:aws:cognito-idp:us-west-2:710339184759:userpool/us-west-2_rrVhZsufQ'



cognito_id_provider_client.create_user_pool_client(UserPoolId=user_pool_id,ClientName='DakobedUserPoolClient')