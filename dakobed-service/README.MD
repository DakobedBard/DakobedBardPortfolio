

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




## 
Register task def

aws ecs register-task-definition --cli-input-json file://task-definition.json





docker build -t dakobed-service .

docker run -p 8080:8080 dakobed-service


{
  "family": "dakobedservicev3",
  "cpu": "256",
  "memory": "512",
  "networkMode": "awsvpc",
  "requiresCompatibilities": [
    "FARGATE"
  ],
  "executionRoleArn": "arn:aws:iam::710339184759:role/ecsTaskExecutionRole",
  "taskRoleArn": "arn:aws:iam::710339184759:role/dakobed-ecs-dynamo-role",
  "containerDefinitions": [
    {
      "name": "Dakobed-Service",
      "image": "710339184759.dkr.ecr.us-west-2.amazonaws.com/dakobedbard/service:latest",
      "portMappings": [
        {
          "containerPort": 8080,
          "protocol": "http"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "dakobedservice-logs",
          "awslogs-region": "us-west-2",
          "awslogs-stream-prefix": "awslogs-dakobedservice-logs"
        }
      },
      "essential": true
    }
  ]
}
