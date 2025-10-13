# =========================
# Stage 1 — Base Node builder
# =========================
FROM node:20-alpine AS build

WORKDIR /app

# Copy package files first for caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source files
COPY . .

# Build the production-ready app
RUN npm run build


# =========================
# Stage 2 — Production (Nginx)
# =========================
FROM nginx:alpine AS prod

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy built app from builder
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom nginx configuration (if you want)
# You can add this later for React Router support, etc.
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]


# =========================
# Stage 3 — Development (Optional)
# =========================
FROM node:20-alpine AS dev

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Expose Vite's default dev port
EXPOSE 5173

# Default command for Vite dev server
CMD ["npm", "run", "dev", "--", "--host"]
