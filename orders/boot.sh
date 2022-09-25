sleep 10
cd ./orders
python manage.py makemigrations --noinput
python manage.py migrate --noinput

python manage.py createsuperuser --email=$DJANGO_SUPERUSER_EMAIL --noinput

gunicorn orders.wsgi --bind 0.0.0.0:8000