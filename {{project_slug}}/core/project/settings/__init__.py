import environ
from split_settings.tools import include

# Инициализация environ
env = environ.Env(
    DJANGO_ENV=(str, 'dev')  # значение по умолчанию
)

# Определение окружения из переменной среды
ENVIRONMENT = env('DJANGO_ENV')

# Включение настроек на основе окружения
include(
    'base.py',
    'databases.py',
    f'{ENVIRONMENT}.py',
)
