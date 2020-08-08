# DakobedBard

This repository contains my software/data/cloud engineering portfolio.  This project has been deployed to AWS as a 
static website hosted on S3, with a containerized API service deployoyed to AWS elastic container service fargate instances.  

aws ecr create-repository --repository-name dakobedbard/service
docker build -t dakobedbard/service .


[Dakobed Music Information Retrieval](dakobed-mir/README.md)
- Train keras neural networks for making predictions on piano using Maestro dataset & the GuitarSet data audio files
- Train Keras neural network model on EC2 GPU instance
- AWS Serverless Application model for deploying the neural network model

 
[Dakobed Snotel Pipeline](dakobed-snotel/README.MD)
- Scrape USDA snowpack & streamflow data and insert into dynamoDB database.
- Spring boot REST API for querying the data


[Dakobed Virus Tweets Pipeline](dakobed-twitter/README.MD)
- Stream & process tweets about the coronavirus
- Push tweets into Kafka topic using Java & twitter4j library
- Process tweets using Spark Streaming t
- Use kafka connect to push data into elastic search
- Spring API routes for querying tweets in ElasticSearch by location & keywords


[Dakobed Neural Style Transfer](dakobed-style-transfer/README.MD)
- Perform neural style tranfer using Keras
- Train network on EC2 GPU isntances

[Dakobed Elastic Container Service Spring Project](dakobed-ecs-services/README.MD)
- Deploy a Spring Boot API to AWS Elastic Container Service


[Dakobed Spring Microservices Kafka Spring Binder](dakobed-spring-kafka-microservices/README.MD)
- Event driven microservices architecture using Spring Kafka Streams 
- Use AVRO serialization 


[Dakobed Vue Frontend](dakobed-vue/README.MD)
- Frontend website for interacting with the API's provided in other projects
- technologies used: vue, vuetify, vuex, google maps javascript API, D3
- Containerized & run on AWS ECS Fargate instances






