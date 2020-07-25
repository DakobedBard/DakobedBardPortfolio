import boto3
import os
import findspark
findspark.init()
import pyspark as ps
import json
import csv

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('BasinLocations')
locationsDataResponse = table.scan()
locations = locationsDataResponse = table.scan()
['Items']

bucket = 'dakobed-snotel-analysis'

def create_data_folders():
    for location in locations:
        os.mkdir('data/snotel/{}'.format(location['LocationID']))
#create_data_folders()


def query_snotel_table(location, sdate, edate ):
    dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')
    items = []
    try:
        response = dynamodb_client.query(
            TableName='Snotel',
            KeyConditionExpression='LocationID = :LocationID and SnotelDate BETWEEN :sdate and :edate',
            ExpressionAttributeValues={
                ':LocationID': {'S': location},
                ':sdate': {'S': sdate},
                ':edate': {'S': edate}
            }
        )
        items = response['Items']
        output_data = []
        for item in items:
            output_data.append({
                'SnotelDate': str(item['SnotelDate']['S']),
                'WaterCurrentAverage': int(item['WaterCurrentAverage']['N']),
                'WaterPctAverage': int(item['WaterPctAverage']['N']),
                'SnowCurrent': int(item['SnowCurrent']['N']),
                'WaterCurrent': int(item['WaterCurrent']['N']),
                'SnowMedian': int(item['SnowMedian']['N']),
                'SnowPctMedian': int(item['SnowPctMedian']['N']),
                'LocationID': str(item['LocationID']['S'])})

    except Exception as e:
        print(e)
    return output_data


def save_snotel_json_data(data,location, year):
    with open('data/snotel/{}/{}.json'.format(location, year), "w") as f:
        json.dump(data, f)

# data = query_snotel_table('Trinity', '20140101','20141231')

# with open('data/snotel/{}/{}.json'.format('Trinity','2014'), "w") as f:
#     json.dump(data, f)

def load_snotel_dataframe_from_json(spark, location, year):
    df = spark.read.json(os.getcwd() + '/data/snotel/{}/{}.json'.format(location, year))
    return df

def load_snotel_rdd_from_csv(sc, location, year):
    ut = sc.textFile(os.getcwd() + '/data/snotel/{}/{}.csv'.format(location, year))
    return ut


def write_snotel_data_json(data, location, year):
    with open('data/snotel/{}/{}.json'.format(location,year), "w") as f:
        json.dump(data, f)


def write_snotel_data_csv(data,location, year):
    keys = data[0].keys()
    with open('data/snotel/{}/{}.csv'.format(location,year), 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)




java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
os.environ['JAVA_HOME'] = java8_location

spark = ps.sql.SparkSession.builder \
    .master("local[4]") \
    .appName("individual") \
    .getOrCreate()
sc = spark.sparkContext





trinity2014Raw =  query_snotel_table('Trinity','20140101','20141231')

write_snotel_data_json(trinity2014Raw, 'Trinity','2014')

write_snotel_data_csv(trinity2014Raw, 'Trinity','2014')

trinity2014RDD = load_snotel_rdd_from_csv(sc, 'Trinity','2014')
trinity2014DF = load_snotel_dataframe_from_json(spark, 'Trinity','2014')


