# 베이스 이미지를 지정합니다.
FROM python:3.9-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 필요한 파일들을 복사합니다.
COPY requirements.txt .

# 의존성을 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드를 복사합니다.
COPY . .

# Flask 애플리케이션을 실행합니다.
CMD ["python", "app.py"]