FROM python:3.7-alpine

COPY config.py
COPY app.py
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

CMD ["python3", "app.py"]