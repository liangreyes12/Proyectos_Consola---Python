class usuario:

      idUser = 0

      def __init__(self, nombre, cuenta, saldo = 0):
          self.aumentarId()
          self._id = self.idUser
          self._nombre = nombre
          self._cuenta = cuenta
          self._saldo = saldo

      @property
      def nombre(self):
          return self._nombre

      @property
      def cuenta(self):
          return self._cuenta

      @property
      def saldo(self):
          return self._saldo

      @classmethod
      def aumentarId(cls):
          cls.idUser += 1

if __name__ == "__main__":
     user1 = usuario("Liang", "0009876")
     user2 = usuario("Ever", "0012344")
     user3 = usuario("Fabio", "0909876")
     print(user1._id, user2._id, user3._id)
     print(user1._nombre, user2._nombre, user3._nombre)
     print(user1._cuenta)
     print(user1._saldo)
