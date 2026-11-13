# Multi-stage Dockerfile for Smart Study Planner & Optimizer
FROM python:3.11-slim

# Thiết lập biến môi trường
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

# Cài đặt thư viện hệ thống cần thiết
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Cài đặt các gói phụ thuộc Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn dự án
COPY . /app/

# Chạy migrate và thu thập static files khi build hoặc startup
RUN python manage.py collectstatic --noinput || true

# Mở cổng dịch vụ
EXPOSE 8000

# Khởi chạy ASGI Server (Django + FastAPI mounted)
CMD ["sh", "-c", "python manage.py migrate && python manage.py seed_data && uvicorn study_planner.asgi:application --host 0.0.0.0 --port ${PORT:-8000}"]
