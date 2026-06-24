import streamlit as st

from auxiliares import convertir_diccionario_a_lista_keys, convertir_diccionario_a_lista_values, sumar_por_categoria, filtrar_columna

#la entrada la representaremos como ya la habiamos representado el dataset y la region sera representada como un string
#la salida que es una lista que no repite estados que pertencen a la region, sera representada por una lista de strings
#toma una lista de registros y una region seleccionada
#devuelve una lista con los estados sin repetir que pertenecen a esa region
def filtrar_estados_por_region(registros:list[dict], region:str)-> list[str]:
    estados = []

    for registro in registros:
        if registro["Region"] == region:
            if registro["State"] not in estados:
                estados.append(registro["State"])

    return estados


#la entrada la representaremos como ya la habiamos representado el dataset y el estado sera representada como un string
#la salida que es una lista con los registros que pertencen al estado, sera representado como una lista de diccionarios
#toma una lista de registros y un estado seleccionado
#devuelve una lista con los registros que pertenecen a ese estado
def filtrar_registros_por_estado(registros:list[dict], estado:str)-> list[dict]:
    registros_filtrados = []

    for registro in registros:
        if registro["State"] == estado:
            registros_filtrados.append(registro)

    return registros_filtrados


#el registro filtrado sera representado como una lista de diccionarios, y el estado como un string
#la salida como lo unico que hace es devolver un grafico, sera None
#toma una lista de registros ya filtrados por estado y el nombre del estado
#calcula la cantidad de unidades vendidas (Quantity) por categoria
#muestra un grafico de barras horizontal usando st.bar_chart
def mostrar_grafico_categorias_vendidas(registros_filtrados:list[dict], estado:str)-> None:
    unidades = sumar_por_categoria(registros_filtrados, "Category", "Quantity")

    categorias = convertir_diccionario_a_lista_keys(unidades)
    cantidades = convertir_diccionario_a_lista_values(unidades)

    datos = {"Categoria": categorias, "Cantidad de unidades": cantidades}

    st.subheader(f"Categorias mas vendidas en {estado}")
    st.bar_chart(datos, x="Categoria", y="Cantidad de unidades", horizontal=True)



#la entrada la representaremos como ya la habiamos representado el dataset
#y la salida como muestra un selectbox con los estados sera None
#toma una lista de registros
#muestra un selectbox de regiones y, segun la region elegida, un selectbox de estados
#si se selecciono region y estado, filtra los registros y muestra el grafico de categorias mas vendidas
def entrada_region_estado(registros:list[dict])-> None:
    regiones = filtrar_columna(registros,"Region")

    region = st.selectbox(
        "Regiones",
        regiones,
        index=None,
        placeholder="Seleccione una region",
    )

    if region is not None:
        estados = filtrar_estados_por_region(registros, region)

        estado = st.selectbox(
            "Estado",
            estados,
            index=None,
            placeholder="Seleccione un estado",
        )

        if estado is not None:
            registros_filtrados = filtrar_registros_por_estado(registros, estado)
            mostrar_grafico_categorias_vendidas(registros_filtrados, estado)
