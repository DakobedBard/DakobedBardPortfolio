

## Create ECR Repository
aws ecr create-repository --repository-name dakobed/service


## Create Stack


aws cloudformation create-stack --stack-name DakobedStack --capabilities CAPABILITY_NAMED_IAM --template-body file://core.yml   
aws cloudformation describe-stacks --stack-name DakobedStack > cloudformation-core-output.json


## Create cluster

aws cloudformation wait stack-create-complete --stack-name DakobedStack && echo "stack created"
aws ecs create-cluster --cluster-name DakobedServiceCluster


## Create LOG GROUP
aws logs create-log-group --log-group-name dakobedservice-logs


## Register task definition specifying the task name, the task role and the execution role

aws ecs register-task-definition --cli-input-json file://task-definition.json


## Create a load balancer, rpelace subnet IDS

aws elbv2 create-load-balancer --name dakobed-nlb --scheme internet-facing --type network --subnets subnet-02c6411185d162cc9  subnet-09f9aeabcd99b761f > nlb-output.json

## Create a LB target group, replace the VPC ID w/ your VPC ID
aws elbv2 create-target-group --name DakobedService-TargetGroup --port 8080 --protocol TCP --target-type ip --vpc-id vpc-0600c7c4476f4982d --health-check-interval-seconds 10 --health-check-path / --health-check-protocol HTTP --healthy-threshold-count 3 --unhealthy-threshold-count 3 > opn.json


## Create a load balancer listener, replacing ARNs for the LB target group and the NLB

aws elbv2 create-listener --default-actions TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:710339184759:targetgroup/DakobedService-TargetGroup/2221998324380b6f,Type=forward --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:710339184759:loadbalancer/net/dakobed-nlb/90a9a986800b0c3e --port 80 --protocol TCP


## Create the service specifying the service name, the cluster name, the subnet IDS, the security group ID, the task definition name & the container name.  Also specify the Load balancer target group ARN
aws ecs create-service --cli-input-json file://service-definition.json


## Test the load balancer 

http://dakobed-nlb-8da0b69cbdc6185f.elb.us-west-2.amazonaws.com/guitarset


docker build -t dakobed-service .


AWS CODE SERVICES

aws s3 mb s3://dakobed-bard-artifacts

