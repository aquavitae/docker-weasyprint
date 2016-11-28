FROM python:2.7-wheezy

RUN apt-get -y update \
    && apt-get install -y \
        libcairo2 \
        libffi-dev \
        libgdk-pixbuf2.0-0 \
        libpango1.0-0 \
        python-dev \
        python-lxml \
        shared-mime-info \
        net-tools\
        git\
    && apt-get -y clean

COPY /qhv2.004otf/*.* /usr/share/fonts/opentype/
COPY /RobotoTTF/*.* /usr/share/fonts/truetype/

WORKDIR /usr/src

RUN git clone https://github.com/sander76/weasy-server.git

WORKDIR /usr/src/weasy-server

RUN pip install -r requirements.txt

EXPOSE 5001

# CMD gunicorn --bind 0.0.0.0:5001 wsgi:app
CMD python wsgi.py