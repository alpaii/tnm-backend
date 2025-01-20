## 요구 사항

- Python 3.13

## 1. 로컬 실행 환경

### 1.1 리포지토리 클론

```bash
git clone https://github.com/alpaii/tnm-backend.git
cd tnm-backend
```

### 1.2 가상 환경 생성 및 활성화

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 1.3 의존성 설치

```bash
pip install -r requirements.txt
```

### 1.4 마이그레이션 실행

```bash
python manage.py migrate
```

### 1.5 서버 실행

```bash
python manage.py runserver
```

## 2. Docker 실행 환경

### 2.1 docker-compose

```bash
# venv 폴더 존재할 경우 제외
venv/.dockerignore  # 파일 생성

docker-compose up -d
```
