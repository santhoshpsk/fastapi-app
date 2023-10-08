FROM python:3.12

WORKDIR /opt/src/

COPY . .

RUN pip install -r requirements.pip

CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]