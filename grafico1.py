import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from auxiliares import contar_columna, calcular_porcentajes_columna

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

