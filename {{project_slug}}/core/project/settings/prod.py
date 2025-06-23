from .base import *

# Production settings
DEBUG = False

# ALLOWED_HOSTS must be set in production via environment variable
# No default value to force explicit configuration in production
if not env("ALLOWED_HOSTS", default=""):
    raise ValueError("ALLOWED_HOSTS environment variable must be set in production")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# HTTPS settings (uncomment when HTTPS is configured)
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
