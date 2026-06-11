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

def filtrar_sub_categorias(registros):
    sub_categorias = []

    for metodo in registros:
        if metodo["Sub-Category"] not in sub_categorias:
            sub_categorias.append(metodo["Sub-Category"])
    
    return sub_categorias

def filtrar_cantidad_de_ventas(registros_filtrados):
    acumulador = {}

    for registro in registros_filtrados:
        subcategoria = registro["Sub-Category"]
        cantidad = int(registro["Quantity"])

        if subcategoria in acumulador:
            acumulador[subcategoria] += cantidad
        else:
            acumulador[subcategoria] = cantidad

    return acumulador

def maximo_descuento_sub_categoria(registros_filtrados):
    maximos = {}

    for registro in registros_filtrados:
        sub_categoria = registro["Sub-Category"]
        descuento = float(registro["Discount"])

        if sub_categoria not in maximos:
            maximos[sub_categoria] = descuento
        elif descuento > maximos[sub_categoria]:
            maximos[sub_categoria] = descuento

    for key in maximos:
        maximos[key] = round(float(maximos[key]) * 100, 1)

    return maximos


def total_ventas(registros_filtrados):
    ventas = {}

    for registro in registros_filtrados:
        subcategoria = registro["Sub-Category"]
        venta = float(registro["Sales"])

        if subcategoria in ventas:
            ventas[subcategoria] += venta
        else:
            ventas[subcategoria] = venta

    return ventas

def total_ganancias(registros_filtrados):
    ganancias = {}

    for registro in registros_filtrados:
        subcategoria = registro["Sub-Category"]
        ganancia = float(registro["Profit"])

        if subcategoria in ganancias:
            ganancias[subcategoria] += ganancia
        else:
            ganancias[subcategoria] = ganancia
    
    return ganancias


def filtrar_registros(registros,porcentaje):
    porcentaje = porcentaje / 100
    registros_filtrados = []

    for registro in registros:
        if float(registro["Discount"]) >= porcentaje:
            registros_filtrados.append(registro)

    return registros_filtrados


def slider():
    rango = range(0,100)
    porcentaje_slider = st.select_slider("descuento aplicado", options=rango)
    return porcentaje_slider


def mostrar_tabla_slider(registros):
    porcentaje = slider()

    registros_filtrados = filtrar_registros(registros,porcentaje)
    sub_categorias = filtrar_sub_categorias(registros_filtrados)
    cantidad_de_ventas = filtrar_cantidad_de_ventas(registros_filtrados)
    descuentos_maximos = maximo_descuento_sub_categoria(registros_filtrados)
    ventas_con_descuento = total_ventas(registros_filtrados)
    ganancias = total_ganancias(registros_filtrados)

    filas = []

    for sub_categoria in sub_categorias:
        filas.append({
            "Sub-Categoria": sub_categoria,
            "Descuento maximo": f"{descuentos_maximos[sub_categoria]:.1f}%",
            "Cantidad de ventas": cantidad_de_ventas[sub_categoria],
            "Ventas": f"${ventas_con_descuento[sub_categoria]:.2f}",
            "Ganancias": f"${ganancias[sub_categoria]:.2f}",
        })

    tabla = pd.DataFrame(filas)

    return st.table(tabla)


def main():
    st.title ("Proyecto Grupal de Programación")

    registros = leer_archivo("SampleSuperstore_geo.csv")

    mostrar_tabla_slider(registros)


    
if __name__ == "__main__":
    main()
