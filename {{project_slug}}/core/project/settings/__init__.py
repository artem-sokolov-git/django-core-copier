from pathlib import Path

import environ
from split_settings.tools import include

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Инициализация environ
env = environ.Env(
    # Настройки окружения
    DJANGO_ENV=(str, "dev"),
)

# Чтение .env файла
environ.Env.read_env(BASE_DIR / ".env")

# Определение окружения из переменной среды
ENVIRONMENT = env("DJANGO_ENV")

# Экспорт для использования в других модулях настроек
__all__ = ["env", "BASE_DIR", "ENVIRONMENT"]

# Включение настроек на основе окружения
include(
    "base.py",
    "databases.py",
    f"{ENVIRONMENT}.py",
)
