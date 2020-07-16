### AWS Deployment

security groups are not supported with network load balancer for some reason..


aws cloudformation create-stack --stack-name DakobedStack --capabilities CAPABILITY_NAMED_IAM --template-body file://stack.yml   

aws cloudformation describe-stacks --stack-name DakobedStack > output/cloudformation-output.json


#### Load balancer targete group

aws elbv2 create-target-group --name DakobedService-TargetGroup --port 8080 --protocol TCP --target-type ip --vpc-id vpc-1800e660 --health-check-interval-seconds 10 --health-check-path / --health-check-protocol HTTP --healthy-threshold-count 3 --unhealthy-threshold-count 3 > opn


