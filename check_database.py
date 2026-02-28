#!/usr/bin/env python
"""
Database Connection Check Script
Run: python check_database.py
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
sys.path.insert(0, os.path.dirname(__file__))

from decouple import config

print("=" * 60)
print("DATABASE CONNECTION DIAGNOSTIC")
print("=" * 60)

# 1. Check environment variables
print("\n1. Environment Variables:")
database_url = config('DATABASE_URL', default='')
secret_key = config('SECRET_KEY', default='default-key')
debug = config('DEBUG', default=False)

print(f"   DATABASE_URL: {database_url[:50]}..." if database_url else "   DATABASE_URL: NOT SET ❌")
print(f"   SECRET_KEY: {'SET ✓' if secret_key != 'default-key' else 'USING DEFAULT ❌'}")
print(f"   DEBUG: {debug}")

# 2. Check Django Database Config
print("\n2. Django Database Configuration:")
django.setup()

from django.conf import settings
db_config = settings.DATABASES['default']
print(f"   ENGINE: {db_config['ENGINE']}")
print(f"   NAME: {db_config.get('NAME', 'N/A')}")
print(f"   HOST: {db_config.get('HOST', 'local')}")

# 3. Test database connection
print("\n3. Testing Database Connection...")
from django.db import connection
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        print("   ✓ Database connection successful!")
except Exception as e:
    print(f"   ❌ Database connection failed: {e}")
    sys.exit(1)

# 4. Check tables
print("\n4. Checking Tables...")
from home.models import Achievement, Award, GalleryImage
try:
    achievement_count = Achievement.objects.count()
    award_count = Award.objects.count()
    gallery_count = GalleryImage.objects.count()
    print(f"   Achievements: {achievement_count} record(s) ✓")
    print(f"   Awards: {award_count} record(s) ✓")
    print(f"   Gallery Images: {gallery_count} record(s) ✓")
except Exception as e:
    print(f"   ❌ Error querying tables: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✓ All checks passed!")
print("=" * 60)
