# Dakobed Spring Application

This directory contains the Spring Boot application that has been launched to AWS elastic container service.  To minimize 
the costs of deployment for a low traffic API, I have chosen an monolothic architecture.  

In the AWS folder are the within this directory are the boto3 scripts for launching the CloudFormation stack, as well
as ECS task & service.  


  
[Elastic Container Service Deployment](dakobed-aws/README.MD)
- Perform neural style tranfer using Keras
- Train network on EC2 GPU isntances
  
## Snotel Data Service

##### Query all locations
curl --request GET localhost:8080/locations | jq


## Tweets Query service
The API endpoints in this domain allow for querying of tweets using the Elastic Search high level REST client. 

##### Query all tweets in ES
curl --request GET localhost:8080/tweets | jq

## Transcription Music Service

##### Query the guitarset training examples 
curl --request GET localhost:8080/guitarset | jq

