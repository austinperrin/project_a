from decouple import config
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DJANGO_DEBUG', default=True)

# Handle ALLOWED_HOSTS
ALLOWED_HOSTS_FILE = BASE_DIR / config('DJANGO_ALLOWED_HOSTS_FILE', default='.env.hosts')

if not ALLOWED_HOSTS_FILE.exists():
    raise FileNotFoundError(f"DJANGO_ALLOWED_HOSTS_FILE '{ALLOWED_HOSTS_FILE}' not found.")

with open(ALLOWED_HOSTS_FILE) as f:
    ALLOWED_HOSTS = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith('#')
    ]

if not ALLOWED_HOSTS:
    raise ValueError(f"DJANGO_ALLOWED_HOSTS_FILE '{ALLOWED_HOSTS_FILE}' is empty or contains only comments.")

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST', default='db'),
        'PORT': config('POSTGRES_PORT', cast=int, default=5432),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / "staticfiles"

# No need for STATICFILES_DIRS in production since files are collected
STATICFILES_DIRS = []

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

EMAIL_BACKEND = config("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = config("EMAIL_HOST", default="")
EMAIL_PORT = config("EMAIL_PORT", cast=int, default=587)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=True)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="")
