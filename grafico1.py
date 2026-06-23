import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#nombre_archivo: str
#claves: list[str]
#datos: list[str]
#fila2: dict[str, str]
#leer_archivo: str -> list
#lee el dataset y devuelve una lista de diccionarios, donde cada diccionario
#representa una fila del archivo, se utilizan los nombres de la columnas
#como claves del diccionario
def leer_archivo(nombre_archivo):
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


#contador: dict
#contar_columna : list[dict] Str -> dict[str, int]
#dada una lista con los datos y el nombre de una columna
#devuelve un diccionario donde cada clave es la columna dada
#y su valor es la cantidad de veces que aparecio
def contar_columna(lista, columna):
    contador = {}

    for linea in lista:
        valor = linea[columna]

        if valor in contador:
            contador[valor] += 1
        else:
            contador[valor] = 1
    
    return contador



#porcentajes: dict[str, float]
#total: int
#porcentaje: float
#calcular_porcentajes_ship_mode: dict[str, int] -> list[float]
#dado un diccionario que contiene la columna como clave y la cantidad de veces que aparece como valor, devuelve un diccionario
#donde las claves son la columna y los valores son los porcentajes de utilizacion
def calcular_porcentajes_columna(contador):
    porcentajes = {}
    total = 0
    for cantidad in contador.values():
        total += cantidad

    for metodo in contador:
        porcentaje = contador[metodo] * 100 / total
        porcentajes[metodo] = porcentaje
    
    return porcentajes
        
#contador: dict[str, int]
#porcentajes: dict[str, float]
#mostrar_grafico_ship_mode: list[dict] -> None
#dada una lista con los registros, calcula la cantidad y el porcentaje de utilizacion
#de cada metodo de envio y muestre un grafico circular usando Matplotlib
def mostrar_grafico_ship_mode(registros):

    contador = contar_columna(registros,"Ship Mode")
    porcentajes = calcular_porcentajes_columna(contador)

    labels = porcentajes.keys()
    sizes = porcentajes.values()
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'size': 'smaller'}, radius=0.75)
    ax.set_title("¿Cuál es el porcentaje de utilizacion de cada envio?")
    st.pyplot(fig)

def main():
    registros = leer_archivo("SampleSuperstore_geo.csv")

    mostrar_grafico_ship_mode(registros)
    
if __name__ == "__main__":
    main()
