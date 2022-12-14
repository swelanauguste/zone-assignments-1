#!/bin/sh

python manage.py flush --no-input

python manage.py createsuperuser --username king --email no-reply@mail.com --no-input

python manage.py add_zones
python manage.py add_agencies
python manage.py add_technicians


python manage.py collectstatic --no-input


exec "$@"