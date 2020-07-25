# Dakobed Serverless API

In this directory I define the serverless API that is used by my front end web application.

Make a get request to this endpoint 

https://qesg5zrff2.execute-api.us-west-2.amazonaws.com


curl -X OPTIONS -H "Access-Control-Request-Method: GET" \
     -H "Access-Control-Request-Headers: Content-Type" \
     -H "Origin: http://example.com" --verbose https://qesg5zrff2.execute-api.us-west-2.amazonaws.com/v1/guitarset

