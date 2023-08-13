FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT ["gunicorn", "config.wsgi:application", "--bind", "0:8000"]