#!/bin/bash
export DJANGO_SETTINGS_MODULE=neattree.settings.production
python manage.py generate_secret_key --replace
python manage.py makemigrations
python manage.py migrate
