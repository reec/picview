# Copy this file to picview_settings.py and edit these

# This should be the path to a directory with albums - directories with image files in them.
PICVIEW_DIR = '/srv/photos'

FILES_PER_PAGE = 24

# If you want logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s - %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'picview': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

# You don't need to change anything past here!
IMAGE_EXTS = ('jpg', 'jpeg', 'png', 'gif', 'bmp')
VIDEO_EXTS = ('mpg', 'mpeg', '3gp', 'mkv', '.divx', 'xvid')