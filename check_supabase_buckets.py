#!/usr/bin/env python
import boto3
from decouple import config

# Create S3 client pointing to Supabase Storage
s3_client = boto3.client(
    's3',
    endpoint_url=config('SUPABASE_URL'),
    aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
    region_name='auto'
)

print("=" * 60)
print("Supabase Storage Buckets")
print("=" * 60)

try:
    response = s3_client.list_buckets()
    buckets = response.get('Buckets', [])
    
    if buckets:
        print(f"Found {len(buckets)} bucket(s):")
        for bucket in buckets:
            print(f"  - {bucket['Name']} (created: {bucket['CreationDate']})")
    else:
        print("No buckets found")
        
except Exception as e:
    print(f"Error listing buckets: {type(e).__name__}: {e}")
    
# Also try to list objects in the portfolio bucket
print()
print("=" * 60)
print("Testing Portfolio Bucket")
print("=" * 60)

try:
    response = s3_client.list_objects_v2(Bucket='portfolio', MaxKeys=10)
    if 'Contents' in response:
        print(f"Files in 'portfolio' bucket:")
        for obj in response['Contents']:
            print(f"  - {obj['Key']} ({obj['Size']} bytes)")
    else:
        print("No files in 'portfolio' bucket (or bucket is empty)")
except Exception as e:
    print(f"Error listing portfolio bucket: {type(e).__name__}: {e}")
