"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '810y_zla$zy-^#_-atty7is_ivige1)*&x&b25w1n2_d9kmzz7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'clientes',
    'mysite',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

    },

    'mssql': {
        'NAME': 'CODIGOS',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'plan01spo15',
        'USER': 'planejamento',
        'PASSWORD': 'pl@n1234',
        #'DNS': 'SQL_DW',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',

        },
    },

    'mssql_': {
        'NAME': 'Controladoria',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'plan01spo15',
        'USER': 'planejamento',
        'PASSWORD': 'pl@n1234',
        #'DNS': 'SQL_DW',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',

        },
    },

    'func_funcionarios': {
        'NAME': 'DW',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'plan01spo15',
        'USER': 'planejamento',
        'PASSWORD': 'pl@n1234',
        # 'DNS': 'SQL_DW',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',

        },
    },

    'premiacao': {
        'NAME': 'PRODUCAO',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'plan01spo15',
        'USER': 'usr_mis',
        'PASSWORD': 'pl@@n1234',
        # 'DNS': 'SQL_DW',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',

        },
    },


}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = 'media'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = 'person_list'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    'statics',
]

DATABASE_ROUTERS = ['mysite.db_route.DatabaseRouter']