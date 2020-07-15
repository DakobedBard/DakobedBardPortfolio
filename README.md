# DakobedBard

This repository contains my software/data/cloud engineering portfolio.  This project has been deployed to AWS as a 
static website hosted on S3, with a containerized API service deployoyed to AWS elastic container service fargate instances.  



aws ecr create-repository --repository-name dakobedbard/service
docker build -t dakobedbard/service .



