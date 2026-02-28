#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings

print("=" * 60)
print("Testing Supabase Storage Upload")
print("=" * 60)
print(f"Storage Backend: {settings.STORAGES['default']['BACKEND']}")
print(f"AWS_S3_ENDPOINT_URL: {settings.AWS_S3_ENDPOINT_URL}")
print(f"AWS_STORAGE_BUCKET_NAME: {settings.AWS_STORAGE_BUCKET_NAME}")
print(f"AWS_S3_CUSTOM_DOMAIN: {settings.AWS_S3_CUSTOM_DOMAIN}")
print(f"MEDIA_URL: {settings.MEDIA_URL}")
print()

try:
    # Try to upload a test file
    test_content = b"This is a test file"
    file_name = default_storage.save('test_upload.txt', ContentFile(test_content))
    file_url = default_storage.url(file_name)
    
    print(f"Upload successful!")
    print(f"File name in storage: {file_name}")
    print(f"Generated URL: {file_url}")
    print()
    
    # Try to read it back
    if default_storage.exists(file_name):
        print(f"File exists in storage: YES")
        with default_storage.open(file_name, 'r') as f:
            content = f.read()
            print(f"File content: {content}")
    else:
        print(f"File exists in storage: NO - Upload failed silently!")
        
except Exception as e:
    print(f"Error during upload test: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
