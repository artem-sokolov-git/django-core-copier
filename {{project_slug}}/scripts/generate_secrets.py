#!/usr/bin/env python3
"""
Script to generate secrets for Django project.
Replaces placeholder values in .env file with randomly generated secrets.
"""

import secrets
import string
from pathlib import Path


def generate_password(length=16):
    """Generate a shorter, more readable password.

    Uses only alphanumeric characters to avoid shell escaping issues
    and make passwords easier to read and type manually if needed.
    """
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def generate_secret_key():
    """Generate Django SECRET_KEY."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*(-_=+)"
    return "".join(secrets.choice(chars) for _ in range(50))


def main():
    """Main function to generate secrets in .env file."""
    project_root = Path(__file__).parent.parent
    env_file = project_root / ".env"

    if not env_file.exists():
        print(f"Error: .env file not found at {env_file}")
        print("Please create .env file from .env.example first")
        return 1

    with open(env_file, encoding="utf-8") as f:
        content = f.read()

    changes_made = False

    if "password_must_be_generated_by_script" in content:
        password = generate_password()
        content = content.replace("password_must_be_generated_by_script", password)
        changes_made = True
        print("✓ Generated new database password")

    if "secret_key_must_be_generated_by_script" in content:
        secret_key = generate_secret_key()
        content = content.replace("secret_key_must_be_generated_by_script", secret_key)
        changes_made = True
        print("✓ Generated new Django SECRET_KEY")

    if changes_made:
        with open(env_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✓ Secrets updated in {env_file}")
    else:
        print("No placeholders found to replace")

    return 0


if __name__ == "__main__":
    exit(main())
