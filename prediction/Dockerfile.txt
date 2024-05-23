FROM python:3.11-slim

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y libpq-dev && apt-get clean
RUN pip install -r requirements.txt
RUN pip install gunicorn


CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'root@example.com', 'admin')" \
    && python manage.py clear_db \
    && python manage.py initialize_db \
    && python manage.py collectstatic --no-input \
    && ls /app/static \
    && gunicorn prediction.wsgi:application --bind 0.0.0.0:8000 --log-level info