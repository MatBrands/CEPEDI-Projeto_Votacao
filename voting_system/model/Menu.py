import os
import platform
from termcolor import colored
from pynput import keyboard

def clear() -> None:
    so = platform.system()
    if so == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

class Menu:
    def on_press(self, key) -> bool:
        if str(key) == 'Key.up':
            self.option -= 1
        elif str(key) == 'Key.down':
            self.option += 1
        elif str(key) == 'Key.enter':
            self.acess = True

        return False

    def setTitle(self, *args) -> None:
        self.title = ''.join(*args)

    def setItems(self, *args) -> None:
        self.elements = len(*args)
        self.items = list(*args)

    def startMenu(self) -> int:
        self.option = 0
        self.acess = False
        current_menu = self.items.copy()

        while not self.acess:
            clear()

            for i in range(self.elements):
                if self.option % self.elements == i:
                    if current_menu[i] in ['Sair', 'Retornar']:
                        current_menu[i] = colored(current_menu[i], 'red')
                    else:
                        current_menu[i] = colored(current_menu[i], 'green')

            if self.title:
                print(self.title)

            [print(item) for item in current_menu]

            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
                current_menu = self.items.copy()

        input()
        clear()

        return self.option % self.elements