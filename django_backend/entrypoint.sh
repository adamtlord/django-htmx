#!/bin/bash
python manage.py migrate --noinput
python manage.py initadmin
python manage.py fakedata