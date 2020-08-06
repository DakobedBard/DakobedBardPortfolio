from elasticsearch import Elasticsearch
host = "localhost:29200"
es = Elasticsearch(host)
es.delete_by_query(index="tweets", body={"query": {"match_all": {}}})
