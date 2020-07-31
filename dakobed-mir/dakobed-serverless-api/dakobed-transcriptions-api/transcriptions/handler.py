import json
import boto3
import numpy as np
from keras.models import load_model
def lambda_handler(event, context):

    guitarset = 'hello'
    model = load_model('/opt/python/model1.h5')
    return {
        "statusCode": 200,
        "body": guitarset,
    }
