FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

CMD ["taipy", "run", "--no-debug", "--no-reloader", "main.py", "--host", "0.0.0.0", "-P", "8000"]