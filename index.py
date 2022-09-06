import os
from screens import index_screens
from models import UserModel

if __name__ == '__main__':
    while 1:
        index_screens.main_screen()
        option = int(input())
        os.system('clear')

        if option != 1 and option != 2 and option != 3 or option < 0 or option > 3:
            print('Opção invalida')
        if option == 1:
            os.system('clear')
            index_screens.login_screen()
        if option == 2:
            pass
        if option == 3:
            UserModel.users_all()
            break
    index_screens.logout_screen()
