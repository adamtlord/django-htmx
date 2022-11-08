import os
import sys
import json


AWS_REGION = os.getenv("AWS_REGION") or "eu-west-1"


def get_secret(secret_name, default_value=None, path="", required=True, region_name=AWS_REGION):
    if secret_name in os.environ:
        return os.environ[secret_name]

    else:
        if required:
            raise Exception(f"No value found for required environment variable {secret_name}")
        else:
            return default_value


# Get the ENV settings
ENV = get_secret("ENV")
if not ENV:
    raise Exception("Environment variable ENV is required!")

# Environment settings
DEBUG = False
IS_DEV = False
IS_STAGING = False
IS_PROD = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# project root and add "apps" to the path
PROJECT_ROOT = BASE_DIR
sys.path.append(os.path.join(PROJECT_ROOT, "apps/"))

SECRET_KEY = get_secret("SECRET_KEY")

# Initadmin Users (username, email, password)
ADMINS = (("admin", "admin@tivix.com", "admin!rules"),)

ALLOWED_HOSTS = []


# Env extensions
ENV_APPS = []
ENV_MIDDLEWARES = []


# Application definition
PROJECT_APPS = ["core", "marketing", "accounts", "demo"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "django.contrib.sites",
    "django_htmx",
    "django.contrib.humanize",
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
# Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]

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
## Databases
##
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "%s" % get_secret("POSTGRES_DB"),
        "USER": "%s" % get_secret("POSTGRES_USER"),
        "PASSWORD": "%s" % get_secret("POSTGRES_PASSWORD"),
        "HOST": "%s" % get_secret("POSTGRES_HOST"),
        "PORT": get_secret("POSTGRES_PORT", default_value=5432, required=False),
    },
}

# Data / file settings
DATA_UPLOAD_MAX_MEMORY_SIZE = 20971520  # 20MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 4194304  # 4mb
DATA_VOLUME = "/data"
UPLOADS_DIR_NAME = "uploads"
MEDIA_URL = "/%s/" % UPLOADS_DIR_NAME
MEDIA_ROOT = os.path.join(DATA_VOLUME, "%s" % UPLOADS_DIR_NAME)

STATIC_URL = "/static/"
STATIC_ROOT = "/static"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "src", "static"),
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # "compressor.finders.CompressorFinder",
]

# Log settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "[django] %(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"}
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "django": {
            "handlers": ["console"],
            "level": "ERROR",
        },
        "huey.consumer": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

if "test" in sys.argv:
    IS_TEST = True
    LOGGING["handlers"]["console"] = {"class": "logging.NullHandler"}


##
# Env overrides
##
# Per-env constants and overrides.
# If a setting is used by a single environment, needs to be overriden for a
# single environment, and isn't otherwise defined using os.getenv() or
# get_secret(), put it here.
if ENV == "dev":
    IS_DEV = True
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
    TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG


ENV_LOGGING = {"handlers": {}, "loggers": {}}


LOGGING["handlers"].update(ENV_LOGGING["handlers"])
LOGGING["loggers"].update(ENV_LOGGING["loggers"])
