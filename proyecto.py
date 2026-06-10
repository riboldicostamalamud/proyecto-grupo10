import streamlit as st
import matplotlib.pyplot as plt

"""
nombre_archivo: str
claves: list[str]
datos: list[str]
fila2: dict[str, str]

leer_archivo: str -> list

lee el dataset y devuelve una lista de diccionarios, donde cada diccionario
representa una fila del archivo, se utilizan los nombres de la columnas
como claves del diccionario
"""
def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lista = []

    claves = archivo.readline()
    claves = encabezado.split(",")

    for fila in archivo:
        datos = fila.split(",")

        fila2 = {}

        for i in range(len(claves)):
            fila2[claves[i]] = datos[i]
        
        lista.append(fila2)

    archivo.close()

    return lista




def main():
    st.title ("Proyecto Grupal de Programación")
    st.write ("Empecemos a trabajar equipo!")



if __name__ == "__main__":
    main()
