# Dakobed Serverless API

In this directory I define the serverless API that is used by my front end web application.

Make a get request to this endpoint 

sam package \
    --template-file template.yaml \
    --s3-bucket "dakobed-serverless-api"\
    --output-template-file package.yaml

sam deploy \
    --template-file package.yaml \
    --stack-name DakobedServerlessApiStack \
    --capabilities CAPABILITY_IAM

aws cloudformation deploy \
    --template-file ./package.yaml  \
    --stack-name DakobedApiServerlessStack \
    --capabilities CAPABILITY_IAM



https://qesg5zrff2.execute-api.us-west-2.amazonaws.com


curl -X OPTIONS -H "Access-Control-Request-Method: GET" \
     -H "Access-Control-Request-Headers: Content-Type" \
     -H "Origin: http://example.com" --verbose https://ie684ksl4b.execute-api.us-west-2.amazonaws.com/v2/guitarset

