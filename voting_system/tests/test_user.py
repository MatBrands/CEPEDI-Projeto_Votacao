import sys
sys.path.insert(1, '../')
from interface.usersClass import *

if __name__ == '__main__':
    user_1 = Eleitor(1, 'Matheus_Mbr', '123456', 'Matheus Brandão')

    print (user_1.getId(), user_1.getName(), user_1.getUser())

    user_2 = Candidato(2, 'LucaSao', '123456', 'Luca Sacramento', 'Bolsa Pinga')

    print (user_2.getId(), user_2.getName(), user_2.getUser(), user_2.getProposta(), user_2.getContagem())

    print (type(user_1), type(user_2))
