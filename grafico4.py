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


#toma la lista de diccionarios con los datos del dataset filtrados con el descuento
#crea y devuelve una lista con los nombres de las subcategorias sin repetir
def filtrar_sub_categorias(registros_filtrados:list[dict])->list[str]:
    sub_categorias = []

    for registro in registros_filtrados:
        if registro["Sub-Category"] not in sub_categorias:
            sub_categorias.append(registro["Sub-Category"])
    
    return sub_categorias


#toma una lista con los registros filtrados
#devuelve un diccionario con cuya clave es una subcategoria
#y el valor es la suma de las cantidades de vendidas de esa subcategoria
def filtrar_cantidad_de_ventas(registros_filtrados:list[dict])->dict[str, int]:
    acumulador = {}

    for registro in registros_filtrados:
        subcategoria = registro["Sub-Category"]
        cantidad = int(registro["Quantity"])

        if subcategoria in acumulador:
            acumulador[subcategoria] += cantidad
        else:
            acumulador[subcategoria] = cantidad

    return acumulador


#toma una lista de registros filtrados
#devuelve un diccionario cuya clave es la subctegoria
#y el valor es el descuento maximo aplicado a esa categoria
def maximo_descuento_sub_categoria(registros_filtrados:list[dict])->dict[str, float]:
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



#toma una lista de registros filtrados y el nombre de una de las columnas
#devuelve un diccionario cuya clave es una subcategoria
#y el valor es la suma de los valores de esa columna para dicha categoria
def sumar_por_subcategoria(registros_filtrados:list[dict], columna:str)-> dict[str, float]:
    acumulador = {}

    for registro in registros_filtrados:
        subcategoria = registro["Sub-Category"]
        valor = float(registro[columna])

        if subcategoria in acumulador:
            acumulador[subcategoria] += valor
        else:
            acumulador[subcategoria] = valor
    
    return acumulador


#filtrar_registros : List[dict] int -> List[dict] 
#toma los registros del dataset y un porcentaje de descuento
#filtra todos los registros que tengan un descuento mayor o igual al porcentaje
#devuelve una nueva lista con los registros filtrados con la condicion
def filtrar_registros(registros,porcentaje):
    porcentaje = porcentaje / 100
    registros_filtrados = []

    for registro in registros:
        if float(registro["Discount"]) >= porcentaje:
            registros_filtrados.append(registro)

    return registros_filtrados


#slider : None -> Int
#muestra un slider con los valores entre 0 y 100
#permite al usuario seleccionar un porcentaje de descuento
#devuelve el porcentaje elegido
def slider()->int :
    rango = range(10,81)
    porcentaje_slider = st.select_slider("descuento aplicado", options=rango)
    return porcentaje_slider


#toma una lista de registros del dataset
#obtiene el porcentaje seleccionado por el usuario
#filtra los registros segun dicho porcentaje
#calcula la informacion de cada subcategoria
#muestra una tabla con los descuentos maximos, cantidades vendidas, ventas y ganancias
#para crear la tabla se utiliza streamlit
def mostrar_tabla_slider(registros:list[dict])-> None:
    porcentaje = slider()

    registros_filtrados = filtrar_registros(registros,porcentaje)
    sub_categorias = filtrar_sub_categorias(registros_filtrados)
    cantidad_de_ventas = filtrar_cantidad_de_ventas(registros_filtrados)
    descuentos_maximos = maximo_descuento_sub_categoria(registros_filtrados)
    ventas_con_descuento = sumar_por_subcategoria(registros_filtrados, "Sales")
    ganancias = sumar_por_subcategoria(registros_filtrados,"Profit")

    filas = []

    for sub_categoria in sub_categorias:
        filas.append({
            "Sub-Categoria": sub_categoria,
            "Descuento maximo": f"{descuentos_maximos[sub_categoria]:.1f}%",
            "Cantidad de ventas": cantidad_de_ventas[sub_categoria],
            "Ventas": f"${ventas_con_descuento[sub_categoria]:.2f}",
            "Ganancias": f"${ganancias[sub_categoria]:.2f}",
        })

    return st.table(filas)


def main():
    st.title ("Proyecto Grupal de Programación")

    registros = leer_archivo("SampleSuperstore_geo.csv")
    mostrar_tabla_slider(registros)


    
if __name__ == "__main__":
    main()
