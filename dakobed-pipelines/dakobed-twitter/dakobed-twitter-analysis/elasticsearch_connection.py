from elasticsearch import Elasticsearch
def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 29200}])
    if _es.ping():
        print('Connected')
    else:
        print('Could not connect')
    return _es
