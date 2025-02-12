from banco import Banco
import limpieza

bancoLiang = Banco()
while True:
    try:
        print("********BIENVENIDO AL BANCO DE LIANG********\n")
        print(f"ESCOGE UNA OPCION:\n1. Crear Cuenta\n2. Ver Información de Cuenta\n3. Depositar\n4. Retirar\n5. Salir\n")
        opcion = int(input("- "))

        match opcion:
            case 1:
                name = input("Ingrese nombre de usuario: ")
                counts = input("Ingrese numero de cuenta: ")
                bancoLiang.crearUsuario(name, counts)
                limpieza.limpíarPantalla()
            case 2:
                counts = input("Ingrese numero de cuenta: ")
                bancoLiang.imprimirInformacion(counts)
                limpieza.limpíarPantalla()
            case 3:
                counts = input("Ingrese numero de cuenta: ")
                monto = int(input("Ingrese monto a depositar: "))
                bancoLiang.depositar(counts, monto)
                limpieza.limpíarPantalla()
            case 4:
                counts = input("Ingrese numero de cuenta: ")
                monto = int(input("Ingrese monto a retirar: "))
                bancoLiang.retirar(counts, monto)
                limpieza.limpíarPantalla()
            case 5:
                print("GRACIAS POR SU PREFERIR NUESTRO SERVICIO")
                break
            case _:
                print("OPCION INVALIDA, VUELVA A INTENTARLO")
                limpieza.limpíarPantalla()
    except ValueError:
        print(f"Ingrese tipo de dato valido")
        limpieza.limpíarPantalla()
    except Exception as e:
        print(f"ERROR: {e}")