import boto3
import os
import json

print(os.environ['AWS_ACCESS_KEY_ID'])

session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

dynamodb = session.resource('dynamodb', region_name='us-east-2')
db = dynamodb.Table('esVerbDefs')

print(db.creation_date_time)

data = json.load(open('verbs.json'))

for key, value in data.items():
    if(value[0]['tense'] == 'Infinitive'):
        for en in value[0]['translation'].split('; '):
            if(en[:3] != 'to '):
                en = 'to ' + en
            db.put_item(
                Item = {
                    'EN': en,
                    'ES': key,
                    'score': 0
                }
            )
            print("EN: " + en + " / ES: " + key)