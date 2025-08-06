#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn --bind 0.0.0.0:$PORT --workers 3 APIT.wsgi:application
