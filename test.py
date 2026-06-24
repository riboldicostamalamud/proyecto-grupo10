from auxiliares import contar_columna
from auxiliares import filtrar_columna, convertir_diccionario_a_lista_keys, convertir_diccionario_a_lista_values
from grafico4 import filtrar_registros, maximo_descuento_sub_categoria, filtrar_cantidad_de_ventas
from grafico5 import filtrar_estados_por_region, filtrar_registros_por_estado
from grafico6 import filtrar_latitudes, filtrar_longitudes

registros = [
    {
        "Ship Mode": "Second Class",
        "Segment": "Consumer",
        "Country": "United States",
        "City": "Henderson",
        "State": "Kentucky",
        "Postal Code": "42420",
        "Region": "South",
        "Category": "Office Supplies",
        "Sub-Category": "Bookcases",
        "Sales": "261.96",
        "Quantity": "2",
        "Discount": "0.0",
        "Profit": "-41.9136",
        "Latitude": "37.836111",
        "Longitude\n": "-100\n"
    },
    {
        "Ship Mode": "Second Class",
        "Segment": "Consumer",
        "Country": "United States",
        "City": "Henderson",
        "State": "Kentucky",
        "Postal Code": "42420",
        "Region": "South",
        "Category": "Furniture",
        "Sub-Category": "Bookcases",
        "Sales": "261.96",
        "Quantity": "2",
        "Discount": "0.1",
        "Profit": "41.9136",
        "Latitude": "37.836111",
        "Longitude\n": "-87.59\n"
    },
    {
        "Ship Mode": "Second Class",
        "Segment": "Consumer",
        "Country": "United States",
        "City": "Henderson",
        "State": "Kentucky",
        "Postal Code": "42420",
        "Region": "South",
        "Category": "Furniture",
        "Sub-Category": "Chairs",
        "Sales": "731.94",
        "Quantity": "3",
        "Discount": "0.1",
        "Profit": "219.582",
        "Latitude": "37.836111",
        "Longitude\n": "-87.59\n"
    },
    {
        "Ship Mode": "Second Class",
        "Segment": "Consumer",
        "Country": "United States",
        "City": "Henderson",
        "State": "Kentucky",
        "Postal Code": "42420",
        "Region": "South",
        "Category": "Furniture",
        "Sub-Category": "Chairs",
        "Sales": "731.94",
        "Quantity": "3",
        "Discount": "0.5",
        "Profit": "219.582",
        "Latitude": "37.836111",
        "Longitude\n": "-87.59\n"
    }
]




#===================TEST_GRAFICO_4=======================
def test_filtrar_registros():
    assert filtrar_registros(registros, 50) == [
        {
            "Ship Mode": "Second Class",
            "Segment": "Consumer",
            "Country": "United States",
            "City": "Henderson",
            "State": "Kentucky",
            "Postal Code": "42420",
            "Region": "South",
            "Category": "Furniture",
            "Sub-Category": "Chairs",
            "Sales": "731.94",
            "Quantity": "3",
            "Discount": "0.5",
            "Profit": "219.582",
            "Latitude": "37.836111",
            "Longitude\n": "-87.59\n"
        }
    ]
    assert filtrar_registros(registros, 0) == registros
    assert filtrar_registros(registros, 90) == []

def test_maximo_descuento_sub_categoria():
    assert maximo_descuento_sub_categoria(registros) == {
        "Chairs" : 50,
        "Bookcases" : 10
    }




#===================TEST_GRAFICO_6=======================
def test_funcionesgrafico6():
    assert (filtrar_latitudes(registros,"Office Supplies")) == [37.836111]
    assert (filtrar_longitudes(registros,"Office Supplies")) == [-100]






#===================TEST_GRAFICO_5=======================
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