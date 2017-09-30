from .base_settings import *

import os
from urllib import parse

import dj_database_url

DEBUG = True
ALLOWED_HOSTS = [
    "streamxyz.herokuapp.com", "www.streamxyz.com", "streamxyz.com"]

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


redis_url = parse.urlparse(os.environ.get('REDIS_URL'))
CACHES = {
    "default": {
         "BACKEND": "redis_cache.RedisCache",
         "LOCATION": "{0}:{1}".format(redis_url.hostname, redis_url.port),
         "OPTIONS": {
             "PASSWORD": redis_url.password,
             "DB": 0,
         }
    }
}
