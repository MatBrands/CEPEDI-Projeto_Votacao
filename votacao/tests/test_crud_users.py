import sys
sys.path.insert(1, '../')
from interface.menuClass import *
from interface.usersClass import *
from models.module_CRUD import *

if __name__ == '__main__':

    usuario = {
        "user": "zDarkness",
        "password": "coxinha123",
        "name": "Dan",
        "age": 23,
        "role": '0'
    }

    usuario2 = {
        "user": "zDarkness",
        "password": "coxinha123",
        "name": "Darley",
        "age": 20,
        "role": '0'
    }

    usuario3 = {
        "user": "Lulonaro",
        "password": "arteezy321",
        "name": "Eric",
        "age": 20,
        "role": '0'
    }

    path = '../database/database.json'

    print(createUser(path, **usuario))

    # print(updateUser(path, **usuario2))

    # print(readUser(path, "Lulonaro"))

    # print(updateUser(path, **usuario)) 

    # print(deleteUser(path, "zDarkness"))
