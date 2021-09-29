FROM python:3.9.6-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install pipenv

RUN pip install --upgrade pip

COPY Pipfile /app/

RUN pipenv install --python python3 --deploy

COPY . /app/

RUN pipenv run python manage.py collectstatic --no-input -v 0
