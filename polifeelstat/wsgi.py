"""
WSGI config for polifeelstat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys
sys.path.append(' /Users/User/Desktop/polifeel/polifeelstat/polifeelstat')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polifeelstat.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
