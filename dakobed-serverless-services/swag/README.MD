Try to use a Swagger API definition 



sam package --template-file ./template.yaml --output-template-file ./outpute-template.yml --s3-bucket dakobed-deploy-lambda-keras

aws cloudformation deploy --template-file ./outpute-template.yml  --stack-name DakobedKerasDeployStack --capabilities CAPABILITY_IAM --parameter-overrides S3BucketName=dakobed-serverless-pipeline StageName=dakobed-stage