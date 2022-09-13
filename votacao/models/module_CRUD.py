import json

def createUser(path, **user):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    for value in list(data.items()):
        if (value['name'] == user['name']) or (value['email'] == user['email']):
            return False

    u = { user['id']:{ } }

    if usr['role'] == 0:
        usr = {
        "user": user['user'],
        "email": user['email'],
        "password": user['password'],
        "name": user['name'],
        "age": user['age'],
        "role": 0
        }

    else:
        usr = {
        "user": user['user'],
        "email": user['email'],
        "password": user['password'],
        "name": user['name'],
        "age": user['age'],
        "proposta": user['proposta'],
        "role": 1
        }

    u[user['id']].update(usr)

    data.update(u)

    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    return True

def updateUser(path, **new_data):
    find = False
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    for key, _ in list(data.items()):
        if key == new_data['id']:
            data.pop(key)
            data.update(new_data)
            find = True
    if find:
        u = {
            new_data['id']: {
            }
        }

        if new_data['role'] == 0:
            usr = {
            "user": new_data['user'],
            "email": new_data['email'],
            "password": new_data['password'],
            "name": new_data['name'],
            "age": new_data['age'],
            "role": 0
            }

        else:
            usr = {
            "user": new_data['user'],
            "email": new_data['email'],
            "password": new_data['password'],
            "name": new_data['name'],
            "age": new_data['age'],
            "proposta": new_data['proposta'],
            "role": 1
            }

        u[new_data['id']].update(usr)

        data.update(u)

        with open(path, "w") as file:
            json.dump(data, file, indent=4)
    else:
        return False

    return True

def readUser(path, id):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    for k, item in data.items():
        if k == str(id):
            return item
            
    return False

def deleteUser(path, id):
    find = False
    with open(path, encoding='utf-8') as file:
        data = json.load(file)

    for key, _ in list(data.items()):
        if key == str(id):
            data.pop(key)
            find = True

    if find:
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
    else:
        return False
    return True
