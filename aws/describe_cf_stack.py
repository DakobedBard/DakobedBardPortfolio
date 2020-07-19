import json
import boto3

def cloudformation_stack_output():

    client = boto3.client('cloudformation')
    outputs = client.describe_stacks(StackName='DakobedBardStack')['Stacks'][0]['Outputs']
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
    return stack