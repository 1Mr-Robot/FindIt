#!/bin/sh

set -e

echo "Waiting for MySQL..."

while ! nc -z db 3306; do
  sleep 1
done

echo "MySQL is ready!"

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Checking superuser..."

python << END
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FindIt.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

institutional_email = os.getenv('SUPERUSER_EMAIL')
password = os.getenv('SUPERUSER_PASSWORD')
first_name = os.getenv('SUPERUSER_FIRST_NAME')
last_name = os.getenv('SUPERUSER_LAST_NAME')
tuition = os.getenv('SUPERUSER_TUITION')

if institutional_email and not User.objects.filter(institutional_email=institutional_email).exists():
    User.objects.create_superuser(
        institutional_email=institutional_email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        tuition=tuition
    )
    print("Superuser created")
else:
    print("Superuser already exists or not defined")
END

echo "Starting server..."
exec gunicorn FindIt.wsgi:application --bind 0.0.0.0:8000