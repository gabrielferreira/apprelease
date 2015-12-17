#!/bin/bash

cd /var/www/html

#echo CREATE DATABASE IF NOT EXISTS apprelease | mysql -uroot -h mysql

python manage.py syncdb --noinput
python manage.py migrate
# python manage.py collectstatic --noinput

# /usr/sbin/apache2ctl -D FOREGROUND
python manage.py runserver 0.0.0.0:8080
