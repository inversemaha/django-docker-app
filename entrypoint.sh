#!/bin/sh
if [ ! -f "manage.py" ]; then
  django-admin startproject app .
fi
exec "$@"
