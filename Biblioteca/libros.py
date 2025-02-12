class Libros:

      def __init__(self, nombre, autor, genero, ISBN):
         self._nombre = nombre
         self._autor = autor
         self._genero = genero
         self._ISBN = ISBN

      @property
      def nombre(self):
          return self._nombre

      @property
      def autor(self):
          return self._autor

      @property
      def genero(self):
          return self._genero

      @property
      def ISBN(self):
          return self._ISBN
