FROM python:3.7-alpine

COPY config.py /twitter-emotion-bot/
COPY app.py /twitter-emotion-bot/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /twitter-emotion-bots
CMD ["python3", "app.py"]