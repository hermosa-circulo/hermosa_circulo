FROM ubuntu
MAINTAINER bando

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common python-software-properties build-essential sysv-rc-conf curl git
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y sqlite3 libsqlite3-dev python-setuptools python-pip
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mercurial make binutils bison gcc

RUN mkdir /var/oppai_iga
WORKDIR /var/oppai_iga
ADD ./ /var/oppai_iga/
RUN pip install -r requirements.txt
RUN python manage.py migrate
#RUN echo yes | python manage.py collectstatic
CMD python manage.py runserver 0.0.0.0:8000 && bash

EXPOSE 8000
