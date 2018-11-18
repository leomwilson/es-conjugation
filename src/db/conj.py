import boto3
import os
import csv

def fill(s):
    if not s:
        return '-'
    else:
        return s

print(os.environ['AWS_ACCESS_KEY_ID'])

session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

dynamodb = session.resource('dynamodb', region_name='us-east-2')
db = dynamodb.Table('esConj')

print(db.creation_date_time)

lns = [line.rstrip('\n') for line in open('conj.csv')]
csv = []
for ln in lns:
    csv.append([bit.replace('"', '') for bit in ln.split('","')])

first = True
for row in csv:
    if(first): # ignores the first line
        first = False
        continue
    db.put_item(
        Item = {
            'ES': fill(row[0]),
            'yo': fill(row[7]),
            'tu': fill(row[8]),
            'el': fill(row[9]), # should have an accent
            'nosotros': fill(row[10]),
            'vosotros': fill(row[11]),
            'ellos': fill(row[12]),
            'gerund': fill(row[13]),
            'pastparticiple': fill(row[15]),
            'mood': fill(row[2]),
            'tense': fill(row[4])
        }
    )
    print("ES: " + fill(row[0]) + " / yo: " + fill(row[7]))