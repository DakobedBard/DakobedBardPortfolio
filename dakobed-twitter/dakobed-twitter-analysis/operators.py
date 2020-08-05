import logging
from airflow.models import BaseOperator
from elasticsearch import Elasticsearch, helpers, exceptions



class DeleteItemsElasticSearchIndexOperator(BaseOperator):
    def execute(self, context):
        host = "localhost:29200"
        es = Elasticsearch(host)
        es.delete_by_query(index="tweets", body={"query": {"match_all": {}}})

