
sam package --template-file ./template.yaml --output-template-file ./output-template.yml --s3-bucket dakobed-serverless-pipeline

aws cloudformation deploy --template-file ./output-template.yml  --stack-name DakobedApiServerlessStack --capabilities CAPABILITY_IAM


curl -X OPTIONS -H "Access-Control-Request-Method: POST" \
     -H "Access-Control-Request-Headers: Content-Type" \
     -H "Origin: http://example.com" --verbose <endpoint>