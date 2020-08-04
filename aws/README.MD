### Dakobed AWS services

This directory contains all of the services for interacting with AWS.  


##### Build the container
sam build --use-container

##### Start the API on http://127.0.0.1:3000
sam local start-api -t template.yaml

##### Make a get request to the API & the /click route

curl http://127.0.0.1:3000 /click

sam package --template-file ./real-time-streaming.yml --output-template-file ./transformed-streaming.yml --s3-bucket sam-s3-lambda

aws cloudformation deploy --template-file transformed-streaming.yml --stack-name DakobedStreamingStack --capabilities CAPABILITY_IAM


aws codecommit create-repository --repository-name dakobedstreamingrepository