import functools

from core.services import connection_service


def touch_connection(func):
    @functools.wraps(func)
    def inner(consumer, text_data, *args, **kwargs):
        connection_service.touch_connection(consumer.channel_name)
        if text_data == '"heartbeat"':
            return
        return func(consumer, text_data, *args, **kwargs)

    return inner