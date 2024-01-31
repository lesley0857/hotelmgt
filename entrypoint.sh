#!/bin/ash

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn hotelmgtproj.wsgi:app --bind 0.0.0.0:8000
