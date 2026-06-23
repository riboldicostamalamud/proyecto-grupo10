import streamlit as st
import matplotlib.pyplot as plt
import numpy as np



#lee el dataset y devuelve una lista de diccionarios, donde cada diccionario
#representa una fila del archivo, se utilizan los nombres de la columnas
#como claves del diccionario
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


def main():
    st.title ("Proyecto Grupal de Programación")

    registros = leer_archivo("SampleSuperstore_geo.csv")
    mostrar_grafico_category(registros)

    
if __name__ == "__main__":
    main()
