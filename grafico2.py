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




def contar_ship_mode(lista):
    contador = {}

    for linea in lista:
        ship_mode = linea["Category"]

        if ship_mode in contador:
            contador[ship_mode] += 1
        else:
            contador[ship_mode] = 1
        
    return contador

def calcular_porcentajes_ship_mode(contador):
    porcentajes = []
    total = 0
    for cantidad in contador.values():
        total += cantidad

    for metodo in contador:
        porcentaje = contador[metodo] * 100 / total
        porcentajes.append(porcentaje)
    
    return porcentajes


def mostrar_grafico_ship_mode(registros):

    contador = contar_ship_mode(registros)
    
    lista2 = []
    for i in contador.keys():
        lista2.append(i)

    porcentajes = calcular_porcentajes_ship_mode(contador)

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


def main():
    st.title ("Proyecto Grupal de Programación")

    registros = leer_archivo("SampleSuperstore_geo.csv")
    mostrar_grafico_ship_mode(registros)

    
if __name__ == "__main__":
    main()
