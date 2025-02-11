class Usuario:

      idUser = 0

      def __init__(self, nombre, cuenta, saldo = 0):
          self.aumentarId()
          self._id = Usuario.idUser
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
      
      @saldo.setter
      def saldo(self, saldo):
          self._saldo = saldo

      @classmethod
      def aumentarId(cls):
          cls.idUser += 1


