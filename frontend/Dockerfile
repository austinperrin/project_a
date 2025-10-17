###############################################################
# Frontend Service Dockerfile
# Multi-stage build for development and production environments
# Base image: node:25-alpine
###############################################################

# ============================
# Base Stage
# ============================
FROM node:25-alpine AS base

WORKDIR /app

# Configure CA trust for internal/company certificate
COPY ./certs/company-ca.crt /etc/ssl/certs/company-ca.crt
RUN mkdir -p /usr/local/share/ca-certificates \
    && cp /etc/ssl/certs/company-ca.crt /usr/local/share/ca-certificates/company-ca.crt \
    && cat /usr/local/share/ca-certificates/company-ca.crt >> /etc/ssl/certs/ca-certificates.crt \
    && apk update && apk add --no-cache ca-certificates \
    && update-ca-certificates

# Configure Node and npm to trust this CA
ENV NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt
RUN npm config set cafile /etc/ssl/certs/ca-certificates.crt \
    && npm config set strict-ssl true

# Install dependencies first (leveraging cache)
COPY ./frontend/package*.json ./
# If you use package-lock.json or npm 7+, npm ci is preferred for reproducible builds
RUN if [ -f package-lock.json ]; then npm ci; else npm install; fi


# ============================
# Build Stage
# ============================
FROM base AS build

# Copy the application source and build production assets
COPY ./frontend ./
RUN npm run build


# ============================
# Development Stage
# ============================
FROM base AS dev

# Copy source files after dependency installation
COPY ./frontend ./

# Expose Vite's default dev server port
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]


# ============================
# Production Runtime Stage
# ============================
FROM nginx:alpine AS prod

WORKDIR /usr/share/nginx/html

# Clean out default nginx content and copy built assets
RUN rm -rf ./*
COPY --from=build /app/dist ./

# Optional custom nginx.conf (e.g., for React Router)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
