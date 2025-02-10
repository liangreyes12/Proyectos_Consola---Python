from usuario import usuario

class Banco:

      def __init__(self, nombre):
         self._nombre = nombre
         self._users = []

      def imprimirInformacion(self, cuenta):
          for i in self._users:
              if i.cuenta == cuenta:
                 print(i._id, i._nombre, i._cuenta)

      def crearUsuario(self, nombre, cuenta):
          us = usuario(nombre, cuenta)
          self._users.append(us)

      def retirar(self):
          pass

      def depositar(self):
          pass

      def buscarCuenta(self, cuenta):
          for i in self._users:
              if i.cuenta == cuenta:
                 return f"encontrado"
              else:
                 return f"Cuenta No existe"

banco1 = Banco("Bancolombia")
banco1.crearUsuario("Liang", "0009876")
banco1.crearUsuario("Ever", "0001234")
print(banco1._users)
print(banco1.buscarCuenta("0009876"))
banco1.imprimirInformacion("0001234")

