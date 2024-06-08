from funciones import *

def menu():
    limpiar_pantalla()
    print(f"""MENU DE OPCIONES
A- Cargar archivo CSV: Se pedirá el nombre del archivo y se cargará en una lista de diccionarios
los elementos del mismo. Informar que se ha cargado con éxito.
B- Imprimir lista: Se imprimirá por pantalla la tabla con los datos de los posts.
C- Asignar estadísticas: Se deberá mapear la lista con una función que asignará a cada post un
valor de likes entre 500 y 3000, dislikes con valores entre 300 y 3500 y followers entre 10000 y
20000. calculados de manera aleatoria.
D- Filtrar por mejores posts: Se deberá generar un archivo igual al original, pero donde solo
aparezcan los posts con más de 2000 likes.
E- Filtrar por haters: Se deberá generar un archivo igual al original, pero donde solo aparezcan
posts donde la cantidad de dislikes supere a la de likes.
F- Informar promedio de followers: Informar por consola el promedio de followers.
G- Ordenar los datos por nombre de user ascendente: Se deberán ordenar los datos y al listado
ordenado guardarlo en un archivo en formato JSON.
H- Mostrar más popular: Informar el nombre del user o users con el posteo más likeado. Y cuál es
ese número.
I- Salir.
""")
    return input("Ingrese opcion: ").upper()

while True:
    match menu():
        case "A":
            #Cargar archivo CSV: Se pedirá el nombre del archivo y se cargará en una lista de diccionarios los elementos del mismo. Informar que se ha cargado con éxito.
            with open(get_path_actual("posts.csv"), "r", encoding = "utf-8") as archivo:
                lista = []
                encabezado = archivo.readline().strip("\n").split(",")
                
                for linea in archivo.readlines():
                    persona = {}
                    linea = linea.strip("\n").split(",")

                    id, user, likes, dislikes, followers = linea
                    persona["id"] = int(id)
                    persona["user"] = user
                    persona["likes"] = int(likes)
                    persona["dislikes"] = int(dislikes)
                    persona["followers"] = int(followers)
                    lista.append(persona)
            print("Archivo cargado correctamente.")
        case "B":
            #2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de los posts.
            print("ID       User              Likes        Dislikes     Followers  ")
            print("----------------------------------------------------------------")
            for i in lista:
                mostrar_post(i)
            print("\n")
        case "C":
            #3) Asignar estadísticas: Se deberá mapear la lista con una función que asignará a cada post un valor de likes entre 500 y 3000, dislikes con valores entre 300 y 3500 y followers entre 10000 y 20000. calculados de manera aleatoria.

            asignacion_estadisticas = mapear_lista(valores_random, lista)

            print("ID       User              Likes        Dislikes     Followers  ")
            print("----------------------------------------------------------------")
            for i in lista:
                mostrar_post(i)
        case "D":
            #4) Filtrar por mejores posts: Se deberá generar un archivo igual al original, pero donde solo aparezcan los posts con más de 2000 likes.

            posts_2000_likes = filtrar_lista(filtrar_posts_2000_likes, lista)

            with open(get_path_actual("posts_2000_likes.csv"), "w", encoding = "utf-8") as archivo:
                encabezado = ",".join(list(lista[0].keys())) + "\n"
                archivo.write(encabezado)
                for persona in posts_2000_likes:
                    values = list(persona.values())
                    l = []
                    for value in values:
                        if isinstance(value, int):
                            l.append(str(value))
                        elif isinstance(value, float):
                            l.append(str(value))
                        else:
                            l.append(value)
                        
                    linea = ",".join(l) + "\n"
                    archivo.write(linea)
            print("Archivo cargado correctamente.")
        case "E":
            #5) Filtrar por haters: Se deberá generar un archivo igual al original, pero donde solo aparezcan posts donde la cantidad de dislikes supere a la de likes.

            haters = filtrar_lista(funcion_haters, lista)

            with open(get_path_actual("haters.csv"), "w", encoding = "utf-8") as archivo:
                encabezado = ",".join(list(lista[0].keys())) + "\n"
                archivo.write(encabezado)
                for persona in haters:
                    values = list(persona.values())
                    l = []
                    for value in values:
                        if isinstance(value, int):
                            l.append(str(value))
                        elif isinstance(value, float):
                            l.append(str(value))
                        else:
                            l.append(value)
                        
                    linea = ",".join(l) + "\n"
                    archivo.write(linea)
            print("Archivo cargado correctamente.")
        case "F":
            #6) Informar promedio de followers: Informar por consola el promedio de followers.
            with open(get_path_actual("posts_2000_likes.csv"), "a", encoding = "utf-8") as archivo:
                followers = []
                for i in followers:
                    followers.append(i["followers"])
                suma_followers = sumar_lista(followers)
                promedio_followers = promedio_lista(followers)
        case "G":
            #7) Ordenar los datos por nombre de user ascendente: Se deberán ordenar los datos y al listado ordenado guardarlo en un archivo en formato JSON.
            pass
        case "H":
            #8) Mostrar más popular: Informar el nombre del user o users con el posteo más likeado. cuál es ese número.
            with open(get_path_actual("posts_2000_likes.csv"), "a", encoding = "utf-8") as archivo:
                likes = []
                for i in likes:
                    likes.append(i["likes"])
                print(likes)
        case "I":
            break

    pausa()