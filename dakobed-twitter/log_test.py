import logging
from elasticsearch import Elasticsearch, helpers, exceptions

LOG_FILENAME = '/var/log/tweets.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)


def scan_tweets_index():
    host = "localhost:29200"
    client = Elasticsearch(host)
    search_body = {
        "size": 10000,
        "query": {
            "match_all": {}
        }
    }
    resp = client.search(
        index="tweets",
        body=search_body,
        scroll='3m',  # time value for search
    )
    scroll_id = resp['_scroll_id']
    resp = client.scroll(
        scroll_id = scroll_id,
        scroll = '1s', # time value for search
    )
    resp = helpers.scan(
        client,
        scroll = '3m',
        size = 10,
    )
    return list(resp)
resp = scan_tweets_index()
logging.info(len(resp))