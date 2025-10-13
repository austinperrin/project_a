# =========================
# Stage 1 — Base image
# =========================
FROM python:3.12-slim AS base

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirement files
COPY requirements/ ./requirements/

# =========================
# Stage 2 — Development image
# =========================
FROM base AS dev

# Install dev dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements/base-requirements.txt && \
    pip install -r requirements/dev-requirements.txt

# Copy project files
COPY . .

# Default command for development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# =========================
# Stage 3 — Production image
# =========================
FROM base AS prod

# Install production dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements/base-requirements.txt && \
    pip install -r requirements/prod-requirements.txt && \
    pip install gunicorn psycopg2-binary

# Copy project files
COPY . .

# Collect static files during build (optional)
RUN python manage.py collectstatic --noinput || true

# Expose the application port
EXPOSE 8000

# Run the app with Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
