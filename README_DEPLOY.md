Deployment notes — quick steps to host the site (Heroku / Render / VPS)

1. Set environment variables:
   - DJANGO_SECRET_KEY (set a strong secret)
   - DJANGO_DEBUG (False in production)
   - DJANGO_ALLOWED_HOSTS (comma-separated domains)
   - EMAIL_HOST_USER / EMAIL_HOST_PASSWORD (for emails)

2. Install requirements:
   pip install -r requirements.txt

3. Collect static files:
   python manage.py collectstatic --noinput

4. Create database migrations and migrate:
   python manage.py makemigrations
   python manage.py migrate

5. (Heroku/Render) Push code; set buildpacks if needed. Procfile is included.

6. Configure media files: use an object store (S3) or serve via the server for small sites.

7. For a simple deployment on a VPS: use gunicorn + nginx, create systemd service pointing to gunicorn, and serve staticfiles from /staticfiles.

Notes:

- This project currently uses SQLite by default. For production, switch to PostgreSQL and update DATABASES.
- Remember to set DEBUG=False and add your domain to ALLOWED_HOSTS.
