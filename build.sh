#!/bin/bash
echo "Building portfolio application..."

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate --run-syncdb

echo "Build complete!"
