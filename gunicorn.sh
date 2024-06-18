#!/bin/sh
gunicorn --chdir /app main:app -w 2 --threads 2 --timeout 600 --log-level debug -b 0.0.0.0:9000
