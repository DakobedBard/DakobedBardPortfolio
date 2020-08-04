import boto3
import json
from .aws_utils import create_application_load_balancer_listener, create_network_load_balancer, create_ecs_service, \
    create_target_group, create_security_group, create_application_load_balancer, create_network_load_balancer_listener, \
    register_ecs_task, delete_ecs_service, delete_target_group, delete_load_balancer


with open('output/stack_output.json') as f:
  data = json.load(f)

outputs = data['Stacks'][0]['Outputs']

stack = {}
stack['accountID'] = outputs[0]['OutputValue']
stack['securitygroupID'] = outputs[1]['OutputValue']
stack['publicsubnet1'] = outputs[2]['OutputValue']
stack['ecstaskrole'] = outputs[3]['OutputValue']
stack['region'] = outputs[4]['OutputValue']
stack['vpcID'] = outputs[5]['OutputValue']
stack['ecsservicerole'] = outputs[6]['OutputValue']
stack['privatesubnet1'] = outputs[7]['OutputValue']

