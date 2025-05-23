FROM python:3.10-slim

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY bot/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .env .

COPY bot/ .

WORKDIR /app

CMD ["python3", "-u", "main.py"]
