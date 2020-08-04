# Dakobed Orders Microservice

This projct consits of several microservices which communicate with one another with the Spring Kafka Streams binder.  I have not fully implemented the Kafka code into this porfolio.  Eventually I will merge the code from my KafkaServices repository https://github.com/MathiasDarr/KafkaServices into this one.  

This spring boot microservice has endpoints for managing orders to an ECommerce event driven system.  Currently there is an orders and a products microservice, both utilizing DynamoDB as a backend.  


#### Query all orders from  customer w/ ID
curl localhost:8080/customer-orders?id=jerry@gmail.com | jq

#### Query all orders from customer w/ ID having been placed after date

localhost:8080/detail?id=jerry@gmail.com&date=20170603-25875 | jq


