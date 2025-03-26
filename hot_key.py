import keyboard
import time
from colorama import init, Fore, Back, Style

init()

print(Fore.LIGHTRED_EX + " ▄▄▄      ▒█████   ██████   ██  ██ ▄▄▄▄      ")
print(                   "▒████▄   ▒██▒  ██▒██    ▒█▒ ██  ██ █████▄    ")
print(                   "▒██  ▀█▄ ▒██░  ██░██     ██ ████   █▌  ▀█▄  ")
print(                   "░██▄▄▄▄██▒██   ██░██     █░ ██ ██ ░██▄▄▄▄██ ")
print(                   " ▓█    ██░ ████▓▒▒███████▒░▒██  ██ ██    ██▒")
print(                   " ▒▒   ▓▒ ░ ▒░▒░▒░▒ ▒▓▒ ▒ ░ ▒▒▓  ▒  ▒▒   ▓▒ ░")
print(                   "  ▒   ▒▒ ░ ░ ▒ ▒░░ ░▒  ░ ░ ░ ▒  ▒   ▒   ▒▒ ░")
print(                   "  ░   ▒  ░ ░ ░ ▒ ░  ░  ░   ░ ░  ░   ░   ▒   ")
print(                   "      ░  ░   ░ ░       ░     ░          ░  ░")
Fore.RESET
print(f"{Fore.RED}Este programa te permite asignar una tecla como hotkey para otra combinacion de teclas.")
print(f"{Fore.RED}Para salir del programa presiona la tecla 'q','Q'.\n")
Fore.RESET

tecla1 = input(Fore.GREEN + "Ingresa la tecla que deseas usar como hotkey:")

print("\n")
Fore.RESET 
print(Fore.GREEN + "Ingresa la combinacion de teclas ejemplo: ", Fore.LIGHTYELLOW_EX + "windows+e\n")
print(Fore.RESET + "")
tecla2 = input(Fore.LIGHTMAGENTA_EX + "Ingresa la primera de las teclas: ")
tecla3 = input(Fore.LIGHTMAGENTA_EX + "Ingresa la segundo de las teclas: ")

while True:
    # Verificar si se presionó la tecla 'r'
    if keyboard.is_pressed(tecla1):
        Fore.RESET
        print(Fore.LIGHTBLUE_EX + "Hotkey 'r' activada!")
        keyboard.press(tecla2)
        time.sleep(0.5)
        keyboard.press(tecla3)
        time.sleep(0.2)
        keyboard.release(tecla2)
        keyboard.release(tecla3)


    # Verificar si se presionó la tecla 'q'
    elif keyboard.is_pressed('q' or 'Q'):
        Fore.RESET
        print(Fore.LIGHTRED_EX + "Saliste del programa.")
        break