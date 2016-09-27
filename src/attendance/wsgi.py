"""
WSGI config for openservices project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, '../..')))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendance.settings")

application = get_wsgi_application()
