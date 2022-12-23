"""
Django settings for aberdeen project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()



PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'users.apps.UsersConfig',
    'django.contrib.contenttypes',
    'user_sessions',
    'django.contrib.sessions',
    'django.contrib.messages',
    
    'django.contrib.sites',
    
    'django.contrib.staticfiles',
    'social_django',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_email',
    'two_factor',
    'two_factor.plugins.phonenumber',
    'two_factor.plugins.email',

    'provider',


    'bootstrapform',

 # The following apps are required:

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.okta',
    'allauth.socialaccount.providers.google',



    
]

SITE_ID = 1

# Provider specific settings


SOCIALACCOUNT_PROVIDERS = {
    
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    
    
    
    'okta': {
        'OKTA_BASE_URL': 'okta.dhkdemo.com',
        'APP': {
            'client_id': '0oa4n2ii2dJLxQWxi1d7',
            'secret': 'IP1TMwh8dxeI4gX8wQj4BH2wW54qcxDCKu7rpOMY',
            'key': ''
        }
    },

    'iamsmart': {
        'iamsmart_BASE_URL': 'okta.dhkdemo.com',
        'APP': {
            'client_id': '0oa6g0nc6j0fqMDRO1d7',
            'secret': 'c2rZ3uxGP9yDDjnmSVcAct44Q81guLNZhBzM0Eej',
            'key': ''
        }
    },




}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'user_sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'two_factor.middleware.threadlocals.ThreadLocals',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aberdeen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_PATH, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',


                 # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'aberdeen.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'two_factor': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',


# Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

)

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL =   'two_factor:login'
LOGIN_REDIRECT_URL =  'two_factor:profile'

INTERNAL_IPS = ('127.0.0.1',)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



TWO_FACTOR_SMS_GATEWAY = str(os.getenv('TWILIO_SMS_GATEWAY'))
PHONENUMBER_DEFAULT_REGION = 'HK'

TWILIO_ACCOUNT_SID = str(os.getenv('TWILIO_ACCOUNT_SID'))
TWILIO_AUTH_TOKEN = str(os.getenv('TWILIO_AUTH_TOKEN'))
TWILIO_CALLER_ID = str(os.getenv('TWILIO_CALLER_ID'))

IAM_SMART_ID = str(os.getenv('IAM_SMART_ID'))
IAM_SMART_SECRET = str(os.getenv('IAM_SMART_SECRET'))

TWO_FACTOR_REMEMBER_COOKIE_AGE = 120  # Set to 2 minute for testing

SESSION_ENGINE = 'user_sessions.backends.db'

DEFAULT_FROM_EMAIL = str(os.getenv('EMAIL_USER'))

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST_USER = str(os.getenv('EMAIL_USER')) 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587 
EMAIL_USE_TLS = True 
EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_PASSWORD'))

SILENCED_SYSTEM_CHECKS = ['admin.E410']

