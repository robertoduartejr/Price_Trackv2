release: python manage.py migrate
web: gunicorn project.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput