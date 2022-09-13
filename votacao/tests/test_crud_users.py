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
        "user": "zDarkness",
        "email": "dan@uesc.br",
        "password": "coxinha123",
        "name": "Dan",
        "age": 23,
        "role": '0'
    }

    usuario2 = {
        "user": "zDarkness",
        "email": "dan@uesc.br",
        "password": "coxinha123",
        "name": "Darley",
        "age": 20,
        "role": '0'
    }

    usuario3 = {
        "user": "Lulonaro",
        "email": "ericx2@uesc.br",
        "password": "arteezy321",
        "name": "Eric",
        "age": 20,
        "role": '0'
    }

    path = '../database/database.json'

    # print(createUser(path, **usuario))

    # print(updateUser(path, **usuario2))

    # print(readUser(path, "Lulonaro"))

    # print(updateUser(path, **usuario)) 

    print(deleteUser(path, "zDarkness"))
