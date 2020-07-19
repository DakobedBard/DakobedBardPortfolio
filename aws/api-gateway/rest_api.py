import boto3
from describe_cf_stack import cloudformation_stack_output


# aws apigateway create-vpc-link --name MysfitsApiVpcLink --target-arns REPLACE_ME_NLB_ARN > ~/environment/api-gateway-link-output.json
#stack = cloudformation_stack_output()

# load_balancer_arn = 'arn:aws:elasticloadbalancing:us-west-2:710339184759:loadbalancer/net/dakobedapplicationlb/99944864d2a8ad88'
# gateway_client.create_vpc_link(name='DakobedApiVpcLink',targetArns =[load_balancer_arn] )

gateway_client = boto3.client('apigateway')
with open('dakobed-core-services/api-swagger.json', 'r') as cf_file:
    swagger_file = cf_file.read()
    gateway_client.import_rest_api(
        parameters={'endpointConfigurationTypes':'REGIONAL'},
        failOnWarnings=True,
        body=swagger_file
    )

gateway_id = 'vpmr6r5rb4'
gateway_client.create_deployment(
    stageName='prod',
    restApiId = gateway_id
)

execution_url='https://.execute-api.REPLACE_ME_WITH_REGION.amazonaws.com/prod'