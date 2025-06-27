#!/bin/bash

set -e

PROJECT_NAME=test_project

# Color definitions
BLUE='\033[1;34m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[36m'
RESET='\033[0m'

# Function to print dynamic separator
print_separator() {
    printf '%*s\n' "$(tput cols)" '' | tr ' ' '═'
}

# Decorator functions
start_task() {
    echo ""
    print_separator
    echo -e "${BLUE}$1${RESET}"
    print_separator
}

end_task() {
    echo -e "${GREEN}$1${RESET}"
    echo ""
}

start_task "Testing template generation..."
rm -rf $PROJECT_NAME
uv tool run copier copy .. . \
    -d project_name="$PROJECT_NAME" \
    -d use_psql=False \
    -d use_drf=False \
    -d use_ruff=True \
    -d author_name="Artem Sokolov" \
    -d author_email="artem.sokolov.dev@gmail.com" \
    --defaults \
    --quiet 2>/dev/null
end_task "Template generated successfully!"

start_task "Setting up project environment..."
cd $PROJECT_NAME
mv .env.example .env
end_task "Environment configured!"

start_task "Running project setup..."
make project
end_task "Build completed successfully!"
