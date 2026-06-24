import streamlit as st

from auxiliares import convertir_diccionario_a_lista_keys, convertir_diccionario_a_lista_values, sumar_por_categoria

#filtrar_regiones : List[Dict] -> List[str]
#toma una lista de registros
#devuelve una lista con todas las regiones sin repetir
def filtrar_regiones(registros):
    regiones = []

    for registro in registros:
        if registro["Region"] not in regiones:
            regiones.append(registro["Region"])

    return regiones


#filtrar_estados_por_region : List[Dict] Str -> List[str]
#toma una lista de registros y una region seleccionada
#devuelve una lista con los estados sin repetir que pertenecen a esa region
def filtrar_estados_por_region(registros, region):
    estados = []

    for registro in registros:
        if registro["Region"] == region:
            if registro["State"] not in estados:
                estados.append(registro["State"])

    return estados


#filtrar_registros_por_estado : List[Dict] Str -> List[Dict]
#toma una lista de registros y un estado seleccionado
#devuelve una lista con los registros que pertenecen a ese estado
def filtrar_registros_por_estado(registros, estado):
    registros_filtrados = []

    for registro in registros:
        if registro["State"] == estado:
            registros_filtrados.append(registro)

    return registros_filtrados


#mostrar_grafico_categorias_vendidas : List[Dict] Str -> None
#toma una lista de registros ya filtrados por estado y el nombre del estado
#calcula la cantidad de unidades vendidas (Quantity) por categoria
#muestra un grafico de barras horizontal usando st.bar_chart
def mostrar_grafico_categorias_vendidas(registros_filtrados, estado):
    unidades = sumar_por_categoria(registros_filtrados, "Category", "Quantity")

    categorias = convertir_diccionario_a_lista_keys(unidades)
    cantidades = convertir_diccionario_a_lista_values(unidades)

    datos = {"Categoria": categorias, "Cantidad de unidades": cantidades}

    st.subheader(f"Categorias mas vendidas en {estado}")
    st.bar_chart(datos, x="Categoria", y="Cantidad de unidades", horizontal=True)


#entrada_region_estado : List[Dict] -> None
#toma una lista de registros
#muestra un selectbox de regiones y, segun la region elegida, un selectbox de estados
#si se selecciono region y estado, filtra los registros y muestra el grafico de categorias mas vendidas
def entrada_region_estado(registros):
    regiones = filtrar_regiones(registros)

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

