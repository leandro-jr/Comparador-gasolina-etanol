"""
WSGI config for fulltank project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
import time
import traceback
import signal

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/leandro/CS50W/comparador/project_final/fulltank')
# adjust the Python version in the line below as needed
sys.path.append('/home/leandro/CS50W/comparador/lpdaj/project_final/.venv/lib/python3.6/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fulltank.settings")

try:
    print('wsgi1')
    application = get_wsgi_application()
    print('wsgi2')
except Exception:
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)