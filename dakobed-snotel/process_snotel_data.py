import boto3
import os

import json
import csv


def query_snotel_table(location, sdate, edate ):
    dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')
    output_data = []
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


def write_snotel_data_json(data, location, year):
    with open('data/snotel/{}/{}.json'.format(location,year), "w") as f:
        json.dump(data, f)


def write_snotel_json_data_years(locations, years):
    for location in locations:
        for year in years:
            data = query_snotel_table(location,'{}0101'.format(year),'{}1231'.format(year))
            write_snotel_data_json(data, location, year)





locations = ['Pope Ridge', 'Trough','Upper Wheeler','Blewett Pass','Lyman Lake','Trinity','Park Creek Ridge','Stevens Pass']

write_snotel_json_data_years(locations, ['2015', '2016','2017','2018','2019'])

