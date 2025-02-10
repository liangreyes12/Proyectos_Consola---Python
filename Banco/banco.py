from usuario import Usuario

class Banco:

    def __init__(self):
        self._users = []


    def imprimirInformacion(self, cuenta):
        for i in self._users:
            if i.cuenta == cuenta:
                print(i._id, i._nombre, i._cuenta, i._saldo)


    def crearUsuario(self, nombre, cuenta):
        us = Usuario(nombre, cuenta)
        if not any(u.cuenta == us.cuenta for u in self._users):
            self._users.append(us)
            print("Usuario creado con éxito")
        else:
            print("OPERACION INVALIDA, ESTA CUENTA YA EXISTE")
            

    def retirar(self, cuenta, monto):
        usuario = self.buscarCuenta(cuenta)
        if usuario:
            if usuario._saldo < monto:
                print("SALDO INSUFICIENTE")
            else:
                usuario._saldo -= monto
                print("Retiro exitoso")
        else:
            print("Cuenta no encontrada")


    def depositar(self, cuenta, monto):
        usuario = self.buscarCuenta(cuenta)
        if usuario:
            usuario._saldo += monto
            print("Deposito exitoso")


    def buscarCuenta(self, cuenta):
        for i in self._users:
            if cuenta == i.cuenta:
                return i
            else:
                return None

# banco1 = Banco()
# banco1.crearUsuario("Liang", "0009876")
# banco1.crearUsuario("Ever", "0001234")
# print(banco1._users)
# print(banco1.buscarCuenta("0009876"))
# banco1.imprimirInformacion("0001234")