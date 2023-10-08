FROM python:3.12

WORKDIR /opt/src/

COPY . .

RUN pip install -r requirements.pip