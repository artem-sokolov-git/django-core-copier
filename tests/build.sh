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
uv tool run copier copy .. . \
    -d project_name="$PROJECT_NAME" \
    --trust \
    -w
end_task "Template generated successfully!"
