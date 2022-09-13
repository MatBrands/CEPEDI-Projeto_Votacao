import sys
sys.path.insert(1, '../')
from interface.menuClass import *
from interface.usersClass import *
from models.module_CRUD import *

if __name__ == '__main__':

    dados = {
        "user_1": {
            "id": 1,
            "name": "Luca",
            "age": 22,
            "phone": "(73)9111-2222",
            "email": "luca@gmail.com"
        },
        "user_2":{
            "id": 2,
            "name": "Matheus",
            "age": 23,
            "phone": "(73)9111-2222",
            "email": "matheus@gmail.com"
        }
    }

    usuario = {
        "id": 4,
        "user": "zDarkness",
        "email": "dan@uesc.br",
        "password": "coxinha123",
        "name": "Dan",
        "age": 23,
        "role": '0'
    }

    usuario2 = {
        "id": 3,
        "user": "zDarkness",
        "email": "dan@uesc.br",
        "password": "coxinha123",
        "name": "Darley",
        "age": 20,
        "role": '0'
    }

    usuario3 = {
        "id": 5,
        "user": "Lulonaro",
        "email": "ericx2@uesc.br",
        "password": "arteezy321",
        "name": "Eric",
        "age": 20,
        "role": '0'
    }

    path = '../database/database.json'

    # print(createUser(path, **usuario3))

    # print(createUser(path, **usuario))

    # print(readUser(path, 1))

    # print(deleteUser(path, 'zDarkness'))

    # print(updateUser(path, **usuario2))

    print(deleteUser(path, 1))
