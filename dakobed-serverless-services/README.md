### Dakobed Serverless Services

This directory contains a SAM application for the Snotel Service querying DynamoDB.

sam package --template-file ./template.yaml --output-template-file ./snotel-template.yml --s3-bucket dakobed-deploy-lambda-keras

aws cloudformation deploy --template-file ./snotel-template.yml  --stack-name DakobedServerlessStack --capabilities CAPABILITY_IAM

location=Trinity&sdate=20140101&edate=20140104


"querystring": "$input.params().querystring"




Testing Cors

curl -v -X OPTIONS https://vzmta1umza.execute-api.us-west-2.amazonaws.com/v1

curl --request POST  -H "Content-Type: application/audio" --data-binary aa.jpg https://vzmta1umza.execute-api.us-west-2.amazonaws.com/v1/upload