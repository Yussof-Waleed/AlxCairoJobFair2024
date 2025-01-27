"""
WSGI config for jobfair project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
sys.path.append('/home/spyce/AlxCairoJobFair2024')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobfair.settings')

application = get_wsgi_application()
