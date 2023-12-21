#!/usr/bin/env bash
# exit on error
set -o errexit

pip freeze > requirements.txt

cd minorproject
python manage.py migrate