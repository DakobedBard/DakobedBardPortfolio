import json
import boto3
import numpy as np

def lambda_handler(event, context):

    guitarset = 'hello'
    return {
        "statusCode": 200,

        "body": guitarset,
    }
