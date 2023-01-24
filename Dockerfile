FROM python:slim

COPY . /app
WORKDIR /app


RUN python3 -c "print('xD')"
