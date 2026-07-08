from auxiliares import filtrar_columna, convertir_diccionario_a_lista_keys, convertir_diccionario_a_lista_values, contar_columna, leer_archivo,calcular_porcentajes_columna, sumar_por_categoria
from grafico4 import filtrar_registros, maximo_descuento_sub_categoria
from grafico5 import filtrar_estados_por_region, filtrar_registros_por_estado
from grafico6 import filtrar_latitudes, filtrar_longitudes

archivo = "ejemplo_archivos.csv"

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
        "Longitude\n": "-87.59"
    }
]
registros_test_cord = [
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
        "Category": "Office Supplies",
        "Sub-Category": "Chairs",
        "Sales": "731.94",
        "Quantity": "3",
        "Discount": "0.5",
        "Profit": "-219.582",
        "Latitude": "200",
        "Longitude\n": "-900"
    }
]
#===================TEST_Auxiliar=======================
def test_auxiliares():
    assert (leer_archivo(archivo)) == registros

    assert contar_columna(registros, "Category") == {"Office Supplies": 1,"Furniture":3}
    assert contar_columna(registros, "Ship Mode") == {"Second Class":4}
    assert contar_columna({}, "Ship Mode") == {}

    assert filtrar_columna(registros,"Sub-Category") == ["Bookcases", "Chairs"]
    assert filtrar_columna(registros,"Region") == ["South"]
    assert filtrar_columna({},"Region") == []


    assert calcular_porcentajes_columna({"Office Supplies": 1,"Furniture":3}) == {"Office Supplies": 25.0,"Furniture": 75.0}
    assert calcular_porcentajes_columna({"Second Class":4}) == {"Second Class": 100}
    assert calcular_porcentajes_columna({}) == {}


    assert convertir_diccionario_a_lista_keys({"hola":123,"312":"hola"}) == ["hola","312"]
    assert convertir_diccionario_a_lista_keys({}) == []

    assert convertir_diccionario_a_lista_values({"hola":123,"312":"hola"}) == [123,"hola"]
    assert convertir_diccionario_a_lista_values({}) == []
    
    assert sumar_por_categoria(registros,"Segment", "Profit", float) == {"Consumer": 439.164}
    assert sumar_por_categoria(registros,"Sub-Category", "Sales", float) == {"Bookcases": 523.92, "Chairs": 1463.88}
    assert sumar_por_categoria({},"Sub-Category", "Sales", float) == {}



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
            "Longitude\n": "-87.59"
        }
    ]
    assert filtrar_registros(registros, 0) == registros
    assert filtrar_registros(registros, 90) == []
    assert filtrar_registros([], 50) == []

def test_maximo_descuento_sub_categoria():
    assert maximo_descuento_sub_categoria(registros) == {
        "Chairs" : 50,
        "Bookcases" : 10
    }
    assert maximo_descuento_sub_categoria([
        {"Sub-Category": "Tables", "Discount": "0.2"}
    ]) == {
        "Tables": 20.0
    }
    assert maximo_descuento_sub_categoria([]) == {}
    assert maximo_descuento_sub_categoria([
        {"Sub-Category": "Tables", "Discount": "0.3"},
        {"Sub-Category": "Tables", "Discount": "0.3"},
    ]) == {
        "Tables": 30.0
    }




#===================TEST_GRAFICO_6=======================
def test_funcionesgrafico6():
    assert filtrar_latitudes(registros,"Office Supplies") == [37.836111]
    assert filtrar_longitudes(registros,"Office Supplies") == [-100]
    assert filtrar_latitudes(registros_test_cord,"Office Supplies") == [37.836111,200]
    assert filtrar_longitudes(registros_test_cord,"Office Supplies") == [-100,-900]
    assert filtrar_latitudes(registros,"Technology") == []
    assert filtrar_longitudes(registros,"Furniture") == []
    assert filtrar_latitudes([], "Furniture") == []
    assert filtrar_longitudes([], "Furniture") == []
    assert filtrar_latitudes([
        {
            "Category": "Office Supplies",
            "Profit": "0",
            "Latitude": "10",
            "Longitude\n": "20"
        },
        {
            "Category": "Office Supplies",
            "Profit": "-5",
            "Latitude": "30",
            "Longitude\n": "40"
        }
    ], "Office Supplies") == [30]
    assert filtrar_longitudes([
        {
            "Category": "Office Supplies",
            "Profit": "0",
            "Latitude": "10",
            "Longitude\n": "20"
        },
        {
            "Category": "Office Supplies",
            "Profit": "-5",
            "Latitude": "30",
            "Longitude\n": "40"
        }
    ], "Office Supplies") == [40]







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
    assert filtrar_estados_por_region(registros_grafico5(),"South") == ["Kentucky","Florida"]
    assert filtrar_estados_por_region(registros_grafico5(),"West") == ["California"]
    assert filtrar_estados_por_region(registros_grafico5(), "North") == []
    assert filtrar_estados_por_region([], "South") == []
    assert filtrar_registros_por_estado(registros_grafico5(),"Kentucky") == [{"Region": "South", "State": "Kentucky", "Category": "Furniture", "Quantity": "2"},{"Region": "South", "State": "Kentucky", "Category": "Office Supplies", "Quantity": "5"}]
    assert filtrar_registros_por_estado(registros_grafico5(),"Florida") == [{"Region": "South", "State": "Florida", "Category": "Technology", "Quantity": "1"}]
    assert filtrar_registros_por_estado(registros_grafico5(), "Texas") == []
    assert filtrar_registros_por_estado([], "Kentucky") == []



