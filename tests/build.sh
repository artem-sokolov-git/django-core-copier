#!/bin/bash

set -e

PROJECT_NAME=test_project

rm -rf $PROJECT_NAME
uvx copier copy .. . \
    -d project_name="$PROJECT_NAME" \
    -d database=mysql \
    --trust \
    --defaults