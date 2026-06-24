import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#representaremos la lista a contar sera el dataset con la representacion implementada
#y la salida que es la aparicion de la columna y la cantidad de veces que aparece. la representaremos
#con un diccionario como clave que es la categoria un string y la cantidad de veces como un entero
#dado el registro de todo el dataset
#devuelve un diccionario con la categoria y la cantidad de apariciones que tiene
def contar_category(lista:list[dict])-> dict[str, int]:
    contador = {}

    for linea in lista:
        categoria = linea["Category"]

        if categoria in contador:
            contador[categoria] += 1
        else:
            contador[categoria] = 1
        
    return contador


#representaremos el contador de columnas como un diccionario con clave de la columna y valor la cantidad de veces que aparece
#y la salida que es un porcentaje con el uso de cada columna, sera representado como una lista de reales.
#dado un diccionario que contiene la columna como clave y la cantidad de veces que aparece como valor, devuelve un diccionario
#donde las claves son la columna y los valores son los porcentajes de utilizacion
def calcular_porcentajes_category(contador:dict[str,int])-> list[float]:
    porcentajes = []
    total = 0
    for cantidad in contador.values():
        total += cantidad

    for metodo in contador:
        porcentaje = contador[metodo] * 100 / total
        porcentajes.append(porcentaje)
    
    return porcentajes


#representaremos la entrada que es el dataset como una lista de diccionarios. y la salida
#que sera mostrar el grafico como un None
#dado una lista con los registros, calcula los porcentajes de las categorias mas vendidas
#y lo muestra con un grafico circular usando Matplotlib
def mostrar_grafico_category(registros:list[dict])-> None:

    contador = contar_category(registros)
    
    lista2 = []
    for i in contador.keys():
        lista2.append(i)

    porcentajes = calcular_porcentajes_category(contador)

    recipe = lista2
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
