#!/bin/bash
set -e

echo "Building portfolio application..."

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies (should already be installed, but ensure)
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running migrations..."
python manage.py migrate

echo "Build complete!"
