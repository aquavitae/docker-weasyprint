FROM python:3.5-onbuild

RUN apt-get -y update \
    && apt-get install -y \
        fonts-font-awesome \
        libcairo2 \
        libffi-dev \
        libgdk-pixbuf2.0-0 \
        libpango1.0-0 \
        python-dev \
        python-lxml \
        shared-mime-info \
    && apt-get -y clean

EXPOSE 5001

CMD gunicorn --bind 0.0.0.0:5001 wsgi:app
