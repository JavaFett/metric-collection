FROM python:3.11-alpine

COPY . /var/www/metric-collection-service

RUN apk --no-cache add musl-dev linux-headers g++

RUN pip install --upgrade pip && pip install --no-cache-dir -r /var/www/metric-collection-service/requirements.txt

WORKDIR /var/www/metric-collection-service/app/

EXPOSE 80

CMD ["python", "./main.py"]
