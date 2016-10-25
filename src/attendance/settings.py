'''
Django settings for attendance project.
'''

import os

from IPy import IP


class IPList(list):

    def __init__(self, addresses):
        super(IPList, self).__init__()
        for address in addresses:
            self.append(IP(address))

    def __contains__(self, address):
        for net in self:
            if address in net:
                return True
        return False

BASE_DIR = os.path.abspath(os.path.join(__file__, '../../..'))

SITE_ID = os.environ.get('DJANGO_SITE_ID')

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = 'DJANGO_DEBUG' in os.environ
ADMINS = (
    ('Michael Fladischer', 'michael@openservices.at'),
)
EMAIL_HOST = 'localhost'
SERVER_EMAIL = 'django@qraz.at'

if 'DJANGO_INTERNAL_IPS' in os.environ:
    INTERNAL_IPS = IPList(os.environ.get('DJANGO_INTERNAL_IPS', '127.0.0.1,::1').split(','))

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'attendance.base',
    'django.contrib.admin',
    'django_extensions',
    'crispy_forms',
    'guardian',
    'debug_toolbar',
    'django_python3_ldap',
    'reversion',
    'rest_framework',
    'rest_framework.authtoken',
    'oauth2_provider',
    'corsheaders',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'attendance.urls'

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

WSGI_APPLICATION = 'attendance.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'DJANGO_DATABASES_DEFAULT_ENGINE',
            'django.db.backends.sqlite3'
        ),
        'NAME': os.environ.get(
            'DJANGO_DATABASES_DEFAULT_NAME',
            os.path.join(BASE_DIR, 'db.sqlite3')
        ),
        'USER': os.environ.get(
            'DJANGO_DATABASES_DEFAULT_USER',
            ''
        ),
        'PASSWORD': os.environ.get(
            'DJANGO_DATABASES_DEFAULT_PASSWORD',
            ''
        ),
        'HOST': os.environ.get(
            'DJANGO_DATABASES_DEFAULT_HOST',
            ''
        ),
        'PORT': int(os.environ.get(
            'DJANGO_DATABASES_DEFAULT_PORT',
            '0'
        )),
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
        'KEY_PREFIX': __package__,
    }
}
CACHE_MIDDLEWARE_SECONDS = 60
CACHE_MIDDLEWARE_KEY_PREFIX = SITE_ID

LANGUAGE_CODE = 'de-at'
TIME_ZONE = 'Europe/Vienna'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_python3_ldap.auth.LDAPBackend',
    'guardian.backends.ObjectPermissionBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# The URL of the LDAP server.
LDAP_AUTH_URL = os.environ.get('DJANGO_LDAP_AUTH_URL')

# Initiate TLS on connection.
LDAP_AUTH_USE_TLS = 'DJANGO_LDAP_AUTH_USE_TLS' in os.environ

# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = os.environ.get('DJANGO_LDAP_AUTH_SEARCH_BASE')

# The LDAP class that represents a user.
LDAP_AUTH_OBJECT_CLASS = 'inetOrgPerson'

# User model fields mapped to the LDAP
# attributes that represent them.
LDAP_AUTH_USER_FIELDS = {
    'username': 'cn',
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
}

# A tuple of django model fields used to uniquely identify a user.
LDAP_AUTH_USER_LOOKUP_FIELDS = ('username',)

# Path to a callable that takes a dict of {model_field_name: value},
# returning a dict of clean model data.
# Use this to customize how data loaded from LDAP is saved to the User model.
LDAP_AUTH_CLEAN_USER_DATA = 'django_python3_ldap.utils.clean_user_data'

# Path to a callable that takes a user model and a dict of {ldap_field_name: [value]},
# and saves any additional user relationships based on the LDAP data.
# Use this to customize how data loaded from LDAP is saved to User model relations.
# For customizing non-related User model fields, use LDAP_AUTH_CLEAN_USER_DATA.
LDAP_AUTH_SYNC_USER_RELATIONS = 'django_python3_ldap.utils.sync_user_relations'

# Path to a callable that takes a dict of {ldap_field_name: value},
# returning a list of [ldap_search_filter]. The search filters will then be AND'd
# together when creating the final search filter.
LDAP_AUTH_FORMAT_SEARCH_FILTERS = 'attendance.ldap.group_membership_filter'

# Path to a callable that takes a dict of {model_field_name: value}, and returns
# a string of the username to bind to the LDAP server.
# Use this to support different types of LDAP server.
LDAP_AUTH_FORMAT_USERNAME = 'django_python3_ldap.utils.format_username_openldap'

# Sets the login domain for Active Directory users.
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = None

# The LDAP username and password of a user for authenticating the `ldap_sync_users`
# management command. Set to None if you allow anonymous queries.
LDAP_AUTH_CONNECTION_USERNAME = os.environ.get('DJANGO_LDAP_AUTH_CONNECTION_USERNAME', None)
LDAP_AUTH_CONNECTION_PASSWORD = os.environ.get('DJANGO_LDAP_AUTH_CONNECTION_PASSWORD', None)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGE_SIZE': 10
}

RUNSERVERPLUS_SERVER_ADDRESS_PORT = '0.0.0.0:8088'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django_python3_ldap': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

from debug_toolbar.panels.headers import HeadersPanel

HeadersPanel.ENVIRON_FILTER.add('GEOIP_ADDR')
HeadersPanel.ENVIRON_FILTER.add('GEOIP_CONTINENT_CODE')
HeadersPanel.ENVIRON_FILTER.add('GEOIP_COUNTRY_CODE')
HeadersPanel.ENVIRON_FILTER.add('GEOIP_COUNTRY_NAME')
