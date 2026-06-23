import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.random import default_rng as rng

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

#filtrar_categorias: List[Dict] -> List[str]
#toma una lista de registros
#devuelve una lista con todas las categorias dentro
def filtrar_categorias(registros):
    categorias = []

    for registro in registros:
        if registro["Category"] not in categorias:
            categorias.append(registro["Category"])
    
    return categorias

#entrada_mapa: List[Dict] -> ....
#toma una lista de registros 
#devuelve un menu desplegable y un mapa
def entrada_mapa(registros):
    categorias = filtrar_categorias(registros)
    option = st.selectbox(
        "Sobre que categoria desea conocer las perdidas/ganancias",
        categorias,
        index=None,
        placeholder="Seleccione una categoria",
    )

    st.write("Usted selecciono:", option)
    if option is not None:
        mapa(registros, option)

#filtrar_longitudes : List[Dict] Str -> List[float]
#toma una lista de registros y un string que hace referencia a una categoria seleccionada
#devuelve una lista con todas las longitudes que dada una categoria seleccionada contenga profit negativo
def filtrar_longitudes(registros,seleccion):
    lista_inicial = []

    for registro in registros:
        if seleccion == registro["Category"]:
            if float(registro["Profit"]) < 0:
                lista_inicial.append(float(registro["Longitude\n"]))
    return lista_inicial

#filtrar_latitudes : List[Dict] Str -> List[float]
#toma una lista de registros y un string que hace referencia a una categoria seleccionada
#devuelve una lista con todas las latitudes que dada una categoria seleccionada contenga profit negativo
def filtrar_latitudes(registros,seleccion):
    lista_inicial = []

    for registro in registros:
        if seleccion == registro["Category"]:
            if float(registro["Profit"]) < 0:
                lista_inicial.append(float(registro["Latitude"]))
    return lista_inicial

#mapa : List[Dict] Str-> None
#toma una lista de registros y un string que hace referencia a una categoria seleccionada
#devuelve un mapa
def mapa(registros,seleccion):
    latitudes = filtrar_latitudes(registros,seleccion)
    longitudes = filtrar_longitudes(registros,seleccion)
    
    dic_aux = {"lat": latitudes,"lon": longitudes}

    st.map(dic_aux)

def main():
    registros = leer_archivo("SampleSuperstore_geo.csv")
    entrada_mapa(registros)
    
    
if __name__ == "__main__":
    main()
