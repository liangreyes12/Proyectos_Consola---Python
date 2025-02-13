from biblioteca import Biblioteca
import funciones as fn

biblio = Biblioteca()
try:
    while True:
        print("*******SISTEMA GESTOR DE BIBLIOTECA******\n")
        print(f"ESCOGE UNA OPCION:\n1. Registrar Libro\n2. Buscar Libro por Autor\n3. Buscar Libro por Nombre\n4. Buscar Libro por Genero\n5. Buscar Libro por ISBN\n6. Salir\n")
        opcion = int(input("- "))
        match opcion:
            case 1:
               
                print(biblio.registrarLibro())
            case 2:
                
                print(biblio.buscarPorNombre())
            case 3:
                
                biblio.buscarPorAutor()
            case 4:
               
                biblio.buscarPorGenero()
            case 5:
                
                print(biblio.buscarPorISBN())
            case _:
                print(f"OPCION INVALIDA INTENTALO OTRA VEZ")
except ValueError:
    print("INGRESE DATO VALIDO")
except Exception as e: 
    print(f"ERROR {e}")