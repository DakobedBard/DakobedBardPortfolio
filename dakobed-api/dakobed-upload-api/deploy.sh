#!/bin/sh

# IMPORTANT: Bucket names must be unique for all AWS users.
BUCKET="dakobed-serverless-pipeline"

# Uploads files to S3 bucket and creates CloudFormation template
sam package \
    --template-file upload_template.yaml \
    --s3-bucket $BUCKET \
    --output-template-file upload_package.yaml

## Deploys your stack
sam deploy \
    --template-file upload_package.yaml \
    --stack-name DakobedTranscriptionStack \
    --capabilities CAPABILITY_IAM
