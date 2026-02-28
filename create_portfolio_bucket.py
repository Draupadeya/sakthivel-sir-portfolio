#!/usr/bin/env python
import boto3
from decouple import config

s3_client = boto3.client(
    's3',
    endpoint_url=config('SUPABASE_URL'),
    aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
    region_name='auto'
)

print("=" * 60)
print("Creating Portfolio Bucket")
print("=" * 60)

try:
    response = s3_client.create_bucket(Bucket='portfolio')
    print("Bucket created successfully!")
    print(f"Response: {response}")
    
    # Make bucket public by adding a public read policy
    print()
    print("=" * 60)
    print("Setting Bucket Public Access")
    print("=" * 60)
    
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicRead",
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:GetObject"
                ],
                "Resource": "arn:aws:s3:::portfolio/*"
            }
        ]
    }
    
    import json
    s3_client.put_bucket_policy(
        Bucket='portfolio',
        Policy=json.dumps(policy)
    )
    print("Public read policy applied!")
    
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
