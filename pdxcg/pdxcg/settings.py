"""
Django settings for pdxcg project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    ('Christopher Jones', 'chris@chrischarlesjones.net'),
)
MANAGERS = ADMINS

SECRET_KEY = open(os.path.expanduser('~/.gallery-secret')).read().strip()

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'fluent_comments',
    'threadedcomments',
    'django.contrib.comments',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'pdxcodeguild',
    'crispy_forms',
    'south',
    'sekizai',
    'pdx_blog',
    'markdown',
    'markitup',
    'pybb',
    'froala_editor',
)

MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})

MARKITUP_SET = 'markitup/sets/markdown'

MARKITUP_SKIN = 'markitup/skins/markitup'

JQUERY_URL = None

COMMENTS_APP = 'fluent_comments'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pybb.middleware.PybbMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    'pybb.context_processors.processor',
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

PYBB_ATTACHMENT_SIZE_LIMIT = 40960 * 40960
PYBB_ATTACHMENT_ENABLE = True

ROOT_URLCONF = 'pdxcg.urls'

WSGI_APPLICATION = 'pdxcg.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
SITE_ID = 1
FLUENT_COMMENTS_EXCLUDE_FIELDS = ('name', 'email', 'title', 'url')

LOGIN_REDIRECT_URL = 'mainpage'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

try:
    from local_settings import *
except ImportError:
    pass