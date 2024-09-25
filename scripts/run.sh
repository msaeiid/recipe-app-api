#!/bin/sh

# if any command fail crash it and start from next command
set -e

python manage.py wait_for_db
python manage.py collecstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi