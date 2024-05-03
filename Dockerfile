FROM python:3.10

COPY . /src
WORKDIR /src

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# 환경변수 설정 (이 부분은 필요한 경우에만 추가합니다)
ENV VARIABLE_NAME=value

# EXPOSE 8080

# CMD 지시문을 수정하여 $PORT 환경 변수를 사용하도록 설정합니다.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
