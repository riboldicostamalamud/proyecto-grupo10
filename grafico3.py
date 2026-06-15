import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

#sumar_por_categoria : List[Dict] Str Str -> Dict[Str, float]
#la funcion toma una lista de de diccionario de los registros, una columna que se usara como categoria
#y otra columna numerica donde sus valores se sumaran
#devuelve un diccionario donde cada clave es un valor de la categoria(sin repetir)
#y cada valor es es la suma acumulada de la columna numerica dada
def sumar_por_categoria(registros, columna_categoria, columna_valor):
    acumulador = {}

    for registro in registros:
        categoria = registro[columna_categoria]
        valor = float(registro[columna_valor])

        if categoria in acumulador:
            acumulador[categoria] += valor
        else:
            acumulador[categoria] = valor

    return acumulador


#mostrar_grafico_barras : List[Dict] -> None
#toma una lista de diccionario del dataset
#calcula la suma de las ganancias para cada tipo de cliente
#crea un grafico de barras donde cada barra representa un tipo de cliente
#y su altura corresponde a las ganancias generadas
#muestra el grafico utilizando matplotlib
def mostrar_grafico_barras(registros):

    ganancias = sumar_por_categoria(registros, "Segment", "Profit")
    
    fig, ax = plt.subplots()

    fruits = ganancias.keys()
    counts = ganancias.values()
    bar_labels = ['red', 'blue', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Ganancias')
    ax.set_title('Tipo de clientes con mas ventas')

    plt.show()
    st.pyplot(fig)


def main():
    st.title ("Proyecto Grupal de Programación")

    registros = leer_archivo("SampleSuperstore_geo.csv")

    mostrar_grafico_barras(registros)
    
if __name__ == "__main__":
    main()
