from airflow import DAG
from datetime import datetime, timedelta
from airflow.models import BaseOperator
from elasticsearch import Elasticsearch, helpers, exceptions
import logging


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


def process_tweets_index(resp):
    tweets = []
    for tweet in resp:
        tweets.append({'content': tweet[''] })


class DeleteItemsElasticSearchIndexOperator(BaseOperator):
    def execute(self, context):
        host = "localhost:29200"
        es = Elasticsearch(host)
        es.delete_by_query(index="tweets", body={"query": {"match_all": {}}})


class ScanElasticSearchIndexOperator(BaseOperator):
    def execute(self, context):
        host = "localhost:29200"
        es = Elasticsearch(host)
        LOG_FILENAME = '/home/mddarr/data/log/tweets.log'
        logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
        tweets = scan_tweets_index()
        logging.info(len(tweets))



class WriteToParquetOperator(BaseOperator):
    def execute(self, context):
        pass


default_args = {
    'owner': 'mddarr',
    'start_date': datetime(2020, 3, 1),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': False
}


tweets_pipeline_dag = DAG('tweets_dag',
          default_args=default_args,
          description='Airflow DAG',
          schedule_interval='0 * * * *',
          catchup = False
         )

stage_tweets_parquet = ScanElasticSearchIndexOperator(
    task_id='scan_tweets_index_task',
    dag=tweets_pipeline_dag,
)
