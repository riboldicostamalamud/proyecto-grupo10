import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import default_rng as rng

#la entrada la representaremos como ya la habiamos representado el dataset
#la salida, como esperamos que devuelva una lista con los registros filtrados, la representaremos como una lista de strings 
#toma una lista de registros
#devuelve una lista con todas las categorias dentro
def filtrar_categorias(registros:list[dict])-> list[str]:
    categorias = []

    for registro in registros:
        if registro["Category"] not in categorias:
            categorias.append(registro["Category"])
    
    return categorias


#la entrada la representaremos como ya la habiamos representado el dataset
#y la salida como sera una muestra del mapa sera None
#toma una lista de registros 
#devuelve un menu desplegable y un mapa
def entrada_mapa(registros:list[dict])-> None:
    categorias = filtrar_categorias(registros)
    option = st.selectbox(
        "Sobre que categoria desea conocer las perdidas",
        categorias,
        index=None,
        placeholder="Seleccione una categoria",
    )

    st.write("Usted selecciono:", option)
    if option is not None:
        mapa(registros, option)


#la entrada la representaremos como ya la habiamos representado el dataset y la seleccion la representare como un string
#y la salida como espereo una lista filtrada con unicamente las longitudes, sera un lista de float
#toma una lista de registros y un string que hace referencia a una categoria seleccionada
#devuelve una lista con todas las longitudes que dada una categoria seleccionada contenga profit negativo
def filtrar_longitudes(registros: list[dict], seleccion:str)-> list[float]:
    lista_inicial = []

    for registro in registros:
        if seleccion == registro["Category"]:
            if float(registro["Profit"]) < 0:
                lista_inicial.append(float(registro["Longitude\n"]))
    return lista_inicial


#la entrada la representaremos como ya la habiamos representado el dataset y la seleccion la representare como un string
#y la salida como espereo una lista filtrada con unicamente las latitudes, sera un lista de float
#toma una lista de registros y un string que hace referencia a una categoria seleccionada
#devuelve una lista con todas las latitudes que dada una categoria seleccionada contenga profit negativo
def filtrar_latitudes(registros:list[dict],seleccion:str)-> list[float]:
    lista_inicial = []

    for registro in registros:
        if seleccion == registro["Category"]:
            if float(registro["Profit"]) < 0:
                lista_inicial.append(float(registro["Latitude"]))
    return lista_inicial


#la entrada la representaremos como ya la habiamos representado el dataset y la seleccion la representare como un string
#y como la salidasera el grafico del mapa, sera un None
#toma una lista de registros y un string que hace referencia a una categoria seleccionada
#devuelve un mapa
def mapa(registros:list[dict], seleccion:str)-> None:
    latitudes = filtrar_latitudes(registros,seleccion)
    longitudes = filtrar_longitudes(registros,seleccion)
    
    dic_aux = {"lat": latitudes,"lon": longitudes}

    st.map(dic_aux)
