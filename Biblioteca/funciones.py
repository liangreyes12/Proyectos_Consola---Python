from os import name, system
from time import sleep

def limpiarPantalla():
   sistema = name
   if sistema == "nt":
      sleep(2)
      system("cls")
   else:
      sleep(2)
      system("clear")
      