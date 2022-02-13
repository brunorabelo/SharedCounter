import redis
from django.conf import settings

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


def get_group_count(group_name: str) -> int:
    count = int(redis_instance.get(group_name) or 0)
    return count


def inc_group_counter(group_name: str) -> int:
    redis_instance.incr(group_name)
    return get_group_count(group_name)
