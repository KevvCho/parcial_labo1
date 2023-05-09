from unidecode import unidecode
import re


def parsear_valor(valor:str, encabezado:list):
    """
    Brief: Dependiendo del tipo de dato encontrado en el encabezado
    se encarga de parsear o separar en una lista los valores
    Return: Dato ya modificado
    """
    if encabezado in ("N° Pokedex", "Poder de Ataque", "Poder de Defensa"):
        valor = int(valor)
    elif encabezado in ("Tipo", "Habilidades"):
        valor = re.split('\|\*\||\/|Ninguna', valor.strip())
    else:
        valor = valor.strip()
        
    return valor


def castear_informacion_str(valor:dict, tipo:str) -> str:
    """
    Brief: Recibe un diccionario y un valor en el cual
    comprueba si es 1 o 2 elementos y normaliza.
    Retorna el valor casteado a string.
    Parameters: valor = diccionario al que se accede
                 tipo = tipo de dato a encontrar en el diccionario
    Return: Retorna el dato unido como un string
    """
    tipo_dato = valor[tipo]
    tipolen = len(valor[tipo])
    
    if tipolen > 2:
        tipo_dato_str = ''.join(tipo_dato)
    else:
        tipo_dato_str = '/'.join(tipo_dato)

    tipo_dato_str = unidecode(tipo_dato_str)
    
    return tipo_dato_str


def recibir_string(texto:str) -> str:

    texto_obtenido = input(f"\n{texto}")

    texto_obtenido = texto_obtenido.lower().strip()

    return texto_obtenido


def calcular_division(dividendo:int, divisor:int) -> float:

    resultado = 0

    if divisor != 0:
        resultado = dividendo/divisor
        resultado = round(resultado, 2)

    return resultado


def ordenar_lista(lista_recibida:list, primer_orden:str,
                 segundo_valor:str) -> list:
    """
    Brief: A partir de una lista y dos valores de ordenamiento utiliza 
    ordenamiento por burbujeo para generar una nueva lista.
    Parameters: lista_recibida = una lista de elementos a ordenar.
                valor_ordenamiento = el valor que se quiere ordenar de
                mayor a menor.
                segundo_valor = valor alternativo a ordenar en caso 
                de que dos elementos coincidan en el primer ordenamiento.
    Return: Retorna la lista ordenada.
    """
    lista_recibida = list(lista_recibida)

    n = len(lista_recibida)

    for i in range(n):
        for j in range(0, n-i-1):

            if int(lista_recibida[j][primer_orden]) < int(lista_recibida[j+1][primer_orden]):
                lista_recibida[j], lista_recibida[j+1] = lista_recibida[j+1], lista_recibida[j]

            elif int(lista_recibida[j][primer_orden]) == int(lista_recibida[j+1][primer_orden]):

                if lista_recibida[j][segundo_valor] > lista_recibida[j+1][segundo_valor]:
                    lista_recibida[j], lista_recibida[j+1] = lista_recibida[j+1], lista_recibida[j]

    return lista_recibida


def buscar_tipos(pokemones:tuple) -> list:
    """
    Brief: Recibe una lista, busca cada "tipo" existente y 
    agrega una unidad a su cantidad, en caso de no existir
    se agrega a la lista.
    Parameters: pokemones = Lista de pokemones
    Return: Retorna la lista de tipos y su respectiva cantidad.
    """
    lista_tipos = []

    for pokemon in pokemones:
        
        tipo_str = castear_informacion_str(pokemon, "Tipo")
        tipo_encontrado = False

        for tipo_dic in lista_tipos:

            if tipo_dic['tipo'] == tipo_str:
                tipo_dic['cantidad'] += 1
                tipo_encontrado = True
                break

        if not tipo_encontrado:
            nuevo_tipo = {'tipo': tipo_str, 'cantidad': 1}
            lista_tipos.append(nuevo_tipo)

    return lista_tipos


def calcular_promedio_poder(pokemones:tuple) -> float:
    """
    Brief: Calcula el promedio del poder total de una lista de pokemones.
    Parameters: pokemones = Lista de pokemones.
    Return: Retorna el promedio del poder total.
    """
    poder_total = 0
    for pokemon in pokemones:
        poder_ataque = int(pokemon['Poder de Ataque'])
        poder_defensa = int(pokemon['Poder de Defensa'])
        poder_total += poder_ataque + poder_defensa / 2
    promedio = calcular_division(poder_total, len(pokemones))
    return promedio


def buscar_pokemones_por_habilidad(pokemones:tuple, habilidad_busqueda:str) -> list:
    """
    Brief: Busca pokemones que contengan la habilidad ingresada por el usuario.
    Parameters: pokemones = Lista de pokemones, habilidad_busqueda = Habilidad a buscar.
    Return: Retorna una lista de pokemones que contienen la habilidad.
    """
    pokemones_habilidad = []
    for pokemon in pokemones:
        tipo_pokemon_str = castear_informacion_str(pokemon, "Habilidades")
        if re.search(habilidad_busqueda, tipo_pokemon_str.lower()):
            pokemones_habilidad.append(pokemon)
    return pokemones_habilidad