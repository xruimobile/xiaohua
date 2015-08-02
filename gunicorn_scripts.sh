#!/bin/sh
nohup gunicorn xiaohua.wsgi:application -b 127.0.0.1:8001 2>&1 &
