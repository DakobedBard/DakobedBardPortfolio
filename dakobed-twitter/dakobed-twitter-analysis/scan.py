#!/usr/bin/env python3
from elasticsearch import Elasticsearch, helpers, exceptions
import json

host ="localhost:29200"
client = Elasticsearch( host )


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

    print ('scroll() query length:', len(resp))

    scroll_id = resp['_scroll_id']
    resp = helpers.scan(
        client,
        scroll = '3m',
        size = 10,
    )
    print ('nscan() scroll length:', len( list( resp ) ))
    for num, doc in enumerate(resp):
        print ('\n', num, '', doc)

scan_tweets_index()


def delete_all_items_from_tweets_index():
    host = "localhost:29200"
    es = Elasticsearch(host)
    es.delete_by_query(index="tweets", body={"query": {"match_all": {}}})

delete_all_items_from_tweets_index()

