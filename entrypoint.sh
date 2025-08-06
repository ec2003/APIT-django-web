#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn server..."
gunicorn --bind 0.0.0.0:8000 --workers 3 APIT.wsgi:application
