from {{prname}}.settings import *


STATIC_ROOT = '/home/{{prname}}/webstatic'
MEDIA_ROOT = '/home/{{prname}}/webstatic/media'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{prname}}',
        'USER': '{{prname}}',
        'PASSWORD': '{{prname}}',
        'HOST': '',
        'PORT': '',
    }
}
