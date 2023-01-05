#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate
python manage.py createsuperuser --username king --email no-reply@mail.com --no-input

python manage.py add_zones 
python manage.py add_agencies
python manage.py add_technicians

python manage.py collectstatic --no-input

exec "$@"