#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python3 manage.py collectstatic --no-input
python3 manage.py migrate
python3 manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --password $DJANGO_SUPERUSER_PASSWORD