from core.models import Room, Connection
from core.services import room_service


def new_connection(ws_name: str, room_name: str) -> Connection:
    room = room_service.get_room(room_name)
    if not room:
        raise Exception("Room doesn't exist!")
    if Connection.objects.filter(websocket=ws_name).exists():
        # TODO: logar esse evento
        pass
    conn = Connection(room=room, user="", alive=True, websocket=ws_name)
    conn.save()
    return conn


def kill_connection(conn: Connection) -> None:
    conn.kill()


def set_username_connection(conn: Connection, username: str) -> None:
    conn.set_username(username)


def touch_connection(conn: Connection) -> None:
    conn.touch()
