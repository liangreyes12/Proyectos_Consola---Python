from libros import Libros

class Biblioteca:

      def __init__(self, nombre):
          self._nombre = nombre
          self._inventario = []

      def registrarLibro(self, nombre, autor, genero, ISBN):
          libro = Libros(nombre, autor, genero, ISBN)
          if libro.ISBN in self._inventario:
             print(f"ESTE LIBRO YA ESTA REGISTRADO")
          else:
             self._inventario.append(libro)
             print(f"Libro registrado exitosamente")

      def busquedaISBN(self, ISBN):
          for i in self._inventario:
              if i.ISBN == ISBN:
                 return ISBN
              else:
                 return None

biblio1 = Biblioteca("La salle")
biblio1.registrarLibro("Cien años de soledad", "Gabriel García Marquez", "Realismo Mágico", "009876")
biblio1.registrarLibro("Cien años de soledad", "Gabriel García Marquez", "Realismo Mágico", "0009876")
