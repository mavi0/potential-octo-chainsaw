#!/bin/bash
nohup python3 cleanup.py &
gunicorn -b :5050 --access-logfile - --error-logfile - server:app