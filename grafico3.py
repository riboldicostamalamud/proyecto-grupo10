import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from auxiliares import sumar_por_categoria

#representaremos la entrada que es el dataset como una lista de diccionario
#la salida la representaremos como un None ya que lo que hace es mostrar el grafico de barras
#toma una lista de diccionario del dataset
#calcula la suma de las ganancias para cada tipo de cliente
#crea un grafico de barras donde cada barra representa un tipo de cliente
#y su altura corresponde a las ganancias generadas
#muestra el grafico utilizando matplotlib
def mostrar_grafico_barras(registros:list[dict])-> None:

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

