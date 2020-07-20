#!/usr/bin/env bash

git pull

export DOCKER_HOST=127.0.0.1

sudo docker-compose down

sudo docker-compose build

sudo docker-compose run web python manage.py check

sudo docker-compose run web python manage.py makemigrations
sudo docker-compose run web python manage.py migrate

sudo docker-compose up -d

sudo docker-compose logs -t --tail=100
