FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/

RUN apt-get update -y && apt-get install -y git mysql-client libmysqlclient-dev \
	python-dev apache2 libapache2-mod-wsgi \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN a2enmod proxy proxy_* wsgi
RUN a2enmod rewrite

RUN chmod -R 775 /usr/src/app/
RUN chown -R www-data:www-data /usr/src/app/
VOLUME /usr/src/app

EXPOSE 80
EXPOSE 443
CMD ["apache2-foreground"]
