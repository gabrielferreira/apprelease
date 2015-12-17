FROM python:2.7

WORKDIR /var/www/html
COPY requirements.txt /var/www/html/

RUN apt-get update -y \
	&& apt-get install -y git \
		apache2 \
		mysql-client \
		libmysqlclient-dev \
		python-dev \
		libapache2-mod-wsgi \
		libapache2-mod-proxy-html \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir -r requirements.txt

COPY . /var/www/html/
RUN a2enmod wsgi
COPY apprelease.conf /etc/apache2/sites-enabled/apprelease.conf

RUN chmod -R 775 /var/www/html
RUN chown -R www-data:www-data /var/www/html
VOLUME /var/www/html
RUN service apache2 restart
EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/bin/bash"]
CMD ["/var/www/html/start-project.sh"]
