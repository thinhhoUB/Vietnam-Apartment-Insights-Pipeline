import csv
import json
import boto3
import time
from datetime import datetime
import pandas as pd
import numpy as np
import io
import re



def lambda_handler(event, context):
    
    event_params=event["Records"][0]
    
    bucket=event_params["s3"]["bucket"]["name"]
    key=event_params["s3"]["object"]["key"]
    
    print(bucket)
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket= bucket, Key= key)
    csv_bytes = response['Body'].read()

    # Convert bytes to DataFrame using pandas
    apt_listing = pd.read_csv(io.BytesIO(csv_bytes))
    
    #helper functions
    def remove_punctuation(my_str):
        return None if my_str == None else re.sub(r'[^\w\s]', '', my_str.strip())
        
    def split_full_address(address):
        parts = address.split(", ")
        length = len(parts)
        province = remove_punctuation(parts[-1]) if length >= 1 else None
        district = remove_punctuation(parts[-2]) if length >= 2 else None
        ward = remove_punctuation(parts[-3]) if length >= 3 else None
        street = remove_punctuation(parts[-4]) if length >= 4 else None
        return (street, ward, district, province) 
        
    def create_bed_bath(row):
        bedroom = str(int(row['bedroom_number'])) if pd.notnull(row['bedroom_number']) else '1'
        bathroom = str(int(row['bathroom_number'])) if pd.notnull(row['bathroom_number']) else '1'
        return bedroom + ' - ' + bathroom
    print('Transformation Started')
    print('change columns name')
    columns_name = ["area (sq ft)","price ($)","frontage","alley_length_to_house","house_direction","balcony_direction","floor_number","bedroom_number","bathroom_number",
    "legal_document","furnished","uploaded_date","expired_date","listing_article_tier","listing_id","full_address","latitude","longtitude","url"]
    apt_listing.columns= columns_name
    
    print('drop unescessary columns')
    apt_listing.drop(["frontage","alley_length_to_house","floor_number","legal_document","listing_article_tier"],inplace=True, axis=1)
    
    #print( 'Convert the date column to datetime format')
    #apt_listing['uploaded_date'] = pd.to_datetime(apt_listing['uploaded_date'] , format='%d/%m/%Y')
    #apt_listing['uploaded_date']  = apt_listing['uploaded_date'].dt.strftime('%m/%d/%Y')
    #apt_listing['expired_date'] = pd.to_datetime(apt_listing['expired_date'] , format='%d/%m/%Y')
    #apt_listing['expired_date']  = apt_listing['expired_date'].dt.strftime('%m/%d/%Y')
    
    print('square meter to square feet')
    apt_listing["area (sq ft)"] = np.round(pd.to_numeric(apt_listing["area (sq ft)"].str.split().str[0]) * 10.76, 2)
    
    print('Vietnam Dong to USD')
    round_price = lambda x: np.round(pd.to_numeric(x.replace(',', '').split()[0]) * 1000000 / 24000, 2) if 'triệu/tháng' in x else None
    apt_listing['price ($)'] = apt_listing['price ($)'].apply(round_price)
    
    print('calculate price per sqft')
    apt_listing['price_per_sqft'] = round(apt_listing['price ($)'] / apt_listing['area (sq ft)'], 2)
    
    print('Furnished column')
    check_nan = lambda x: 'No' if x is None or x is np.nan else 'Yes'
    apt_listing['furnished']= apt_listing['furnished'].apply(check_nan)
    
    print('extract address detail')
    apt_listing['street'], apt_listing['ward'], apt_listing['district'], apt_listing['province'] = zip(*apt_listing['full_address'].apply(split_full_address))
    
    print('number of bedroom and bathroom')
    number_of_room = lambda x: int(str(x).split()[0]) if 'phòng' in str(x) else None
    apt_listing["bedroom_number"] = apt_listing["bedroom_number"].apply(number_of_room)
    apt_listing["bathroom_number"] = apt_listing["bathroom_number"].apply(number_of_room)
    apt_listing['bed_bath'] = apt_listing.apply(create_bed_bath, axis=1)
    
    print('change value of house direction and balcony direction')
    translation_dict = {'Đông': 'East','Tây': 'West','Nam': 'South','Bắc': 'North','Đông - Nam': 'Southeast','Đông - Bắc': 'Northeast','Tây - Nam': 'Southwest','Tây - Bắc': 'Northwest',np.nan: None}
    apt_listing['house_direction'] = apt_listing['house_direction'].map(translation_dict)
    apt_listing['balcony_direction'] = apt_listing['balcony_direction'].map(translation_dict)
    
    print('Transformation ended')
    new_bucket = 'processed-apt-listing-data'
    new_key = 'processed/' + key  # Assuming you want to store processed files in 'processed/' prefix
    csv_buffer = io.StringIO()
    apt_listing.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=new_bucket, Key=new_key, Body=csv_buffer.getvalue())
    print("File successfully uploaded to new bucket:", new_bucket, "with key:", new_key)
    
    