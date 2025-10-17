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
STATICFILES_DIRS = [BASE_DIR / "static", ]

# No need for STATIC_ROOT in development
STATIC_ROOT = None

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
