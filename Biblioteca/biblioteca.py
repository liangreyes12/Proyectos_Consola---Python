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
         for i in self._inventario:
            if i.autor == autor:
               print(f"{i.ISBN} => {i.nombre} => {i.genero}")
         return f"LIBRO NO PUDO SER ENCONTRADO"

      def buscarPorGenero(self, genero):
         for i in self._inventario:
            if i.genero == genero:
               print(f"{i.ISBN} => {i.nombre} => {i.genero}")
         return f"LIBRO NO PUDO SER ENCONTRADO"