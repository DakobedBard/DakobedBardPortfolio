import boto3

cloud_formation_client = boto3.client('cloudformation')

with open('stack.yml', 'r') as cf_file:
    cft_template = cf_file.read()
    cloud_formation_client.create_stack(StackName='DakobedStack', TemplateBody=cft_template, Capabilities=['CAPABILITY_NAMED_IAM'])
waiter =cloud_formation_client.get_waiter('stack_create_complete')
print("...waiting for stack to be ready...")
waiter.wait(StackName='DakobedStack')
