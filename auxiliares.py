#representaremos el nombre del archivo como un string. y la salida sera la
#representacion del archivo del dataset que sera una lista de diccionarios.
#lee el dataset y devuelve una lista de diccionarios, donde cada diccionario
#representa una fila del archivo, se utilizan los nombres de la columnas
#como claves del diccionario (((y como valor lo que hay en cada columna)))
def leer_archivo(nombre_archivo:str)-> list[dict[str, str]]:
    archivo = open(nombre_archivo, "r")
    lista = []

    claves = archivo.readline()
    claves = claves.split(",")

    for fila in archivo:
        datos = fila.split(",")

        fila2 = {}

        for i in range(len(claves)):
            fila2[claves[i]] = datos[i]
        
        lista.append(fila2)

    archivo.close()

    return lista


#representaremos la lista a contar sera el dataset con la representacion implementada
#luego las columnas la representare como un string
#y la salida que es la aparicion de la columna y la cantidad de veces que aparece. la representare
#como un diccionario como clave la columna y valor la cantidad de veces que aparece
#dada una lista con los datos y el nombre de una columna
#devuelve un diccionario donde cada clave es la columna dada
#y su valor es la cantidad de veces que aparecio
def contar_columna(lista:list[dict], columna:str)-> dict[str, int]:
    contador = {}

    for linea in lista:
        valor = linea[columna]

        if valor in contador:
            contador[valor] += 1
        else:
            contador[valor] = 1
    
    return contador


#la entrada la representaremos como ya la habiamos representado el dataset
#la salida, como esperamos que devuelva una lista con los registros filtrados, la representaremos como una lista de strings 
#toma una lista de registros
#devuelve una lista con la columna pedida adentro sin repetir datos
def filtrar_columna(registros:list[dict], columna:[str])-> list[str]:
    filas = []

    for registro in registros:
        if registro[columna] not in filas:
            filas.append(registro[columna])
    
    return filas


#representaremos el contador de columnas como un diccionario con clave de la columna y valor la cantidad de veces que aparece
#y la salida que es un porcentaje con el uso de cada columna, sera representado como una lista de reales.
#dado un diccionario que contiene la columna como clave y la cantidad de veces que aparece como valor, devuelve un diccionario
#donde las claves son la columna y los valores son los porcentajes de utilizacion
def calcular_porcentajes_columna(contador:dict[str,int])-> list[float]:
    porcentajes = {}
    total = 0
    for cantidad in contador.values():
        total += cantidad

    for metodo in contador:
        porcentaje = contador[metodo] * 100 / total
        porcentajes[metodo] = porcentaje
    
    return porcentajes


#toma un diccionario y devuelve una lista con sus valores
def convertir_diccionario_a_lista_values(diccionario:dict)->list:
    lista = []
    for clave in diccionario:
        lista.append(diccionario[clave])
    
    return lista


#toma un diccionario y devuelve una lista con sus claves
def convertir_diccionario_a_lista_keys(diccionario:dict)-> list:
    lista = []
    for clave in diccionario.keys():
        lista.append(clave)
    
    return lista


#representaremos la entrada que es la representacion del dataset el cual es una lista de diccionarios,
# la columna de la categoria y el valor de la categoria como un string
#y la salida la representaremos como un diccionario con clave de un valor sin repetir y como valor la suma acumulada de la columna numerica
#la funcion toma una lista de de diccionario de los registros, una columna que se usara como categoria
#y otra columna numerica donde sus valores se sumaran
#devuelve un diccionario donde cada clave es un valor de la categoria(sin repetir)
#y cada valor es es la suma acumulada de la columna numerica dada
def sumar_por_categoria(registros:list[dict], columna_categoria:str, columna_valor:str)-> dict[str, float]:
    acumulador = {}

    for registro in registros:
        categoria = registro[columna_categoria]
        valor = float(registro[columna_valor])

        if categoria in acumulador:
            acumulador[categoria] += valor
        else:
            acumulador[categoria] = valor

    return acumulador
