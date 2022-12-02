import os
import sys
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# Get the ENV settings
ENV = os.getenv("ENV")
if not ENV:
    raise Exception("Environment variable ENV is required!")

# Environment settings
DEBUG = os.getenv("DEBUG")
IS_DEV = False
IS_STAGING = False
IS_PROD = False

# project root and add "apps" to the path
PROJECT_ROOT = BASE_DIR
sys.path.append(os.path.join(PROJECT_ROOT, "apps/"))

SECRET_KEY = os.getenv("SECRET_KEY")

# Initadmin Users (username, email, password)
ADMINS = (("admin", "admin@tivix.com", "admin!rules"),)

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', '').split(' ')

# Env extensions
ENV_APPS = []
ENV_MIDDLEWARES = []


# Application definition
PROJECT_APPS = ["core", "marketing", "accounts", "demo"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "django.contrib.sites",
    "django_htmx",
]

INSTALLED_APPS += ENV_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

MIDDLEWARE = ENV_MIDDLEWARES + MIDDLEWARE

ROOT_URLCONF = "urls"

TEMPLATES_DIR = os.path.join(BASE_DIR, "src", "templates")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]


AUTH_USER_MODEL = "accounts.User"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/demo/"

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1

##
#  Databases
##
DATABASES = {
    "default": dj_database_url.config(conn_max_age=600)
}

# Data / file settings
DATA_UPLOAD_MAX_MEMORY_SIZE = 20971520  # 20MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 4194304  # 4mb

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / 'data/staticfiles'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "src", "static"),
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'data/mediafiles'

##
# Env overrides
##

if ENV == "dev":
    IS_DEV = True
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
    TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG
