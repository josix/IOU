#!/bin/sh -e

poetry run pytest tests/
poetry run black iou tests --check
poetry run isort --check-only iou tests
poetry run flake8 iou/ tests/
poetry run mypy iou/ tests/
