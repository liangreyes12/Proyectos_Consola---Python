from time import sleep
from os import name, system

def limpíarPantalla():
    sistema = name
    if sistema == "nt":
        sleep(2)
        system("cls")
    else:
        sleep(2)
        system("clear")
        