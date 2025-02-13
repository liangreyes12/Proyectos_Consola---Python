from libros import Libros

class Biblioteca:

   def __init__(self):
      self._inventario = []

   def registrarLibro(self, nombre, autor, genero, ISBN):
      for libro in self._inventario:
         if libro.ISBN == ISBN:
            print(f"ESTE LIBRO YA EXISTE EN EL INVENTARIO")
            return  
      libro = Libros(nombre, autor, genero, ISBN)
      self._inventario.append(libro)
      print(f"LIBRO AGREGADO EXITOSAMENTE")

   def buscarPorISBN(self, ISBN):
      for i in self._inventario:
         if i.ISBN == ISBN:
            return f"{i.ISBN} => {i.nombre} => {i.genero}"
      return f"LIBRO NO PUDO SER ENCONTRADO"
   
   def buscarPorNombre(self, nombre):
      for i in self._inventario:
         if i.nombre == nombre:
            return f"{i.ISBN} => {i.nombre} => {i.genero}"
      return f"LIBRO NO PUDO SER ENCONTRADO"

   def buscarPorAutor(self, autor):
    resultado = ""
    for libro in self._inventario:
        if libro.autor == autor:
            resultado += f"{libro.ISBN} => {libro.nombre} => {libro.genero}\n"
    if resultado == "":
        return "LIBRO NO PUDO SER ENCONTRADO"
    return resultado.strip()

   def buscarPorGenero(self, genero):
      resultado = ""
      for libro in self._inventario:
         if libro.genero == genero:
               resultado += f"{libro.ISBN} => {libro.nombre} => {libro.genero}\n"
      if resultado == "":
         return "LIBRO NO PUDO SER ENCONTRADO"
      return resultado.strip()
