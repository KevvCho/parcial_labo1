from parc_manejo_archivos import *
from parc_validaciones import *
from parc_manejo_datos import *


def listar_cantidad_tipo(pokemones:tuple) -> int:
    """
    Brief: A partir de una lista ya ordenada muestra en consola el valor
    de "tipo" y la cantidad total de elementos que comparten tipo.
    Parameters: pokemones = Lista de pokemones
    Return: Retorna 0 en caso de que la lista no este vacia y -1
    en el caso contrario.
    """
    lista_tipos = buscar_tipos(pokemones)
    
    if len(lista_tipos) != 0:
        generar_patron("*" , 81)
        for tipo in lista_tipos:
            listar_general(tipo, 'tipo', 'cantidad')
            generar_patron("*" , 81)
        return 0
    else:
        return -1


def listar_tipo(pokemones:tuple) -> int:
    """
    Brief: Imprime en consola todos los pokemones que comparten
    el mismo elemento de "tipo" mostrando su nombre y 
    poder de ataque.
    Parameters: pokemones = Lista de pokemones
    Return: Retorna 0 en caso de que la lista no este vacia y -1
    en el caso contrario.
    """
    lista_tipos = buscar_tipos(pokemones)
    
    if len(lista_tipos) != 0:
        for tipo in lista_tipos:

            tipo_str = tipo['tipo']

            generar_patron("*" , 81)
            print(f"*Tipo: {tipo_str}\n")
            generar_patron("*" , 81)

            for pokemon in pokemones:

                tipo_pokemon_str = castear_informacion_str(pokemon, "Tipo")
            
                if tipo_str == tipo_pokemon_str:
                    listar_general(pokemon, 'Nombre', 'Poder de Ataque')
                
        return 0
    else:
        return -1
    

def listar_general(objeto:dict, primer_valor_dict:str,
                    segundo_valor_dict:str):
    """
    Brief: Muestra en consola el primer y segundo valor obtenidos
    de un diccionario formateados.
    Parameters: objeto = Diccionario con el elemento a mostrar
                primer_valor_dict: Valor a buscar en el diccionario
                segundo_valor_dict:         ''
    """

    primer_valor = objeto[primer_valor_dict]
    segundo_valor = objeto[segundo_valor_dict]

    primer_valor_dict = primer_valor_dict.capitalize()
    segundo_valor_dict = segundo_valor_dict.capitalize()

    if type(segundo_valor) == list:
        segundo_valor = castear_informacion_str(objeto, segundo_valor_dict)
            
    print(f"{primer_valor_dict}: {primer_valor}, \
{segundo_valor_dict}: {segundo_valor}")
    

def listar_habilidad(pokemones:tuple) -> int:
    """
    Brief: Recibe una habilidad ingresada por el usuario y la busca en
    la lista proporcionada, si la encuentra muestra el nombre y tipo de
    todos los pokemones que la comparten junto a la cantidad.
    Parameters: pokemones = Lista de pokemones.
    Return: Retorna 0 si pudo encontrar la habilidad y -1 en caso contrario.
    """
    habilidad_busqueda = recibir_string("Ingrese la descripción de la habilidad a buscar: ")
    
    if not habilidad_busqueda:
        print("La habilidad no puede ser vacía.")
        return -1

    pokemones_habilidad = buscar_pokemones_por_habilidad(pokemones, habilidad_busqueda)
    cantidad_pokemones = len(pokemones_habilidad)

    if not pokemones_habilidad:
        print(f"No se encontraron pokemones con la habilidad que contenga '{habilidad_busqueda}'")
        return -1

    generar_patron("*", 81)
    for pokemon in pokemones_habilidad:
        listar_general(pokemon,"Nombre","Tipo")
    generar_patron("*", 81)

    poder_promedio = calcular_promedio_poder(pokemones_habilidad)

    print(f"\nSe encontraron {cantidad_pokemones} pokemones con la habilidad que contiene '{habilidad_busqueda}'")
    print(f"Promedio de poder entre ataque y defensa: {poder_promedio}")
    return 0


def listar_ordenado(pokemones:tuple) -> int:
    """
    Brief: Utilizando una lista ordenada en base a poder de ataque y nombre como
    segunda condicion muestra en consola todos los datos provenientes del pokemon.
    Parameters: pokemones = Lista de pokemones
    Return: Retorna 0 si se pudo completar y -1 si la lista esta vacia.
    """
    lista_ordenada  = ordenar_lista(pokemones, "Poder de Ataque", "Nombre")

    if len(lista_ordenada) != 0:
        print("\nLista de pokemones ordenados por poder de ataque")
        generar_patron("*" , 81)

        for pokemon in lista_ordenada:
    
            pokemon_tipo = castear_informacion_str(pokemon, "Tipo")
            pokemon_habilidades = castear_informacion_str(pokemon, "Habilidades")

            print(f"""
    N° Pokedex: {pokemon['N° Pokedex']}
    Nombre: {pokemon['Nombre']}
    Tipo: {pokemon_tipo}
    Habilidades: {pokemon_habilidades}
    Poder de Defensa: {pokemon['Poder de Defensa']}
    Poder de Ataque: {pokemon['Poder de Ataque']}
    """)
            generar_patron("*" , 81)
        return 0
    else:
        return -1

def generar_patron(patron:str, cantidad:int):

    for i in range(cantidad):
        print(f"{patron}",end="")
    print("\n")