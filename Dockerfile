# syntax=docker/dockerfile:1

# pull the official base image
FROM python:3.10.8-slim-bullseye

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


