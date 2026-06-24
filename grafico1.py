import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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


#representare el contador de columnas como un diccionario con clave de la columna y valor la cantidad de veces que aparece
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
        

#representaremos la entrada que es el dataset como una lista de diccionarios. y la salida
#que sera mostrar el grafico como un None
#dada una lista con los registros, calcula la cantidad y el porcentaje de utilizacion
#de cada metodo de envio y muestre un grafico circular usando Matplotlib
def mostrar_grafico_ship_mode(registros:list[dict])-> None:

    contador = contar_columna(registros,"Ship Mode")
    porcentajes = calcular_porcentajes_columna(contador)

    labels = porcentajes.keys()
    sizes = porcentajes.values()
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'size': 'smaller'}, radius=0.75)
    ax.set_title("¿Cuál es el porcentaje de utilizacion de cada envio?")
    st.pyplot(fig)

