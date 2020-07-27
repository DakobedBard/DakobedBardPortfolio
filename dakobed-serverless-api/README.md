### Dakobed Serverless API

Test query params.. 
location=Trinity&sdate=20140101&edate=20140102



curl --request POST -H "Content-Type: application/audio"  --data-binary "@/home/mddarr/data/DakobedBard/dakobed-serverless-api/style.jpg" \
    https://nn04nyh2j5.execute-api.us-west-2.amazonaws.com/v1/upload
    



#      responses:
#        200:
#          description: "OK"
#          headers:
#            Access-Control-Allow-Origin:
#              type: string
#            Access-Control-Allow-Methods:
#              type: string
#            Access-Control-Allow-Headers:
#              type: string
#      x-amazon-apigateway-integration:
#        responses:
#          default:
#            statusCode: "200"
#            responseParameters:
#              method.response.header.Access-Control-Allow-Methods: "'DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT'"
#              method.response.header.Access-Control-Allow-Headers: "'Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token'"
#              method.response.header.Access-Control-Allow-Origin: "'*'"
#
#     requestTemplates:
#      application/json: '{"statusCode": 200}'
#     type: mock
