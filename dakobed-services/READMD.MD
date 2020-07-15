# Dakobed Services

This directory contains the Spring Boot application that has been launched to AWS elastic container service.  To minimize 
the costs of deployment for a low traffic API, I have chosen an monolothic architecture.  


  
## Snotel Data Service

##### Query all locations
curl --request GET localhost:8080/locations | jq


## Tweets Query service
The API endpoints in this domain allow for querying of tweets using the Elastic Search high level REST client. 

##### Query all tweets in ES
curl --request GET localhost:8080/tweets | jq

## Transcription Music Service

##### Query the guitarset training examples 
curl --request GET localhost:8080/guitarset | jq

