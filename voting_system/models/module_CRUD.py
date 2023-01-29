import json

def createUser(path, **user):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    for key, _ in list(data.items()):
        if key == user['user']:
            return False

    u = { user['user']:{ } }

    if user['role'] == 0:
        usr = {
        "password": user['password'],
        "name": user['name'],
        "age": user['age'],
        "role": 0
        }

    else:
        usr = {
        "password": user['password'],
        "name": user['name'],
        "age": user['age'],
        "proposta": user['proposta'],
        "role": 1
        }

    u[user['user']].update(usr)

    data.update(u)

    with open(path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return True

def updateUser(path, **new_data):
    find = False
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    for key, _ in list(data.items()):
        if key == new_data['user']:
            data.pop(key)
            find = True

    if find:
        u = {
            new_data['user']: {
            }
        }

        if new_data['role'] == 0:
            usr = {
            "password": new_data['password'],
            "name": new_data['name'],
            "age": new_data['age'],
            "role": 0
            }

        else:
            usr = {
            "password": new_data['password'],
            "name": new_data['name'],
            "age": new_data['age'],
            "proposta": new_data['proposta'],
            "role": 1
            }

        u[new_data['user']].update(usr)

        data.update(u)

        with open(path, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
        return False

    return True

def readUser(path, user):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    for k, item in data.items():
        if k == str(user):
            return item
            
    return False

def deleteUser(path, user):
    find = False
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    for key, _ in list(data.items()):
        if key == str(user):
            data.pop(key)
            find = True

    if find:
        with open(path, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
        return False
    return True
