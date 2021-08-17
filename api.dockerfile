FROM python:3.8

RUN apt-get update

EXPOSE 5000

ADD reqs.txt .
RUN python -m pip install pip -U
RUN python -m pip install -r reqs.txt

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /app

WORKDIR /app

CMD python -m api.app
