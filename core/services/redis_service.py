import redis
from django.conf import settings

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


def get_room_count(room_name):
    room_group_name = 'counter_%s' % room_name
    count = int(redis_instance.get(room_group_name) or 0)
    return count