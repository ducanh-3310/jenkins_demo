FROM python:3.11-slim

# Tạo thư mục làm việc
WORKDIR /app

# Copy tất cả code vào container
COPY . .

# Cài dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
# Lệnh mặc định: chạy unit test
CMD ["python3", "app.py"]
