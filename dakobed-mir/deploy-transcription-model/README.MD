
# Deploy the Keras model with Lambda & API Gateway

sam package --template-file ./template.yaml --output-template-file ./deploy-lambda-keras.yml --s3-bucket dakobed-deploy-lambda-keras

aws cloudformation deploy --template-file ./deploy-lambda-keras.yml  --stack-name DakobedKerasDeployStack --capabilities CAPABILITY_IAM
