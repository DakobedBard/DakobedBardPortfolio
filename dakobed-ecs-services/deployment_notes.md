
## Deployment notes

## Create ECR Repository
aws ecr create-repository --repository-name dakobed/services


## Create Stack

aws cloudformation create-stack --stack-name DakobedStack --capabilities CAPABILITY_NAMED_IAM --template-body file://aws/stack.yml   
aws cloudformation describe-stacks --stack-name DakobedStack > aws/output/cloudformation-output.json


## Create cluster
aws cloudformation wait stack-create-complete --stack-name DakobedStack && echo "stack created"
aws ecs create-cluster --cluster-name DakobedServiceCluster

## Create LOG GROUP
aws logs create-log-group --log-group-name dakobedservice-logs


## Register task def

aws ecs register-task-definition --cli-input-json file://aws/task-definition.json


## Create a load balancer, rpelace subnet IDS
aws elbv2 create-load-balancer --name dakobed-nlb --scheme internet-facing --type network --subnets subnet-091665b9f5b0471a1 subnet-0db4836bae277c72a  > nlb-output.json

## Create a LB target group, replace the VPC ID w/ your VPC ID
aws elbv2 create-target-group --name DakobedService-TargetGroup --port 8080 --protocol TCP --target-type ip --vpc-id vpc-1800e660 --health-check-interval-seconds 10 --health-check-path / --health-check-protocol HTTP --healthy-threshold-count 3 --unhealthy-threshold-count 3 > opn

## Create a load balancer listener, replacing ARNs for the LB target group and the NLB

aws elbv2 create-listener --default-actions TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:710339184759:targetgroup/DakobedService-TargetGroup/880b919a5694b85a,Type=forward --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:710339184759:loadbalancer/net/dakobed-nlb/8da0b69cbdc6185f --port 80 --protocol TCP


## Create the service specifying the service name, the cluster name, the subnet IDS, the security group ID, the task definition name & the container name.  Also specify the Load balancer target group ARN
aws ecs create-service --cli-input-json file://service-definition.json


docker build -t dakobed-service .






### Create an API gateway VPC link
Perform request authorization before our NLB receives any requests.  Perform this with API Gateway

API Gateway VPC Link that enables API Gateway APIS to directly integrate with backend web services that are privately hosted 
inside a VPC.  


aws apigateway create-vpc-link --name DakobedVPCLink --target-arns arn:aws:elasticloadbalancing:us-west-2:710339184759:loadbalancer/net/dakobed-nlb/7d375feef50c5df0 > aws/output/api-gateway-link-output.json



### Modify the api-swagger.json file to reflect the VPC ID & the NLB DNS 
aws apigateway import-rest-api --parameters endpointConfigurationTypes=REGIONAL --body file://aws/api-swagger.json --fail-on-warnings
