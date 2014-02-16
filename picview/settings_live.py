from picview.settings import *
# You're going to want a settings_local_live.py too, to specify logging paths and stuff

DEBUG = False

# Set this to something appropriate in your settings_local_live.py
ALLOWED_HOSTS = '*'

CACHES['default']['KEY_PREFIX'] = 'live'