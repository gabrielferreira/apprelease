#!/bin/bash

cd /docker-mobrelease/app

echo CREATE DATABASE IF NOT EXISTS apprelease | mysql -uroot -h mysql

python manage.py syncdb --noinput
python manage.py migrate
python manage.py loaddata ./csmobrelease/fixtures/user.json
python manage.py loaddata ./apps/mobrelease/fixtures/platform.json
python manage.py collectstatic --noinput

/usr/sbin/apache2ctl -D FOREGROUND
