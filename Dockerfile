FROM python:3.9

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app.py /app
COPY util.py /app
COPY read.py /app
COPY write.py /app
COPY config.py /app
COPY table_list.txt /app
COPY .env /app

CMD ["python", "app.py", "dev"]