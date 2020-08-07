import findspark
findspark.init()
import pyspark as ps
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import os
import json


if (__name__ == "__main__"):
    sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 60)
    kafkaStream = KafkaUtils.createStream(ssc, 'cdh57-01-node-01.moffatt.me:2181', 'spark-streaming',
                                          {'kafka-tweets': 1})






