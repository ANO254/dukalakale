import os
import sys
from pathlib import Path

# Add project root to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duka.settings')

# Set required environment variables for Vercel
os.environ.setdefault('DJANGO_SECRET_KEY', os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-dev-key-for-vercel'))
os.environ.setdefault('DJANGO_DEBUG', 'False')
os.environ.setdefault('DJANGO_ALLOWED_HOSTS', os.environ.get('DJANGO_ALLOWED_HOSTS', '.vercel.app'))

import django
django.setup()

from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application

# Get WSGI application
application = get_wsgi_application()

def handler(request, context):
    """Vercel serverless handler"""
    wsgi_handler = WSGIHandler()
    
    # Build environ dict from Vercel request
    environ = {
        'REQUEST_METHOD': request.method,
        'PATH_INFO': request.path,
        'QUERY_STRING': request.query or '',
        'CONTENT_TYPE': request.headers.get('content-type', ''),
        'CONTENT_LENGTH': '',
        'SERVER_NAME': 'localhost',
        'SERVER_PORT': '443',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': __import__('io').BytesIO(request.body or b''),
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': True,
        'wsgi.run_once': True,
    }
    
    # Add headers
    for key, value in request.headers.items():
        environ[f'HTTP_{key.upper().replace("-", "_")}'] = value
    
    # Create response start callback
    response_headers = {}
    def start_response(status, headers):
        response_headers.update(headers)
        return lambda x: None
    
    # Get response from Django
    response = wsgi_handler(environ, start_response)
    
    # Collect response content
    content = b''.join(response)
    
    return content, response_headers