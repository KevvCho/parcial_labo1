from parc_manejo_datos import *


def validar_entero(numero_verificacion:str):
    #Utiliza la funcion isdgit para confirmar la existencia de un numero en el string
    
    if numero_verificacion.isdigit():
        return True
    else:
        return False


def obtener_input_int(texto:str) -> int:
    """
    Brief: Obtiene un input a validar que luego es casteado a entero
    Return: Si no se introduce un numero entero retorna -1
    """

    respuesta = input(texto)
    validacion = validar_entero(respuesta)
    if validacion == True:
        respuesta = int(respuesta)
        return respuesta
    else:
        return -1
    

def confirmar_errores(opcion_elegida:str, lista_archivo:list):
    """
    Brief: Recibe una funcion como string y una lista proveniente de un archivo
    Se encarga de ejecutar cada funcion y mostrar si se realizo correctamente o no
    """
    confirmacion = -1

    try:
        if len(lista_archivo) != 0:
            confirmacion = opcion_elegida(lista_archivo)
        else:
            print("\nLa lista proporcionada esta vacia, cargue la lista primero")
    except:
        print("\nHubo un error al cargar datos de la lista\n")

    if confirmacion == -1:
        print("\n\u274C-Se produjo un error realizando la accion\n")
    else:
        print("\n\u2713-Se realizo la operacion con exito!\n")