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
            "name": "Dan",
            "user": "zDarkness",
            "password": "coxinha123",
            "email": "dan@uesc.br",
            "age": 23
    }

    usuario2 = {
            "name": "Darley",
            "user": "zDarkness",
            "password": "coxinha123",
            "email": "dan@uesc.br",
            "age": 20
    }

    usuario3 = {
            "name": "Eric",
            "user": "Lulonaro",
            "password": "arteezy321",
            "email": "ericx2@uesc.br",
            "age": 20
    }

    path = '../database/database.json'

    print(createUser(path, **usuario3))

    print(createUser(path, **usuario))

    print(readUser(path, 'zDarkness'))

    print(deleteUser(path, 'zDarkness'))

    print(updateUser(path, **usuario2))

    print(deleteUser(path, 'zDarkness'))
