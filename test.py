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
    assert (filtrar_latitudes(registros,"Technology")) == []
    assert (filtrar_longitudes(registros,"Furniture")) == []






#===================TEST_GRAFICO_5=======================
def registros_grafico5():
    return [
        {"Region": "South", "State": "Kentucky", "Category": "Furniture", "Quantity": "2"},
        {"Region": "South", "State": "Kentucky", "Category": "Office Supplies", "Quantity": "5"},
        {"Region": "South", "State": "Florida", "Category": "Technology", "Quantity": "1"},
        {"Region": "West", "State": "California", "Category": "Furniture", "Quantity": "3"},
        {"Region": "West", "State": "California", "Category": "Furniture", "Quantity": "4"},
    ]


def test_funcionesgrafico5():
    assert(filtrar_estados_por_region(registros_grafico5(),"South")) == ["Kentucky","Florida"]
    assert(filtrar_estados_por_region(registros_grafico5(),"West")) == ["California"]
    assert(filtrar_registros_por_estado(registros_grafico5(),"Kentucky")) == [{"Region": "South", "State": "Kentucky", "Category": "Furniture", "Quantity": "2"},{"Region": "South", "State": "Kentucky", "Category": "Office Supplies", "Quantity": "5"}]
    assert(filtrar_registros_por_estado(registros_grafico5(),"Florida")) == [{"Region": "South", "State": "Florida", "Category": "Technology", "Quantity": "1"}]



