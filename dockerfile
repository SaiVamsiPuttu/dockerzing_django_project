FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /cloud_assessment1
WORKDIR /cloud_assessment1
ADD requirements.txt /cloud_assessment1/
RUN pip install -r requirements.txt
ADD . /cloud_assessment1/
