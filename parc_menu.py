from parc_mostrar_datos import *

def imprimir_menu():
    
    print("""
    **********************************************************************
    |                    Gestion de pokemones                            |
    **********************************************************************
    |                1- Traer datos desde archivo .csv                   |
    |                2- Listar cantidad de pokemones por tipo            |
    |                3- Listar pokemones por tipo                        |
    |                4- Listar pokemones por habilidad                   |
    |                5- Listar pokemones ordenados                       |
    |                6- Guardar Json                                     |
    |                7- Leer Json                                        |
    |                8- Agregar Pokemon                                  |
    |                9- Guardar csv                                      |
    |                10- Salir                                           |
    **********************************************************************
        """)


def iniciar_menu():

    datos = []
    
    while True:

        imprimir_menu()
        opcion = obtener_input_int("Ingrese una opcion: ")

        while opcion == -1:
            print("No es un caracter valido por favor reingrese la opcion")
            opcion = obtener_input_int()

        match opcion:

            case 1:
                # Traer datos desde archivo
                datos = traer_datos()
            case 2:
                # Listar cantidad por tipo
                confirmar_errores(listar_cantidad_tipo, datos)
            case 3:
                # Listar pokemones por tipo
                confirmar_errores(listar_tipo, datos)
            case 4:
                # Listar pokemones por habilidad
                confirmar_errores(listar_habilidad, datos)
            case 5:
                # Listar pokemones ordenados
                confirmar_errores(listar_ordenado, datos)
            case 6:
                # Guardar Json
                confirmar_errores(guardar_archivo, datos)
            case 7:
                # Leer Json
                leer_archivo()
            case 8:
                datos = agregar_pokemon(datos)
            case 9:
                guardar_csv(datos)
            case 10:
                # Salir
                break
            case _:
                print("Opcion no valida reintroduzca un caracter valido")