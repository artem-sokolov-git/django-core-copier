#!/usr/bin/env python3
import os
import secrets
import string
from pathlib import Path


def generate_secret_key():
    chars = string.ascii_letters + string.digits + "!@#$%^&*(-_=+)"
    return "".join(secrets.choice(chars) for _ in range(50))


def load_env_file(env_path):
    """Load .env file into environment variables"""
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()


env_file = Path(".env")

if not env_file.exists():
    print("Error: .env file not found")
    exit(1)

lines = env_file.read_text().splitlines()

for i, line in enumerate(lines):
    if line.startswith("SECRET_KEY="):
        current_value = line.split("=", 1)[1] if "=" in line else ""

        if current_value.strip():
            print("SECRET_KEY already exists")
            # Load env and show current key
            load_env_file(env_file)
            print(f"Current SECRET_KEY: {os.getenv('SECRET_KEY', 'Not found')}")
            exit(0)

        new_secret_key = generate_secret_key()
        lines[i] = f"SECRET_KEY={new_secret_key}"

        env_file.write_text("\n".join(lines) + "\n")
        print("SECRET_KEY generated successfully")
        # Load env and show new key
        load_env_file(env_file)
        print(f"Generated SECRET_KEY: {os.getenv('SECRET_KEY', 'Not found')}")
        exit(0)

print("SECRET_KEY= not found in .env file")
exit(1)
