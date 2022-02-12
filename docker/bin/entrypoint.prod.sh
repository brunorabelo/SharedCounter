#!/bin/sh
python manage.py migrate --noinput
python manage.py collectstatic --no-input --clear

#daphne -p 8001 appcounter.asgi:application -b 0.0.0.0 &

exec "$@"
