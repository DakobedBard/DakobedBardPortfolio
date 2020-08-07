import findspark
findspark.init()
import pyspark as ps
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import os
import json




def getSparkInstance():
    """
    @return: Return Spark session
    """
    java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
    os.environ['JAVA_HOME'] = java8_location
    spark = ps.sql.SparkSession.builder \
        .config() \
        .master("local[4]") \
        .appName("individual") \
        .getOrCreate()
    return spark


conf = SparkConf().set("spark.jars", "/home/mddarr/data/DalinarSoftware/spark-2.4.5-bin-hadoop2.7/jars/spark-streaming-kafka-0-10-assembly_2.11-2.4.6.jar")
sc = SparkContext(conf = conf)
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 60)
kafkaStream = KafkaUtils.createStream(ssc, 'cdh57-01-node-01.moffatt.me:2181', 'spark-streaming', {'kafka-tweets':1})

