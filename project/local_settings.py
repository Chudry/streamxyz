from .base_settings import *


# Database

# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
ALLOWED_HOSTS = ["*", "68165119.ngrok.io"]

DEBUG = True


ENVIRONMENT = 'local'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
