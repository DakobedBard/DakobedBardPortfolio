### AWS Deployment

security groups are not supported with network load balancer for some reason..


aws cloudformation create-stack --stack-name DakobedStack --capabilities CAPABILITY_NAMED_IAM --template-body file://stack.yml   
aws cloudformation wait stack-create-complete --stack-name DakobedStack && echo "stack created"

aws cloudformation describe-stacks --stack-name DakobedBardStack > output/cloudformation-output.json

#### Load balancer targete group

aws elbv2 create-target-group --name DakobedService-TargetGroup --port 8080 --protocol TCP --target-type ip --vpc-id vpc-1800e660 --health-check-interval-seconds 10 --health-check-path / --health-check-protocol HTTP --healthy-threshold-count 3 --unhealthy-threshold-count 3 > opn


aws s3 mb s3://dakobed-cicid-artifacts

aws s3api put-bucket-policy --bucket dakobed-cicid-artifacts --policy file://artifacts-bucket-policy.json

#### Create code respository

aws codecommit create-repository --repository-name DakobedServiceRepository
aws codebuild create-project --cli-input-json file://code-build-project.json
arn:aws:iam::710339184759:role/DakobedServiceCodeBuildServiceRole

aws codebuild create-project --cli-input-json file://code-build-project.json


#### CI/CD 



SWAGGER

aws apigateway import-rest-api --parameters endpointConfigurationTypes=REGIONAL --body file://api-swagger.json --fail-on-warnings




