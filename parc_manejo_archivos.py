from parc_manejo_datos import *
import re
import json


def leer_encabezado(archivo:str) -> list:
    """
    Brief: Lee la primera linea del archivo y se encarga de
    separar los elementos
    Return: Lista dividida de elementos
    """
    with open(archivo, "r") as archivo_csv:
        encabezado = archivo_csv.readline().strip().split(",")
    return encabezado


def leer_archivo_csv(archivo:str, encabezado:list) -> list:
    """
    Brief: Comienza a leer cada linea del archivo y genera
    un diccionario asignandole valores segun el encabezado
    Parameters: archivo = nombre del archivo
                encabezado = lista de keys para asignar
    Return: Lista completa con todos los datos ya asignados
    """
    datos = []
    with open(archivo, "r") as archivo_csv:
        archivo_csv.readline()
        for linea in archivo_csv:
            pokemon = {}
            valores = linea.strip().split(",")
            for i, valor in enumerate(valores):
                encabezado_actual = encabezado[i]
                pokemon[encabezado_actual] = parsear_valor(valor, encabezado_actual)
            datos.append(pokemon)
    return datos


def traer_datos() -> list:
    """
    Brief: Genera una tupla con los elementos del archivo especificado
    Return: Retorna la tupla con los datos ya parseados 
    """
    archivo = "pokemones.csv"
    try:
        encabezado = leer_encabezado(archivo)
        pokemones = leer_archivo_csv(archivo, encabezado)
        print("\n\u2713 Datos cargados exitosamente!\n")
        pokemones = tuple(pokemones)
        return pokemones
    except:
        print("\n\u274C Error tratando de acceder a los datos\n")


def guardar_archivo(pokemones:list) -> int:
    """
    Brief: Recibe un tipo de pokemon a buscar y lo guarda en un archivo .json
    aquellos del mismo tipo junto a su poder maximo de ataque/defensa.
    Parameters: pokemones = Lista de pokemones
    Return: Retorna 0 si pudo guardar el archivo y -1 si no encontro
    el tipo que fue ingresado.
    """
    tipo_busqueda = recibir_string("Ingrese el tipo de pokemon a buscar: ")

    pokemones_tipo = ""

    for pokemon in pokemones:
        
        tipo_pokemon_str = castear_informacion_str(pokemon, "Tipo")

        if re.search(tipo_busqueda, tipo_pokemon_str.lower()):
            pokemones_tipo = tipo_busqueda

    if len(pokemones_tipo) == 0:
        print(f"\nNo se encontraron pokemones del tipo '{tipo_busqueda}'")
        return -1
    else:
        pokemones_json = []
        for pokemon in pokemones:

            tipo_pokemon_str = castear_informacion_str(pokemon, "Tipo")

            if re.search(tipo_busqueda, tipo_pokemon_str.lower()):
                poder_maximo_ataque = int(pokemon['Poder de Ataque'])
                poder_maximo_defensa = int(pokemon['Poder de Defensa'])

                if poder_maximo_ataque > poder_maximo_defensa:
                    tipo_poder = 'Ataque'
                    poder_maximo = poder_maximo_ataque

                elif poder_maximo_ataque == poder_maximo_defensa:
                    tipo_poder = 'Ambos'
                    poder_maximo = poder_maximo_ataque
                    #poder_maximo = (poder_maximo_ataque,poder_maximo_defensa)
                    
                else:
                    tipo_poder = 'Defensa'
                    poder_maximo = poder_maximo_defensa

                pokemon_json = {
                    'Nombre': pokemon['Nombre'],
                    'Poder Maximo': poder_maximo,
                    'Tipo de Poder': tipo_poder
                }
                pokemones_json.append(pokemon_json)
    
        with open(f"{tipo_busqueda}_pokemones.json", "w") as archivo_json:
            json.dump(pokemones_json, archivo_json, indent=4)
    
        print(f"\nSe encontraron {len(pokemones_json)} \
pokemones del tipo '{tipo_busqueda}'")
        print(f"\nLos datos se han guardado en el archivo \
'{tipo_busqueda}_pokemones.json'")
        
        return 0


def leer_archivo():
    """
    Brief: Recibe un tipo de pokemon a buscar en los archivos existentes
    En caso de encontrarlo muestra en consola
    los datos pertenecientes al mismo formateados.
    Return: Retorna 0 si pudo leer el archivo y -1 si no pudo encontrarlo.
    """
    tipo_busqueda = recibir_string("Ingrese el tipo de pokemon a buscar: ")

    try:
        with open(f"{tipo_busqueda}_pokemones.json", "r") as archivo_json:
            pokemones_json = json.load(archivo_json)
        print(f"\nSe encontraron {len(pokemones_json)} \
pokemones del tipo '{tipo_busqueda}':\n")
        for pokemon in pokemones_json:

            nombre_pokemon = pokemon['Nombre']
            poder_maximo = pokemon['Poder Maximo']
            tipo_poder = pokemon['Tipo de Poder']

            print(f'{nombre_pokemon}-{poder_maximo}-"{tipo_poder}"')    
        print("\n\u2713-Se cargo el archivo con exito!\n")
    except:
        print(f"\nNo se encontró el archivo '{tipo_busqueda}_pokemones.json'")