#!/bin/bash
python manage.py generate_secret_key --replace
python manage.py makemigrations
python manage.py migrate
