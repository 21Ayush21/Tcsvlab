#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

cd minorproject
python manage.py migrate