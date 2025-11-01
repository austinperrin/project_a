# Backend - Project A

This is the Django REST API backend for Project A.  
It powers the core business logic, authentication, and data layer.  
For full project setup, see [Project Root README](../README.md).

---

## Tech Stack
- Django & Django REST Framework
- Gunicorn (production)
- PostgreSQL
- django-environ
- Docker (multi-container networking)

---

## Project Structure

```
backend/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── requirements/
│   ├── base-requirements.txt
│   ├── dev-requirements.txt
│   └── prod-requirements.txt
├── .dockerignore
├── Dockerfile
├── manage.py
└── README.md
```

- `config/` contains Django configuration files.
- `requirements/` contains separate requirements files for base, development, and production.
- The backend is fully containerized using Docker.

---

## Environment Variables

These are the backend-specific environment variables.  
See the root README for the full `.env` configuration.

```env
# ============================================================
# Django Core Settings
# ============================================================

DJANGO_SETTINGS_MODULE=config.settings.dev
DJANGO_SECRET_KEY=change-me-to-a-very-secret-value
DJANGO_DEBUG=True  # Set to False in production!

# Allowed hosts (comma separated)
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# ============================================================
# Database Configuration
# ============================================================

# Database (single URL format)
# postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/<DATABASE_NAME>
DATABASE_URL=postgres://postgres:postgres@db:5432/project_a

# ============================================================
# Email Configuration
# ============================================================

# Development backend (prints emails to console)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Production backend (SMTP example)
# EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
# EMAIL_HOST=smtp.example.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=user@example.com
# EMAIL_HOST_PASSWORD=your_password
# DEFAULT_FROM_EMAIL=webmaster@example.com
```

---

## Running the Backend

Run backend and database only:

```bash
docker compose -f ../docker-compose.dev.yml up backend db
```

Run the full stack (frontend + backend + db):

```bash
docker compose -f ../docker-compose.dev.yml up --build
```

- Backend → http://localhost:8000  
- Frontend → http://localhost:5173

---

## Common Django Commands

```bash
docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
docker compose exec backend python manage.py collectstatic --noinput
```

---

## Testing (Planned)

Testing with Pytest and Django's test framework will be added in future iterations.