#!/bin/sh -e

poetry run isort iou tests
poetry run black iou tests
