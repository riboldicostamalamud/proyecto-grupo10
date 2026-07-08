import streamlit as st

from auxiliares import filtrar_columna, sumar_por_categoria


#la entrada la representaremos como ya la habiamos representado el dataset
#la salida que deseo que sea las subcategorias con el descuento maximo aplicado de esa subcategoria, la representaremos 
#como un diccionario con clave string y valor un real
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


#la entrada la representaremos como ya la habiamos representado el dataset y el porsentaje sera un entero
#la salida, como esperamos que devuelva una lista con los registros filtrados, la representaremos como una lista de diccionarios 
#toma los registros del dataset y un porcentaje de descuento
#filtra todos los registros que tengan un descuento mayor o igual al porcentaje
#devuelve una nueva lista con los registros filtrados con la condicion
def filtrar_registros(registros:list[dict],porcentaje:int)->list[dict]:
    porcentaje = porcentaje / 100
    registros_filtrados = []

    for registro in registros:
        if float(registro["Discount"]) >= porcentaje:
            registros_filtrados.append(registro)

    return registros_filtrados


#la salida como sera un valor del slider, sera representado como un int
#muestra un slider con los valores entre 10 y 80
#permite al usuario seleccionar un porcentaje de descuento
#devuelve el porcentaje elegido
def slider()->int :
    rango = range(10,81)
    porcentaje_slider = st.select_slider("descuento aplicado", options=rango)
    return porcentaje_slider


#la entrada la representaremos como ya la habiamos representado el dataset
#la salida como sera un dibujo , sera representado como un None
#toma una lista de registros del dataset
#obtiene el porcentaje seleccionado por el usuario
#filtra los registros segun dicho porcentaje
#calcula la informacion de cada subcategoria
#muestra una tabla con los descuentos maximos, cantidades vendidas, ventas y ganancias
#para crear la tabla se utiliza streamlit
def mostrar_tabla_slider(registros:list[dict])-> None:
    porcentaje = slider()

    registros_filtrados = filtrar_registros(registros,porcentaje)
    sub_categorias = filtrar_columna(registros_filtrados,"Sub-Category")
    cantidad_de_ventas = sumar_por_categoria(registros_filtrados,"Sub-Category","Quantity",int)
    descuentos_maximos = maximo_descuento_sub_categoria(registros_filtrados)
    ventas_con_descuento = sumar_por_categoria(registros_filtrados,"Sub-Category", "Sales",float)
    ganancias = sumar_por_categoria(registros_filtrados,"Sub-Category","Profit",float)

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

