import boto3
import os
import findspark
findspark.init()
import pyspark as ps
import json


def load_snotel_dataframe_from_json(spark, location, year):
    df = spark.read.json(os.getcwd() + '/data/snotel/{}/{}.json'.format(location, year))
    return df


def concatenate_snotel_datafames(spark, locations, years):
    # This function concatenates individual dataframes into a single dataframe.  Specify the locations and years of
    # the dataframes to add to the single dataframe
    dataframes = []
    for location in locations:
        for year in years:
            dataframes.append(load_snotel_dataframe_from_json(spark, location,year))
    df = dataframes[0]
    for dataf in dataframes[1:]:
        df = df.union(dataf)
    return df


def write_snotel_data_json(data, location, year):
    with open('data/snotel/{}/{}.json'.format(location,year), "w") as f:
        json.dump(data, f)


def count_missing_data(spark, locations, dataframe):
    dataframe.createOrReplaceTempView('snotel')
    for location in locations:
        snotelQuery = spark.sql(
            "SELECT LocationID, SnotelDate, SnowPctMedian FROM snotel WHERE LocationID ='{}' and SnowCurrent=0".format(
                location))
        print("The number of measurements that are missing at {} is {}".format(location, snotelQuery.count()))


java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
os.environ['JAVA_HOME'] = java8_location

spark = ps.sql.SparkSession.builder \
    .master("local[4]") \
    .appName("individual") \
    .getOrCreate()
sc = spark.sparkContext
bucket = 'dakobed-snotel-analysis'

locations = ['Lyman Lake' ]


df = concatenate_snotel_datafames(spark, locations, ['2014','2015','2016','2017', '2018', '2019'])
df.createOrReplaceTempView('snotel')
lyman_lake_pct_median = spark.sql( "SELECT SnotelDate, SnowCurrent, SnowMedian, SnowCurrent/SnowMedian as pctMedian  FROM snotel WHERE LocationID ='{}' and SnotelDate between 20150601 and 20150716".format('Lyman Lake'))



# print("The number of measurements that are missing at {} is {}".format(location, snotelQuery.count()))


import pyspark.sql.functions as F


