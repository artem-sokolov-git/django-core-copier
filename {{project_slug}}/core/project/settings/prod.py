from .base import *

DEBUG = False

if not env("ALLOWED_HOSTS", default=""):
    raise ValueError("ALLOWED_HOSTS environment variable must be set in production")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
