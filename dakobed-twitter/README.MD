### Twitter Pipeline


### dakobed-twitter-producer

Multithreaded Java application which ingests tweets using the twitter4j library and adds them to an array blocking queue
in on thread which are produced to an ElasticSearch index in the other thread.  


### dakobed-twitter-service

Spring Boot API allows for queries on the tweets in ElasticSearch.  