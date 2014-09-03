import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.join(BASE_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
DATABASE_PATH = os.path.join(PROJECT_PATH, 'pdxdjango.db')
TEMPLATE_DIRS = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
STATIC_DIRS = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'static'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
        #'ATOMIC_REQUESTS': True
    }
}


STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    STATIC_DIRS,
)
STATIC_URL = '/static/'

MEDIA_ROOT = '/websites/pdxcodeguild.com/media/'
MEDIA_URL = '/media/'

PYBB_ATTACHMENT_UPLOAD_TO = '/websites/pdxcodeguild.com/media/attachments/'