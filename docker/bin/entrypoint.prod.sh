#!/bin/sh
python manage.py migrate --noinput
python manage.py collectstatic --no-input --clear

daphne -p 8001 appcounter.asgi:application -b 0.0.0.0 &

gunicorn appcounter.wsgi:application --bind 0.0.0.0:8000 &

exec "$@"
