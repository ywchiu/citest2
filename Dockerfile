FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
MAINTAINER ywchiu "david@largitdata.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
