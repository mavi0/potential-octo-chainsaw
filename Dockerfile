FROM python:3.6-stretch

WORKDIR /remonitor

RUN pip3 install schedule \
    Flask \
    path.py \
    gunicorn

COPY . /remonitor

RUN chmod +x main.sh

EXPOSE 5050
ENTRYPOINT ["./main.sh"]