FROM python:3.10-slim

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt 

COPY . /app/
WORKDIR /app

RUN mkdir -p /app/static && \
    chown nobody:nogroup -R /app

EXPOSE 8000
USER nobody

CMD python3 manage.py collectstatic --noinput && \
    python3 manage.py migrate --run-syncdb && \
    gunicorn api.wsgi:application -b 0.0.0.0:8000