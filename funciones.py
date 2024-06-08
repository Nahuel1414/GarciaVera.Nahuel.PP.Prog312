from os import system

def limpiar_pantalla():
    system("cls")
def pausa():
    system("pause")

def get_path_actual(nombre_archivo):
    """_summary_

    Args:
        nombre_archivo (_type_): recibe el archivo

    Returns:
        _type_: retorna el directorio actual y el nombre del archivo.
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def mostrar_post(persona: dict)-> None:
    """_summary_

    Args:
        persona (dict): recibe el diccionario.
    """
    print(f" {persona["id"]:<5}   {persona["user"]:<15}   {persona["likes"]:^7}     {persona["dislikes"]:^9}     {persona["followers"]:^10}   ")

def valores_random(post: dict) -> dict:
    """_summary_

    Args:
        post (dict): recibe un post.

    Returns:
        dict: retorna un diccionario con los valores actualizados.
    """
    import random
    post["likes"] = random.randint(500, 3000)
    post["dislikes"] = random.randint(300, 3500)
    post["followers"] = random.randint(10000, 20000)
    return post

def mapear_lista(procesadora, lista:list):
    """_summary_

    Args:
        procesadora (_type_): recibe una funcion.
        lista (list): recibe una lista.

    Returns:
        _type_: retorna la lista mapeada.
    """
    lista_retorno = []
    for element in lista:
        lista_retorno.append(procesadora(element))
    return lista_retorno

def filtrar_posts_2000_likes(post: dict):
    """_summary_

    Args:
        post (dict): recibe un post(diccionario)

    Returns:
        _type_: retorna los posts con mas de 2000 likes.
    """
    return post["likes"] > 2000

def funcion_haters(post:dict):
    """_summary_

    Args:
        post (dict): recibe un post

    Returns:
        _type_: retorna los posts donde los dislikes sean mayores que los likes.
    """
    return post["dislikes"] > post["likes"]

def filtrar_lista(filtradora, lista:list)->list:
    """_summary_

    Args:
        filtradora (_type_): recibe una funcion
        lista (list): recibe una lista

    Returns:
        list: retorna la lista filtrada
    """
    lista_filtrada = []
    for element in lista:
        if filtradora(element):
            lista_filtrada.append(element)
    return lista_filtrada

def sumar_lista(lista:list)->int:
    """_summary_

    Args:
        lista (list): recibe una lista

    Returns:
        int: retorna la suma de numeros
    """
    suma_numeros = 0
    for numero in lista:
        suma_numeros = suma_numeros + numero
    return suma_numeros

def promedio_lista(lista:list)-> float:
    """_summary_

    Args:
        lista (list): recibe una lista

    Raises:
        Exception: division por cero

    Returns:
        float: retorna el promedio.
    """
    if len(lista) == 0:
        raise Exception("Error. Lista vacía.")
    else:
        return sumar_lista(lista) / len(lista)

def obtener_mayor(lista:list) -> int:
    """_summary_

    Args:
        lista (list): recibe una lista

    Raises:
        ValueError: error de lista vacia.

    Returns:
        int: retorna el mayor.
    """
    if len(lista) == 0:
        raise ValueError("Error. Lista vacia")
    flag = True
    for valor in lista:
        if flag or valor > mayor:
            flag = False
            mayor = valor
    return mayor