import json


def users_all():
    with open('database/database.json', encoding='utf-8') as fd:
        dados = json.load(fd)
    return dados
