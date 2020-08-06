from airflow import DAG
from datetime import datetime, timedelta
from airflow.models import BaseOperator
from airflow.operators.python_operator import PythonOperator
from elasticsearch import Elasticsearch, helpers, exceptions
import logging
import boto3

import findspark
findspark.init()
import pyspark as ps
import os
import datetime

def getSparkInstance():
    java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
    os.environ['JAVA_HOME'] = java8_location

    spark = ps.sql.SparkSession.builder \
        .master("local[4]") \
        .appName("individual") \
        .getOrCreate()
    return spark


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
        tweets_scan = scan_tweets_index()
        tweets = [tweet['_source'] for tweet in tweets_scan ]
        spark = getSparkInstance()
        sc = spark.sparkContext
        df = spark.read.json(sc.parallelize(tweets))
        df.repartition(1).write.mode('overwrite').parquet('tmp/pyspark_us_presidents')


def deleteElasticSearchTweets():
    host = "localhost:29200"
    es = Elasticsearch(host)
    es.delete_by_query(index="tweets", body={"query": {"match_all": {}}})


def generate_directory_name():
    current_time = datetime.datetime.now()
    month = current_time.month
    hour = current_time.hour
    day = current_time.day
    return 'tmp/{}/{}/{}'.format(month, day, hour)


def scanElasticSearchTweets():
    tweets_scan = scan_tweets_index()
    tweets = [tweet['_source'] for tweet in tweets_scan]
    spark = getSparkInstance()
    sc = spark.sparkContext
    df = spark.read.json(sc.parallelize(tweets))
    directory_name = generate_directory_name()
    s3 = boto3.client('s3')
    df.repartition(1).write.mode('overwrite').parquet(directory_name)
    with open(directory_name, "rb") as f:
        s3.upload_fileobj(f, "dakobed-tweets", directory_name)
    os.rmdir(directory_name)



class WriteParquetOperator(BaseOperator):
    def execute(self, context):
        spark = getSparkInstance()

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

scan_tweets = PythonOperator(
    task_id='scan_elastic_tweets',
    dag=tweets_pipeline_dag,
    python_callable=scanElasticSearchTweets,
)
delete_tweets = PythonOperator(
    task_id='delete_elastic_tweets',
    dag=tweets_pipeline_dag,
    python_callable=deleteElasticSearchTweets,
)

