#!/usr/bin/env python
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'belajar_django.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Could not import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        )

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
