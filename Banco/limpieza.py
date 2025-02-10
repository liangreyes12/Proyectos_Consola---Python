from time import sleep
import os

def limpíarPantalla():
    sistema = os.name
    if sistema == "nt":
        sleep(2)
        os.system("cls")
    else:
        sleep(2)
        os.system("clear")
        