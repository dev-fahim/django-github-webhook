#!/usr/bin/env bash

export DOCKER_HOST=127.0.0.1

docker-compose down

docker-compose build

docker-compose run web python manage.py check

docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate

docker-compose up -d

docker-compose logs -t --tail=100
