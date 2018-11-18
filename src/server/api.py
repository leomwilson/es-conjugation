from flask import Flask
import boto3
from boto3.dynamodb.conditions import Key
import os

app = Flask(__name__)

session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

dynamodb = session.resource('dynamodb', region_name='us-east-2')
db = dynamodb.Table('esVerbDefs')

@app.route("/en/<inf>")
def es(inf):
    high = 0
    c = ''
    for v in db.query(KeyConditionExpression=Key('EN').eq(inf)):
        if v['score'] < high:
            continue
        else:
            c = v['ES']
            high = v['score']
    return c
@app.route("/plus/<es>/<en>")
def plus(es, en):
    return db.update_item(Key={'ES':es,'EN':en}, UpdateExpression='set score = :s', ExpressionAttributeValues={':s':(db.get_item(Key={'ES':es,'EN':en})['Item']['score']+1)})
@app.route("/minus/<es>/<en>")
def minus(es, en):
    return db.update_item(Key={'ES':es,'EN':en}, UpdateExpression='set score = :s', ExpressionAttributeValues={':s':(db.get_item(Key={'ES':es,'EN':en})['Item']['score']-1)})