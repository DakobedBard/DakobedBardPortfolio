from flask import Flask, url_for
import os
import boto3
from markupsafe import escape
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"

@app.route("/locations")
def getLocations():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('BasinLocations')
    data = table.scan()
    locations = str(data['Items'])
    return locations
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

#
# @app.route("snotel"):





if __name__ == "__main__":



    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)