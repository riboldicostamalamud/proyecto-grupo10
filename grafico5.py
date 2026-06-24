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

# Datos de prueba: una lista chica e inventada de registros,
# con la misma forma (mismas claves) que las filas del Dataset real.
def registros_de_prueba():
    return [
        {"Region": "South", "State": "Kentucky", "Category": "Furniture", "Quantity": "2"},
        {"Region": "South", "State": "Kentucky", "Category": "Office Supplies", "Quantity": "5"},
        {"Region": "South", "State": "Florida", "Category": "Technology", "Quantity": "1"},
        {"Region": "West", "State": "California", "Category": "Furniture", "Quantity": "3"},
        {"Region": "West", "State": "California", "Category": "Furniture", "Quantity": "4"},
    ]


# ---------------------------------------------------------
# Tests de filtrar_columna (version generica usada en el proyecto)
# ---------------------------------------------------------

def test_filtrar_columna_regiones_sin_repetidos(registros_de_prueba):
    resultado = filtrar_columna(registros_de_prueba, "Region")
    assert resultado == ["South", "West"]


def test_filtrar_columna_lista_vacia():
    resultado = filtrar_columna([], "Region")
    assert resultado == []


# ---------------------------------------------------------
# Tests de filtrar_estados_por_region
# ---------------------------------------------------------

def test_filtrar_estados_por_region_south(registros_de_prueba):
    resultado = filtrar_estados_por_region(registros_de_prueba, "South")
    assert resultado == ["Kentucky", "Florida"]


def test_filtrar_estados_por_region_west(registros_de_prueba):
    resultado = filtrar_estados_por_region(registros_de_prueba, "West")
    assert resultado == ["California"]


def test_filtrar_estados_por_region_inexistente(registros_de_prueba):
    resultado = filtrar_estados_por_region(registros_de_prueba, "North")
    assert resultado == []


# ---------------------------------------------------------
# Tests de filtrar_registros_por_estado
# ---------------------------------------------------------

def test_filtrar_registros_por_estado_kentucky(registros_de_prueba):
    resultado = filtrar_registros_por_estado(registros_de_prueba, "Kentucky")
    assert len(resultado) == 2
    assert all(registro["State"] == "Kentucky" for registro in resultado)


def test_filtrar_registros_por_estado_devuelve_filas_completas(registros_de_prueba):
    resultado = filtrar_registros_por_estado(registros_de_prueba, "Florida")
    assert resultado == [
        {"Region": "South", "State": "Florida", "Category": "Technology", "Quantity": "1"}
    ]


# ---------------------------------------------------------
# Tests de sumar_por_categoria
# ---------------------------------------------------------

def test_sumar_por_categoria_suma_correctamente(registros_de_prueba):
    california = filtrar_registros_por_estado(registros_de_prueba, "California")
    resultado = sumar_por_categoria(california, "Category", "Quantity")
    # Las dos filas de California son Furniture: 3 + 4 = 7
    assert resultado == {"Furniture": 7.0}


def test_sumar_por_categoria_categorias_distintas(registros_de_prueba):
    kentucky = filtrar_registros_por_estado(registros_de_prueba, "Kentucky")
    resultado = sumar_por_categoria(kentucky, "Category", "Quantity")
    assert resultado == {"Furniture": 2.0, "Office Supplies": 5.0}


# ---------------------------------------------------------
# Tests de convertir_diccionario_a_lista_keys / values
# ---------------------------------------------------------

def test_convertir_diccionario_a_lista_keys():
    diccionario = {"Furniture": 7.0, "Office Supplies": 5.0}
    resultado = convertir_diccionario_a_lista_keys(diccionario)
    assert resultado == ["Furniture", "Office Supplies"]


def test_convertir_diccionario_a_lista_values():
    diccionario = {"Furniture": 7.0, "Office Supplies": 5.0}
    resultado = convertir_diccionario_a_lista_values(diccionario)
    assert resultado == [7.0, 5.0]


# ---------------------------------------------------------
# Test de integracion: la cadena completa, de punta a punta
# ---------------------------------------------------------

def test_flujo_completo_region_estado_categoria(registros_de_prueba):
    # Simula lo que hace el usuario: elegir region, despues estado,
    # y ver el resultado final que se usaria en el grafico.
    estados_en_south = filtrar_estados_por_region(registros_de_prueba, "South")
    assert "Kentucky" in estados_en_south

    registros_kentucky = filtrar_registros_por_estado(registros_de_prueba, "Kentucky")
    unidades = sumar_por_categoria(registros_kentucky, "Category", "Quantity")

    assert unidades == {"Furniture": 2.0, "Office Supplies": 5.0}