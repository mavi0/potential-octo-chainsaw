FROM python:3.6-stretch

WORKDIR /remonitor

RUN pip3 install schedule \
    Flask \
    path.py \
    gunicorn

COPY . /remonitor

RUN nohup python3 cleanup.py &

EXPOSE 5000
CMD ["python3", "server.py"]