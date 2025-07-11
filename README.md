# Django Core Copier

A Copier template for Django projects with modern tooling and best practices.

## Features

- Django with REST Framework support
- Modern Python tooling (Ruff, pytest, pre-commit)
- PostgreSQL database support
- Docker configuration
- Comprehensive settings structure
- API structure with versioning
- Pre-configured linting and type checking

## Usage

### With uvx (recommended)

```bash
uvx copier copy https://github.com/your-username/django-core-copier your-project-name
```

### With copier

```bash
copier copy https://github.com/your-username/django-core-copier your-project-name
```

## Template Options

- **Project name and description**
- **Python version** (default: 3.12)
- **Django REST Framework** (optional)
- **Ruff linter** (optional)
- **PostgreSQL** (optional)

## Requirements

- Python 3.12+
- uvx or copier
