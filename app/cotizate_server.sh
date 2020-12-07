#!/bin/sh

gunicorn --bind 0.0.0.0:application api.wsgi:application
