"""
Django settings for alex_project project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os, environ

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path helper
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  '..', x)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(env('SECRET_KEY', default='UajFCuyjDKmWHe29neauXzHi9eZoRXr6RMbT5JyAdPiACBP7Cra2'))

# SECURITY WARNING: don't run with debug turned on in production!

if os.environ.get('ENV') == 'PRODUCTION':
    DEBUG = env.bool('DEBUG', default=False)
else:
    DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS',
                         default=['alassane.herokuapp.com',
                                  'www.alassane.herokuapp.com',
                                  '*',
                                  'localhost'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'blog',
    'debug_toolbar',
    'bootstrap3',
    # 'django_s3_storage',
    'storages',
]

SITE_ID = 5

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
]

ROOT_URLCONF = 'alex_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/'),
        ],
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

WSGI_APPLICATION = 'alex_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Africa/Casablanca'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = location('staticfiles')

STATICFILES_DIRS = [
    location("static/"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# for debug_toolbar
INTERNAL_IPS = ['127.0.0.1']


if os.environ.get('ENV') == 'PRODUCTION':
    """ Sometimes Django apps are deployed at a particular prefix
    (or “subdirectory”) on a domain e.g. http://example.com/my-app/ rather than
    just http://example.com. In this case you would normally use Django’s
    FORCE_SCRIPT_NAME setting to tell the application where it is located
    """
    # FORCE_SCRIPT_NAME = '/blog'
    # Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'
    STATIC_ROOT = location('staticfiles')

    STATICFILES_DIRS = (
        location('static'),
    )

    # """ DROPBOX CONFIGURATION """
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'

    DROPBOX_OAUTH2_TOKEN = "QH8Mis-t1EAAAAAAAAAAEFd2xvWbp5-DkSc-7W5xzz-V9Me_EnzRMUXALHxeq-Oc"

    DROPBOX_ROOT_PATH = '/blog/media/'

    DROPBOX_OAUTH2_KEY = "x6wtdz1yz5xe05j"

    DROPBOX_OAUTH2_SECRET = "9nczp780kbzbgah"

    MEDIA_URL = '/blog/media/'
    MEDIA_ROOT = 'blog/media/'

    ADMIN_MEDIA_PREFIX = '/blog/media/'
    # "************ END DROPBOX CONFIGURATION ************"

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
    # whitenoise.storage.CompressedManifestStaticFilesStorage
    import dj_database_url

    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)


# Django logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                       'pathname=%(pathname)s lineno=%(lineno)s '
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
