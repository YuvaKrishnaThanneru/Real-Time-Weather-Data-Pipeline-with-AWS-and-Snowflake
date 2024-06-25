from datetime import datetime
import pandas as pd
import boto3
from io import StringIO
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("Weather-data")

def handle_insert(record):
    print("Handling Insert: ", record)
    dict = {}

    for key, value in record['dynamodb']['NewImage'].items():
        for dt, col in value.items():
            dict.update({key: col})

    dff = pd.DataFrame([dict])
    return dff

def lambda_handler(event, context):
    print(event)
    df = pd.DataFrame()

    for record in event['Records']:
        if record['eventName'] == "INSERT":
            dff = handle_insert(record)
            df = pd.concat([df, dff])  # Concatenate data for all cities

    if not df.empty:
        all_columns = list(df)
        df[all_columns] = df[all_columns].astype(str)

        # Group data by city and create CSV files
        groups = df.groupby('city')
        for city, group in groups:
            csv_buffer = StringIO()
            group.to_csv(csv_buffer, index=False)
            
            path = f"snowflake/Weather-data/Weather-data_{city}_{str(datetime.now())}.csv"
            s3 = boto3.client('s3')
            bucketName = "data-from-db"
            key = path
            
            s3.put_object(Bucket=bucketName, Key=key, Body=csv_buffer.getvalue())

    print('Successfully processed %s records.' % str(len(event['Records'])))
