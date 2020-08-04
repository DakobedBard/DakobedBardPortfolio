python3 styletransfer.py img/bulb.png    img/style.jpg results/my_result

docker build . -t dakobed:style
docker run  dakobed:style 


docker build . -t dakobed:style
docker run  dakobed:style python

serverless create --template aws-python3  --name numpy-test  --path numpy-test



serverless invoke --function numpy --stage dev --region us-west-2




import boto3
def handler(event,context):
  client = boto3.client('ecs')
  response = client.run_task(
  cluster='dakobed-style-cluster', # name of the cluster
  launchType = 'FARGATE',
  taskDefinition='style-task:1', # replace with your task definition name and revision
  count = 1,
  platformVersion='LATEST',
  networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                'subnet-5db0fb07', # replace with your public subnet or a private with NAT
            ],
            'assignPublicIp': 'DISABLED'
        }
    })
  return str(response)


ECR COMMANDS 

aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 710339184759.dkr.ecr.us-west-2.amazonaws.com

docker build -t dakobed-style .

docker tag dakobed-style:latest 710339184759.dkr.ecr.us-west-2.amazonaws.com/dakobed-style:latest

docker push 710339184759.dkr.ecr.us-west-2.amazonaws.com/dakobed-style:latest