#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from home.models import GalleryImage
from django.conf import settings

print("=" * 60)
print("Storage Configuration Debug")
print("=" * 60)
print(f"STORAGES: {settings.STORAGES}")
print(f"MEDIA_URL: {settings.MEDIA_URL}")
print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
print()

# Get any existing images
images = GalleryImage.objects.all()
print(f"Found {images.count()} gallery images")
print()

if images:
    for img in images[:3]:  # Show first 3
        print(f"Image: {img.title}")
        print(f"  - Raw field: {img.image}")
        print(f"  - URL: {img.image.url}")
        print(f"  - Name: {img.image.name}")
        print()
else:
    print("No images in database")
