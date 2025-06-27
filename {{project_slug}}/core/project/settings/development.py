EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    import debug_toolbar  # noqa
    from . import INSTALLED_APPS, MIDDLEWARE

    INSTALLED_APPS = INSTALLED_APPS + ["debug_toolbar"]
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE
    INTERNAL_IPS = ["127.0.0.1"]
except ImportError:
    pass
