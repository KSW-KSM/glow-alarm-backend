FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8080

# CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8080"]
