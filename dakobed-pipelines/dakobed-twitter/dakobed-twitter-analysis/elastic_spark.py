from getSparkSession import getSparkInstance
from elasticsearch_connection import connect_elasticsearch



import requests

# this will search for car documents with a 'make' of 'Honda':


client = connect_elasticsearch()


tweets_es_query = {
    'query': {
        'match_all': {

        }
    }
}

# print ('\n', number of hits:', len(response_hits))

response = client.search(index="tweets", body=tweets_es_query)
hits = response['hits']
response_hits = response['hits']['hits']
print ('number of hits:  {}'.format(len(response_hits)))


#
#
# spark = getSparkInstance()