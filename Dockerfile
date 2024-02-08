FROM python:3.11.4-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update

COPY requirements.txt requirements.txt 

RUN pip install --upgrade pip 

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

# ENTRYPOINT [ "sh", "./entrypoint.sh" ]
RUN chmod +x ./entrypoint.sh
RUN chmod +x ./worker_entrypoint.sh
