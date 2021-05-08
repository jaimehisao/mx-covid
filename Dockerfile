FROM python:3-alpine
#FROM ubuntu:latest
WORKDIR /usr/code/covid

COPY requirements.txt ./


#RUN apt-get update && apt-get install -y --no-install-recommends \
  #  python3.5 \
  #  python3-pip \
 #   && apt-get clean
#RUN python3 -m pip install -r requirements.txt --no-cache-dir


RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . .

CMD [ "python3", "-u", "main.py" ]