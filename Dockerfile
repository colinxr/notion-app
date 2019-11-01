FROM ubuntu:19.10

RUN apt-get update -y ; apt-get upgrade -y
RUN apt-get install -y apache2 --no-install-recommends; apt-get install -y libapache2-mod-wsgi-py3 --no-install-recommends
RUN a2enmod wsgi

RUN mkdir /var/www/Notion
COPY . /var/www/Notion

RUN cd /usr/local/bin ; ln -s /usr/bin/python3 python

RUN apt-get install -y wget --no-install-recommends
RUN adduser --system --group --disabled-login colin ; cd /home/colin/
RUN apt-get update -y ; apt-get upgrade -y
RUN apt-get install -y python3-pip --no-install-recommends
RUN wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py' ; python get-pip.py --disable-pip-version-check --no-cache-dir
# pip should be now pip3
RUN pip --version ; rm -f get-pip.py

RUN pip install -r /var/www/Notion/requirements.txt

RUN chown -R colin:www-data /var/www/Notion

COPY Notion.conf /etc/apache2/sites-available/Notion.conf

RUN rm -rf /etc/apache2/sites-available/000-default.conf
RUN rm -rf /etc/apache2/sites-enabled/000-default.conf

RUN rm -rf /var/www/Notion/Notion.conf
RUN rm -rf /var/www/Notion/Dockerfile
RUN rm -rf /var/www/Notion/requirements.txt

RUN service apache2 start
RUN sleep 10

RUN chown -R colin:www-data /var/www/Notion

RUN service apache2 start
RUN sleep 4

EXPOSE 80 443

RUN apt-get clean


#  docker-compose build \
#  --build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
#  --build-arg VCS_REF=`git rev-parse --short HEAD` \
#  --build-arg VERSION="latest"



ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.version=$VERSION \
  org.label-schema.license="MIT" \
  org.label-schema.name="Docker image with flask app base (using apache2, wsgi, py3, ubuntu)" \
  org.label-schema.description="Docker image to create docker container from, that accommodates Flask web app which relies on Apache 2, wsgi, Python 3, and Ubuntu." \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/dm4rnde/docker-flask-app-base-apache2-wsgi-py3" \
  org.label-schema.docker.schema-version="1.0"

ENTRYPOINT ["/bin/bash", "/usr/sbin/apache2ctl", "-D", "FOREGROUND"]