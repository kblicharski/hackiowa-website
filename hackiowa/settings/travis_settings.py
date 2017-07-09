import os
from .base import get_secret

#Use the following live settings to build on Travis CI
if os.getenv('BUILD_ON_TRAVIS', None):
    SECRET_KEY = get_secret('SECRET_KEY')
    DEBUG = False
    TEMPLATE_DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'travis_ci_db',
            'USER': 'travis',
            'PASSWORD': '',
            'HOST': '127.0.0.1'
        }
    }
else:
    print('Error configuring CI settings')
