FROM python:2.7

RUN apt-get update && apt-get install -y ca-certificates curl librecode0 libsqlite3-0 libxml2 --no-install-recommends && rm -r /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y apache2-bin apache2.2-common --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV GPG_KEYS 0B96609E270F565C13292B24C13C70B87267B52D 0BD78B5F97500D450838F95DFE857D9A90D90EC1 F38252826ACD957EF380D39F2F7956BC5DA04B5D
RUN set -xe \
	&& for key in $GPG_KEYS; do \
		gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	done

COPY apache2-foreground /usr/local/bin/

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/

RUN apt-get update -y \
	&& apt-get install -y git \
		mysql-client \
		libmysqlclient-dev \
		python-dev \
		libapache2-mod-wsgi \
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
