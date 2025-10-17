# Backend - Project A

This is the Django REST API backend for Project A.  
It powers the core business logic, authentication, and data layer.  
For full project setup, see [Project Root README](../README.md).

---

## Tech Stack
- Django & Django REST Framework
- Gunicorn (production)
- PostgreSQL
- django-decouple
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

```bash
# Django
DJANGO_SETTINGS_MODULE=config.settings.dev
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True # Set to False in production

# Django file containing allowed hosts (newline separated)
DJANGO_ALLOWED_HOSTS_FILE=.env.hosts

# Database
POSTGRES_DB=your_db_name
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
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

## Troubleshooting

| Issue                     | Cause                             | Fix                                                       |
|---------------------------|------------------------------------|------------------------------------------------------------|
| `ALLOWED_HOSTS` error     | `.env.hosts` missing or empty     | Add `localhost` or domain                                  |
| DB connection error       | DB not ready or wrong credentials | Check POSTGRES_* vars                                      |
| Static files missing      | `collectstatic` not run           | Run `collectstatic` in container                            |

---

## Testing (Planned)

Testing with Pytest and Django's test framework will be added in future iterations.