"""
Settings for local development. Specific settings include DEBUG, log level,
and activation of developer tools. Overrides defaults from base.py.
"""

from .base import * 

# DEBUG CONFIGURATION
#
DEBUG = True

# APP CONFIGURATION
INSTALLED_APPS += [
    'debug_toolbar',
]


# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# DJANGO DEBUG TOOLBAR
INTERNAL_IPS = ['127.0.0.1']

LOCALHOST = ''
