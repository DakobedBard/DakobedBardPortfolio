### Dakobed Twitter Pipeline

I had to use a different maven plugin for this, use the jar-with-dependices.jar instead of the other.  Pass
the hostname & the port of the elasticsearch endpoint.  Will use http for localhost, otherwise will use https

java -jar target/dakobed-twitter-producer-1.0-SNAPSHOT-jar-with-dependencies.jar localhost 29200



### dakobed-twitter-producer

Multithreaded Java application which ingests tweets using the twitter4j library and adds them to an array blocking queue
in on thread which are produced to an ElasticSearch index in the other thread.  


### dakobed-twitter-service


AWS ElasticSearch Service

Verify that the ES cluster is healthy -> replacing the ES DNS  

curl -u 'master-user:1!Master-user-password'  'https://search-dakobedes-o5fqopyonjvcuzkvpeyoezfgey.us-west-2.es.amazonaws.com/_cat/health?v'
curl -u 'master-user:1!Master-user-password'  'https://search-dakobedes-o5fqopyonjvcuzkvpeyoezfgey.us-west-2.es.amazonaws.com/_aliases'

