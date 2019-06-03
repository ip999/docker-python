FROM python:3.7-alpine

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY app.py .

CMD [ "python", "./app.py" ]
