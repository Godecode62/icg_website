from pathlib import Path
from decouple import config
import dj_database_url
import os
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
if not SECRET_KEY or len(SECRET_KEY) < 20:
    raise ImproperlyConfigured('SECRET_KEY not configured or too short in .env')

DEBUG = True

ALLOWED_HOSTS = [
    "icguinea.com",
    'www.icguinea.com',
    'icg-6bg2.onrender.com',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'appli',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'icgProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'icgProject.wsgi.application'

DATABASES = {
    'default': dj_database_url.parse(
        config('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

CLOUDFLARE_R2_BUCKET = config('CLOUDFLARE_R2_BUCKET')
CLOUDFLARE_R2_ACCESS_KEY = config('CLOUDFLARE_R2_ACCESS_KEY')
CLOUDFLARE_R2_SECRET_KEY = config('CLOUDFLARE_R2_SECRET_KEY')
CLOUDFLARE_R2_BUCKET_ENDPOINT = config('CLOUDFLARE_R2_BUCKET_ENDPOINT')

_R2_ENDPOINT_URL = CLOUDFLARE_R2_BUCKET_ENDPOINT
if not _R2_ENDPOINT_URL.endswith('/'):
    _R2_ENDPOINT_URL += '/'

STATIC_URL = f"{_R2_ENDPOINT_URL}{CLOUDFLARE_R2_BUCKET}/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = f"{_R2_ENDPOINT_URL}{CLOUDFLARE_R2_BUCKET}/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CLOUDFLARE_R2_CONFIG_OPTIONS = {
    'bucket_name': CLOUDFLARE_R2_BUCKET,
    'access_key': CLOUDFLARE_R2_ACCESS_KEY,
    'secret_key': CLOUDFLARE_R2_SECRET_KEY,
    'endpoint_url': CLOUDFLARE_R2_BUCKET_ENDPOINT,
    'default_acl': 'public-read',
    'file_overwrite': False,
    'signature_version': 's3v4',
    'querystring_auth': False,
    'region_name': None,
}

STORAGES = {
    'default': {
        'BACKEND': 'helpers.cloudflare.storages.MediaFileStorage',
        'OPTIONS': CLOUDFLARE_R2_CONFIG_OPTIONS,
    },
    'staticfiles': {
        'BACKEND': 'helpers.cloudflare.storages.StaticFileStorage',
        'OPTIONS': CLOUDFLARE_R2_CONFIG_OPTIONS,
    }
}

DEFAULT_FILE_STORAGE = 'helpers.cloudflare.storages.MediaFileStorage'
STATICFILES_STORAGE = 'helpers.cloudflare.storages.StaticFileStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_AGE = 3600 * 24
SESSION_SAVE_EVERY_REQUEST = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'