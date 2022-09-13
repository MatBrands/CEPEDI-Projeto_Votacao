from doctest import testfile
from interface.menuClass import *
from interface.usersClass import *
from models.CRUD import *
import json


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

    #print(createUser(**usuario3))

    #print(createUser(**usuario))

    #print(findUser('zDarkness'))

    #print(deleteUser('zDarkness'))

    #print(updateUser(**usuario2))

    #print(deleteUser('zDarkness'))
