from elasticsearch_connection import connect_elasticsearch
from elasticsearch import Elasticsearch, helpers, exceptions
client = connect_elasticsearch()

tweets_es_query = {
    'query': {
        'match_all': {
        }
    }
}

es=Elasticsearch([{'host':'localhost','port':'29200','timeout':60}])
res = es.count(index='tweets', doc_type='your doc_type', body=tweets_es_query)["count"]

results = client.helpers.scan(es,
    index="tweets",
    doc_type="my_document",
    preserve_order=True,
    query={"query": {"match_all": {}}},
)

for item in results:
    print(item['_id'], item['_source']['name'])

search_body = {
    "size": 1000,
    "query": {
        "match_all": {}
    }
}

resp = client.search(
    index="tweets",
    body=search_body,
    scroll='3m',  # time value for search
)

# get the number of docs with len()
print("total docs:", len(resp["hits"]["hits"]))

scroll_id = resp['_scroll_id']

resp = client.scroll(
    scroll_id=scroll_id,
    scroll='1s',  # time value for search
)

print('scroll() query length:', len(resp))


# call the helpers library's scan() method to scroll
resp = helpers.scan(
    client,
    scroll='3m',
    size=10,
)

# returns a generator object
print(type(resp))

resp = helpers.scan(
    client,
    scroll='3m',
    size=10,
)

# returns a generator object
print(type(resp))

print('\nscan() scroll length:', len(list(resp)))


for num, doc in enumerate(resp):
    print('\n', num, '', doc)



# print ('\n', number of hits:', len(response_hits))

# response = client.search(index="tweets", body=tweets_es_query)
# hits = response['hits']
# print ('number of hits:  {}'.format(len(hits)))
# response_hits = response['hits']['hits']
# print ('number of hits:  {}'.format(len(response_hits)))
#

