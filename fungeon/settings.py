# LOCAL SETTINGS - SAMPLE
DEBUG = True

DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.sqlite3",
      "NAME": "dev.db",
  }
}

ALLOWED_HOSTS = ["localhost"]

TIME_ZONE = "America/Denver"

LANGUAGE_CODE = "en-us"

SECRET_KEY = "8p#n50)g9vj)twmkaz%-0$1+177to23--=_a3-+&+$3s%&_upk"

CONTACT_EMAIL = "timpviewfungeon@gmail.com"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
  "version": 1,
    "disable_existing_loggers": False,
    "filters": {
      "require_debug_false": {
        "()": "django.utils.log.RequireDebugFalse"
      }
    },
    "handlers": {
      "mail_admins": {
        "level": "ERROR",
          "filters": ["require_debug_false"],
          "class": "django.utils.log.AdminEmailHandler"
      }
    },
    "loggers": {
      "django.request": {
        "handlers": ["mail_admins"],
        "level": "ERROR",
          "propagate": True,
        },
  }
}


# STATIC SETTINGS
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PACKAGE_ROOT

SITE_ID = int(os.environ.get("SITE_ID", 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static", "dist"),
]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PACKAGE_ROOT, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "fungeon.context_processors.settings"
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "fungeon.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "fungeon.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",

    # templates
    "bootstrapform",
    "pinax.templates",

    # external
    "pinax.blog",
    "pinax.images",
    "pinax.webanalytics",

    # project
    "fungeon",
]

# Grab your own GA id and replace UA-XXXXXXXX or use another
# pinax-webanalytics provider, or roll your own template.
# PINAX_WEBANALYTICS_SETTINGS = {
#     "google": {
#         2: "UA-XXXXXXXX",
#     }
# }

# Turn off the admin js; probably should remove from the form
PINAX_BLOG_ADMIN_JS = []

ADMIN_URL = "admin:index"

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
