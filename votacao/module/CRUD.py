import json


def createUser(**user):
    with open("/home/luca/Documentos/Projeto_votacao/votacao/database/database.json", encoding='utf-8') as file:
        data = json.load(file)

    for key, value in list(data.items()):
        if value['name'] == user['name']:
            return False

    u = {
        user['user']: {
        }
    }

    usr = {
        "name": user['name'],
        "password": user['password'],
        "email": user['email'],
        "age": user['age'],
        "role": 1
    }

    u[user['user']].update(usr)

    data.update(u)

    with open("/home/luca/Documentos/Projeto_votacao/votacao/database/database.json", "w") as file2:
        json.dump(data, file2, indent=4)
    return True


def findUser(user):
    with open("/home/luca/Documentos/Projeto_votacao/votacao/database/database.json", encoding='utf-8') as file:
        data = json.load(file)

    for key, value in list(data.items()):
        if key == user:
            return value

    return False


def updateUser(**new_data):
    with open("/home/luca/Documentos/Projeto_votacao/votacao/database/database.json", encoding='utf-8') as file:
        data = json.load(file)
    find = False

    for key, value in list(data.items()):
        if key == new_data['user']:
            data.pop(key)
            data.update(new_data)
            find = True
    if find:
        u = {
            new_data['user']: {
            }
        }

        usr = {
            "name": new_data['name'],
            "password": new_data['password'],
            "email": new_data['email'],
            "age": new_data['age'],
            "role": 1
        }

        u[new_data['user']].update(usr)

        data.update(u)

        with open("/home/luca/Documentos/Projeto_votacao/votacao/database/database.json", "w") as file2:
            json.dump(data, file2, indent=4)
    else:
        return False

    return True


def deleteUser(user):
    with open("/home/luca/Documentos/Projeto_votacao/votacao/database/database.json", encoding='utf-8') as file:
        data = json.load(file)
        find = False

    for key, value in list(data.items()):
        if key == user:
            data.pop(key)
            find = True

    if find:
        with open("/home/luca/Documentos/Projeto_votacao/votacao/database/database.json", "w") as file2:
            json.dump(data, file2, indent=4)
    else:
        return False
