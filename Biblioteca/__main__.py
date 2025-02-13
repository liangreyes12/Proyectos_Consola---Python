from biblioteca import Biblioteca
import funciones as fn

biblio = Biblioteca()
while True:
    try:
        print("*******SISTEMA GESTOR DE BIBLIOTECA******\n")
        print("ESCOGE UNA OPCION:\n"
            "1. Registrar Libro\n"
            "2. Buscar Libro por Nombre\n"
            "3. Buscar Libro por Autor\n"
            "4. Buscar Libro por Genero\n"
            "5. Buscar Libro por ISBN\n"
            "6. Salir\n")
        
        opcion = int(input("- "))

        match opcion:
            case 1:
                nombre = input("Nombre: ")
                autor = input("autor: ")
                genero = input("genero: ")
                ISBN = input("ISBN: ")
                biblio.registrarLibro(nombre, autor, genero, ISBN)
                fn.limpiarPantalla()
            case 2:
                nombre = input("Nombre: ")
                print(biblio.buscarPorNombre(nombre))
                fn.limpiarPantalla()
            case 3:
                autor = input("autor: ")
                print(biblio.buscarPorAutor(autor))
                fn.limpiarPantalla()
            case 4:
                genero = input("genero: ")
                print(biblio.buscarPorGenero(genero))
                fn.limpiarPantalla()
            case 5:
                ISBN = input("ISBN: ")
                print(biblio.buscarPorISBN(ISBN))
                fn.limpiarPantalla()
            case 6:
                print(f"GRACIAS POR PREFERIR MIS SERVICIOS")
                break
            case _:
                print(f"OPCION INVALIDA INTENTALO OTRA VEZ")
                fn.limpiarPantalla()
    except ValueError:
        print("INGRESE DATO VALIDO")
        fn.limpiarPantalla()
    except Exception as e: 
        print(f"ERROR {e}")