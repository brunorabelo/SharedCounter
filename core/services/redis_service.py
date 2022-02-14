import functools

import redis
from django.conf import settings

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


# def _get_group_name(room_name: str) -> str:
#     group_name = room_name if room_name.startswith('counter_') else f'counter_{room_name.upper()}'
#     return group_name

def redis_group_name(func):
    @functools.wraps(func)
    def inner(room_name, **kwargs):
        group_name = room_name if room_name.startswith('counter_') else f'counter_{room_name.upper()}'
        return func(group_name, **kwargs)

    return inner


@redis_group_name
def get_group_count(room_name: str) -> int:
    count = int(redis_instance.get(room_name) or 0)
    return count


@redis_group_name
def inc_group_counter(room_name: str) -> int:
    redis_instance.incr(room_name)
    return get_group_count(room_name)


@redis_group_name
def set_or_reset_redis_group(room_name: str, *, count: int = 0) -> None:
    redis_instance.set(room_name, count)
