#!/bin/bash

set -e

PROJECT_NAME=test_project

echo "🔨 Building Django Core Copier Template"

echo "📋 Testing template generation..."
rm -rf $PROJECT_NAME
uvx copier copy .. . \
    -d project_name="$PROJECT_NAME" \
    -d author_name="Artem Sokolov" \
    -d author_email="artem.sokolov.dev@gmail.com" \
    --defaults

cd $PROJECT_NAME

mv .env.example .env

make project
