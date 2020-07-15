
### Create an API gateway VPC link
Perform request authorization before our NLB receives any requests.  Perform this with API Gateway

API Gateway VPC Link that enables API Gateway APIS to directly integrate with backend web services that are privately hosted 
inside a VPC.  


aws apigateway create-vpc-link --name DakobedVPCLink --target-arns arn:aws:elasticloadbalancing:us-west-2:710339184759:loadbalancer/net/dakobed-nlb/7d375feef50c5df0 > aws/output/api-gateway-link-output.json



### Modify the api-swagger.json file to reflect the VPC ID & the NLB DNS 
aws apigateway import-rest-api --parameters endpointConfigurationTypes=REGIONAL --body file://aws/api-swagger.json --fail-on-warnings
