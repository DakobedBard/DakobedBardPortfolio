#!/bin/sh

# IMPORTANT: Bucket names must be unique for all AWS users.
BUCKET="dakobed-serverless-api"

# Uploads files to S3 bucket and creates CloudFormation template
sam package \
    --template-file template.yaml \
    --s3-bucket "dakobed-serverless-api"\
    --output-template-file package.yaml

# Deploys your stack
sam deploy \
    --template-file package.yaml \
    --stack-name DakobedServerlessApiStack \
    --capabilities CAPABILITY_IAM
