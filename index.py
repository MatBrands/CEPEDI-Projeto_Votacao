import os
from screens.menuClass import *

if __name__ == '__main__':

    # 
    menu = Menu()
    menu.setTitulo(['#############################################\n', 
    '\tBem Vindo Ao Sistema De Votação\t', 
    '\n#############################################\n'])
    menu.setItems(['Entrar', 'Registrar', 'Sair'])
    # 

    option = menu.iniciarMenu()

    os.system("clear")

    if option == 0:
        print ('Entrou')
        pass
    elif option == 1:
        print ('Registrou')
        pass
    elif option == 2:
        print ('Saiu')
        pass
    