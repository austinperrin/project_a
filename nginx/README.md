# Nginx — Project A

This directory contains the **Nginx reverse proxy** configuration for Project A.  
Nginx serves the frontend and proxies API requests to the backend.

---

## Project Structure

```
nginx/
├── nginx.conf
└── README.md
```

---

## Role in the Architecture

- Serves static frontend build files from `/usr/share/nginx/html`
- Proxies `/api/` requests to the backend
- Serves static/media files from the backend
- Handles SPA routing

---

## Running with Docker

```bash
docker compose -f ../docker-compose.prod.yml up --build -d
```

- Frontend served through Nginx  
- Backend proxied through `/api/`

---

## Example Configuration

```nginx
server {
    listen 80;

    location / {
        root /usr/share/nginx/html;
        try_files $uri /index.html;
    }

    location /api/ {
        proxy_pass http://backend:8000;
    }

    location /static/ {
        alias /app/staticfiles/;
    }

    location /media/ {
        alias /app/media/;
    }
}
```

---

## Future Split Hosting

```nginx
# upstream django {
#     server backend.yourdomain.internal:8000;
# }
```

This allows backend and frontend to be deployed separately.

---

## Troubleshooting

| Issue                        | Cause                       | Fix                                                   |
|-------------------------------|----------------------------|--------------------------------------------------------|
| Frontend not loading          | Missing build              | Run frontend build and rebuild Nginx container         |
| API requests failing          | Wrong proxy_pass target    | Check backend service name and port                   |
| Static files not loading      | Incorrect alias path       | Verify paths in `nginx.conf`                           |
