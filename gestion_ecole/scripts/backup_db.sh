#!/usr/bin/env bash
set -e
python manage.py dumpdata --indent 2 > backups/demo_backup.json
