# DakobedBard


aws ecr create-repository --repository-name dakobedbard/service
docker build -t dakobedbard/service .


### Twitter Pipeline


### dakobed-twitter-producer

Multithreaded Java application which ingests tweets using the twitter4j library and adds them to an array blocking queue
in on thread which are produced to an ElasticSearch index in the other thread.  


### dakobed-twitter-service

Spring Boot API allows for queries on the tweets in ElasticSearch.  


AWS ElasticSearch Service

Verify that the ES cluster is healthy -> replacing the ES DNS  

curl -u 'master-user:1!Master-user-password'  'https://search-dakobedes-o5fqopyonjvcuzkvpeyoezfgey.us-west-2.es.amazonaws.com/_cat/health?v'
curl -u 'master-user:1!Master-user-password'  'https://search-dakobedes-o5fqopyonjvcuzkvpeyoezfgey.us-west-2.es.amazonaws.com/_aliases'


curl -u 'master-user:1!Master-user-password'  'https://search-dakobedes-o5fqopyonjvcuzkvpeyoezfgey.us-west-2.es.amazonaws.com/_aliases'

