###############################################################
# Backend Service Dockerfile
# Multi-stage build for development and production environments
# Base image: python:3.14.0-slim-trixie
###############################################################

# ============================
# Base Stage
# ============================
FROM python:3.14.0-slim-trixie AS base

WORKDIR /app

# Environment configuration for Python and SSL trust
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# Install system dependencies and configure CA certificates
COPY ./certs /usr/local/share/ca-certificates/
RUN apt-get update && apt-get install -y \
    ca-certificates \
    build-essential \
    libpq-dev \
 && update-ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Configure pip to use trusted hosts and CA certs
RUN mkdir -p /root/.config/pip \
 && echo "[global]\ncert = /etc/ssl/certs/ca-certificates.crt\ntrusted-host = pypi.org pypi.python.org files.pythonhosted.org" \
    > /root/.config/pip/pip.conf

# Copy backend source code into the image
COPY ./backend ./backend


# ============================
# Development Stage
# ============================
FROM base AS dev

# Install all development dependencies
RUN pip install --upgrade pip && \
    pip install -r backend/requirements/dev-requirements.txt

# Expose port and start Django development server
EXPOSE 8000
CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]


# ============================
# Production Build Stage
# ============================
FROM base AS builder

# Install only production dependencies to reduce final image size
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r backend/requirements/requirements.txt


# ============================
# Production Runtime Stage
# ============================
FROM python:3.14.0-slim-trixie AS prod

WORKDIR /app

# Install runtime dependencies and configure CA certificates
COPY ./certs /usr/local/share/ca-certificates/
RUN apt-get update && apt-get install -y \
    ca-certificates \
    libpq-dev \
 && update-ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Copy production dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy backend source code
COPY ./backend ./backend

# Expose port and start Gunicorn server for production
EXPOSE 8000
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
