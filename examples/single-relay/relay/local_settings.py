import uuid

TIME_ZONE = 'Europe/London'
MEMCACHE_HOSTS = ['127.0.0.1:11211']
LOG_RENDERING_PERFORMANCE = False
LOG_CACHE_PERFORMANCE = False
DEBUG = False
SECRET_KEY = str(uuid.uuid4())
CARBONLINK_HOSTS=["127.0.0.1:2104:1", "127.0.0.1:2204:2", "127.0.0.1:2304:3", "127.0.0.1:2404:4"]