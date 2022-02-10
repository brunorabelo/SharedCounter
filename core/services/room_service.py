import uuid


def create_new_room():
    BASE_URL = '3.13.147.30'

    room_name = ''
    while True:
        room_name = uuid.uuid4().hex[:6].upper()
        # TODO: verifica se o nome ja tem no banco de dados e sai quando achar um nome novo
        break
    room_link = f'ws://{BASE_URL}/ws/counter/{room_name}'
    # TODO cria o room no db

    #TODO retorna o link
    return room_link


def get_room_count(room_name):
    # TODO verificar se sala existe e retornar valor se tiver
    return 0