FROM python:alpine

ENV PYTHONUNBUFFERED=1

COPY ./requirments.txt requirments.txt
RUN pip install --upgrade pip
RUN pip install -r requirments.txt

RUN mkdir /usr/src/app 
COPY ./django-project /usr/src/app
WORKDIR /usr/src/app
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
