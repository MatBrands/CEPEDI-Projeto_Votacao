import sys
sys.path.insert(1, '../')
from interface.menuClass import *

if __name__ == '__main__':
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
    elif option == 1:
        print ('Registrou')
    else:
        print ('Saiu')
        exit(1)