import keyboard

import colorama
from colorama import Fore, init
init()
print("SJ'apprends le français = I am learning French")
print("")

print(Fore.RED,'Greeting')
print("Greeting")
print("")

keyboard.wait("enter")
print("")

print(Fore.WHITE)
print("Salut = Hello")
print("Comment ca va = How are you?")
print("Encante = Nice to meet you")
print("A_bientot = See you soon")
print("Bonne_soiree = Good Evening")
print("A_demain = See you tomorrow")

print("Programdan çıkmak için Esc' ye basınız")

keyboard.wait("esc")

print("Programdan çıkıldı.")