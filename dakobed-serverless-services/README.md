### Dakobed Serverless Services

This directory contains a SAM application for the Snotel Service querying DynamoDB.

sam package --template-file ./template.yaml --output-template-file ./snotel-template.yml --s3-bucket dakobed-deploy-lambda-keras

aws cloudformation deploy --template-file ./snotel-template.yml  --stack-name DakobedServerlessStack --capabilities CAPABILITY_IAM