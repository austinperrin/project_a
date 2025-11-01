from .base import *


# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [BASE_DIR / "static", ]

# No need for STATIC_ROOT in development
STATIC_ROOT = None

EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
