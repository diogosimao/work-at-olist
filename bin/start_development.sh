#!/bin/bash
export DEBUG=True
export DATABASE_URL=psql://db_user:user_password@127.0.0.1:5432/neattree
python manage.py runserver