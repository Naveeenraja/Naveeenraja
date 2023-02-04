FROM python:3-slim-buster
COPY . /python-flask
WORKDIR /python-flask
RUN pip install flask
RUN pip install flask_session 
ENTRYPOINT ['python','mcq.py']
