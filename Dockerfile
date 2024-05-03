FROM python:3.10-slim

COPY . /src
WORKDIR /src

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# 환경변수 설정
ENV VARIABLE_NAME=value

EXPOSE $PORT

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
