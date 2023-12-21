#!/usr/bin/env bash
# exit on error
set -o errexit

pip freeze > requirement.txt
pip install -r requirement.txt

cd minorproject
python manage.py migrate