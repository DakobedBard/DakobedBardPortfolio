## Dakobed Stack Deployment Notes

Utilize Cloudformation to provision resources


aws cloudformation create-stack --stack-name DakobedStack --capabilities CAPABILITY_NAMED_IAM \
--template-body file://core.yml   

aws cloudformation describe-stacks --stack-name DakobedStack

To save the IDS of resources by cloud formation to a file 

aws cloudformation describe-stacks --stack-name DakobedStack > ./core-output.json


##### Create ECS Cluster

aws ecs create-cluster --cluster-name Dakobed-Fargate-Cluster

###### Dakobed Logs
aws logs create-log-group --log-group-name dakobed-logs

##### Register a task
aws ecs register-task-definition --cli-input-json file://snotel-task-definition.json


##### Application Load Balancer
aws elbv2 create-load-balancer --name dakobed-network-load-balancer --scheme internet-facing --type application --subnets subnet-0ec15e101c2157a2c subnet-0abd5728cc4e12536 > ~/nlb-output.json

aws elbv2 create-target-group --name dakobed-target-group --port 8080 --protocol HTTP --target-type ip \
 --vpc-id vpc-08cf10763c590a599 --health-check-interval-seconds 10 --health-check-path / --health-check-protocol HTTP \
 --healthy-threshold-count 3 --unhealthy-threshold-count 3 > opn

aws elbv2 create-listener --default-actions TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:710339184759:targetgroup/dakobed-target-group/ce547bce55a8f946,Type=forward \
--load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:710339184759:loadbalancer/app/dakobed-network-load-balancer/7e5ac30cf13d5418 \
--port 80 --protocol HTTP



subnet-08ac233e419041d0c
subnet-0cd3f685699d157ee



##### Application Load Balancer
aws elbv2 create-load-balancer --name dakobed-application-lb --scheme internet-facing --type application \
 --subnets subnet-08ac233e419041d0c subnet-0cd3f685699d157ee   > ./alb-output.json


arn:aws:elasticloadbalancing:us-west-2:710339184759:loadbalancer/app/dakobed-application-lb/3ae376999a3a0106

##### Create a Load Balancer Target Group



aws elbv2 create-target-group --name dakobed-targetgroup --port 8080 --protocol TCP --target-type ip --vpc-id \
 vpc-08cf10763c590a599 --health-check-interval-seconds 10 --health-check-path / --health-check-protocol HTTP --healthy-threshold-count 3 --unhealthy-threshold-count 3 > opn >/tg-output.json

##### Create a load balancer listener
aws elbv2 create-listener --default-actions TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:710339184759:targetgroup/dakobed-targetgroup/80c5ef293a3ac23a,Type=forward \
 --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:710339184759:loadbalancer/app/dakobed-application-lb/bc0762f66e6a9535 --port 80 --protocol HTTP



 
 #### Create a listener for APPLICATION LOAD BALANCER
 aws elbv2 create-listener --default-actions TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:710339184759:targetgroup/dakobed-targetgroup/80c5ef293a3ac23a,Type=forward \
  --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:710339184759:loadbalancer/app/dakobed-application-lb/bc0762f66e6a9535 --port 80 --protocol HTTP
 
##### Create Service
aws ecs create-service --cli-input-json file://snotel-service-definition.json
