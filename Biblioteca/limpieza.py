from os import name, system
from time import sleep

def limpiarPantalla():
    sistema = name
    if sistema == "nt":
       system("cls")
       sleep(2.3)
    else:
       system("clear")
       sleep(2.3)
