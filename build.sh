#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirement.txt

cd minorproject
python manage.py migrate