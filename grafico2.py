import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from auxiliares import contar_columna, calcular_porcentajes_columna, convertir_diccionario_a_lista_keys, convertir_diccionario_a_lista_values

#representaremos la entrada que es el dataset como una lista de diccionarios. y la salida
#que sera mostrar el grafico como un None
#dado una lista con los registros, calcula los porcentajes de las categorias mas vendidas
#y lo muestra con un grafico circular usando Matplotlib
def mostrar_grafico_category(registros:list[dict])-> None:

    contador = contar_columna(registros,"Category")
    porcentajes = calcular_porcentajes_columna(contador)

    contador = convertir_diccionario_a_lista_keys(contador)
    porcentajes = convertir_diccionario_a_lista_values(porcentajes)

    recipe = contador
    data = porcentajes

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
 
    wedges, texts, autotexts = ax.pie(data, autopct='%1.1f%%',pctdistance=0.75, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),horizontalalignment=horizontalalignment, **kw)
    plt.setp(autotexts, size=8, weight="bold",)
    ax.set_title("¿Cuáles son las categorias que vendieron mas unidades?")
    st.pyplot(fig)
    plt.show()
