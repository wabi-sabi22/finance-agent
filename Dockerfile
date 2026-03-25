# Sử dụng Python image chính thức
FROM python:3.11-slim

# Cài đặt uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file cấu hình dự án
COPY pyproject.toml ./

# Cài đặt dependencies (không cài đặt project dưới dạng package)
RUN uv sync --no-cache

# Copy toàn bộ mã nguồn
COPY . .

# Mở port cho Gradio (Hugging Face dùng port 7860)
EXPOSE 7860

# Chạy ứng dụng bằng uv
CMD ["uv", "run", "main.py"]
