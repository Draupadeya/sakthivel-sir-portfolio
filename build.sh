#!/bin/bash
set -e  # Exit on error

echo "Building portfolio application..."

# Install system dependencies (for Pillow and psycopg2)
echo "Installing system dependencies..."
apt-get update && apt-get install -y build-essential libjpeg-dev zlib1g-dev

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running migrations..."
python manage.py migrate

echo "Build complete!"
