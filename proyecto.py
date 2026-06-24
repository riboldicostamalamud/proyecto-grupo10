import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


#claves: list[str]
#datos: list[str]
#fila2: dict[str, str]
#leer_archivo: str -> list
#lee el dataset y devuelve una lista de diccionarios, donde cada diccionario
#representa una fila del archivo, se utilizan los nombres de la columnas
#como claves del diccionario
def leer_archivo(nombre_archivo:str)->list:
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

#===============================================================
#GRAFICO-1 FUNCIONES

#contador: dict
#contar_columna : list[dict] Str -> dict[str, int]
#dada una lista con los datos y el nombre de una columna
#devuelve un diccionario donde cada clave es la columna dada
#y su valor es la cantidad de veces que aparecio
def contar_columna(lista: list, columna:str):
    contador = {}

    for linea in lista:
        valor = linea[columna]

        if valor in contador:
            contador[valor] += 1
        else:
            contador[valor] = 1
    
    return contador



#porcentajes: dict[str, float]
#total: int
#porcentaje: float
#calcular_porcentajes_ship_mode: dict[str, int] -> list[float]
#dado un diccionario que contiene la columna como clave y la cantidad de veces que aparece como valor, devuelve un diccionario
#donde las claves son la columna y los valores son los porcentajes de utilizacion
def calcular_porcentajes_columna(contador):
    porcentajes = {}
    total = 0
    for cantidad in contador.values():
        total += cantidad

    for metodo in contador:
        porcentaje = contador[metodo] * 100 / total
        porcentajes[metodo] = porcentaje
    
    return porcentajes
        
#contador: dict[str, int]
#porcentajes: dict[str, float]
#mostrar_grafico_ship_mode: list[dict] -> None
#dada una lista con los registros, calcula la cantidad y el porcentaje de utilizacion
#de cada metodo de envio y muestre un grafico circular usando Matplotlib
def mostrar_grafico_ship_mode(registros):

    contador = contar_columna(registros,"Ship Mode")
    porcentajes = calcular_porcentajes_columna(contador)

    labels = porcentajes.keys()
    sizes = porcentajes.values()
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'size': 'smaller'}, radius=0.75)
    ax.set_title("¿Cuál es el porcentaje de utilizacion de cada envio?")
    st.pyplot(fig)


#===============================================================
#GRAFICO-2 FUNCIONES

def convertir_diccionario_a_lista_values(diccionario):
    lista = []
    for clave in diccionario:
        lista.append(diccionario[clave])
    
    return lista

def convertir_diccionario_a_lista_keys(diccionario):
    lista = []
    for clave in diccionario.keys():
        lista.append(clave)
    
    return lista


def mostrar_grafico_categorias(registros):

    contador = contar_columna(registros,"Category")
    porcentajes = calcular_porcentajes_columna(contador)
    
    
    contador = convertir_diccionario_a_lista_keys(contador)
    porcentajes = convertir_diccionario_a_lista_values(porcentajes)

    recipe = contador
    data = porcentajes
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
 
    wedges, texts, autotexts = ax.pie(data, autopct='%1.1f%%',pctdistance=0.75, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),horizontalalignment=horizontalalignment, **kw)
    plt.setp(autotexts, size=8, weight="bold",)
    ax.set_title("¿Cuáles son las categorias que vendieron mas unidades?")
    st.pyplot(fig)
    plt.show()

#===============================================================
#GRAFICO-3 FUNCIONES

#sumar_por_categoria : List[Dict] Str Str -> Dict[Str, float]
#la funcion toma una lista de de diccionario de los registros, una columna que se usara como categoria
#y otra columna numerica donde sus valores se sumaran
#devuelve un diccionario donde cada clave es un valor de la categoria(sin repetir)
#y cada valor es es la suma acumulada de la columna numerica dada
def sumar_por_categoria(registros, columna_categoria, columna_valor):
    acumulador = {}

    for registro in registros:
        categoria = registro[columna_categoria]
        valor = float(registro[columna_valor])

        if categoria in acumulador:
            acumulador[categoria] += valor
        else:
            acumulador[categoria] = valor

    return acumulador


#mostrar_grafico_barras : List[Dict] -> None
#toma una lista de diccionario del dataset
#calcula la suma de las ganancias para cada tipo de cliente
#crea un grafico de barras donde cada barra representa un tipo de cliente
#y su altura corresponde a las ganancias generadas
#muestra el grafico utilizando matplotlib
def mostrar_grafico_barras(registros):

    ganancias = sumar_por_categoria(registros, "Segment", "Profit")
    
    fig, ax = plt.subplots()

    fruits = ganancias.keys()
    counts = ganancias.values()
    bar_labels = ['red', 'blue', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Ganancias')
    ax.set_title('Tipo de clientes con mas ventas')

    plt.show()
    st.pyplot(fig)


#==============================================================
# GRAFICO-4 FUNCIONES

#filtrar_sub_categorias : List[Dict] -> List[Str]
#toma la lista de diccionarios con los datos del dataset filtrados con el descuento
#crea y devuelve una lista con los nombres de las subcategorias sin repetir
def filtrar_sub_categorias(registros_filtrados):
    sub_categorias = []

    for registro in registros_filtrados:
        if registro["Sub-Category"] not in sub_categorias:
            sub_categorias.append(registro["Sub-Category"])
    
    return sub_categorias

#filtrar_cantidad_de_ventas : List[Dict] -> Dict[Str, Int]
#toma una lista con los registros filtrados
#devuelve un diccionario con cuya clave es una subcategoria
#y el valor es la suma de las cantidades de vendidas de esa subcategoria
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


#maximo_descuento_sub_categoria : List[Dict] -> Dict[str, float]
#toma una lista de registros filtrados
#devuelve un diccionario cuya clave es la subctegoria
#y el valor es el descuento maximo aplicado a esa categoria
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


#sumar_por_subcategoria : List[Dict] str -> Dict[str, float]
#toma una lista de registros filtrados y el nombre de una de las columnas
#devuelve un diccionario cuya clave es una subcategoria
#y el valor es la suma de los valores de esa columna para dicha categoria
def sumar_por_subcategoria(registros_filtrados, columna):
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
def slider():
    rango = range(0,100)
    porcentaje_slider = st.select_slider("descuento aplicado", options=rango)
    return porcentaje_slider


#mostrar_tabla_slider : List[Dict] -> None
#toma una lista de registros del dataset
#obtiene el porcentaje seleccionado por el usuario
#filtra los registros segun dicho porcentaje
#calcula la informacion de cada subcategoria
#muestra una tabla con los descuentos maximos, cantidades vendidas, ventas y ganancias
#para crear la tabla se utiliza streamlit
def mostrar_tabla_slider(registros):
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


#==============================================================
# GRAFICO-6 FUNCIONES

#filtrar_categorias: List[Dict] -> List[str]
#toma una lista de registros
#devuelve una lista con todas las categorias dentro
def filtrar_categorias(registros):
    categorias = []

    for registro in registros:
        if registro["Category"] not in categorias:
            categorias.append(registro["Category"])
    
    return categorias

#entrada_mapa: List[Dict] -> ....
#toma una lista de registros 
#devuelve un menu desplegable y un mapa
def entrada_mapa(registros):
    categorias = filtrar_categorias(registros)
    option = st.selectbox(
        "Sobre que categoria desea conocer las perdidas/ganancias",
        categorias,
        index=None,
        placeholder="Seleccione una categoria",
    )

    st.write("Usted selecciono:", option)
    if option is not None:
        mapa(registros, option)

#filtrar_longitudes : List[Dict] Str -> List[float]
#toma una lista de registros y un string que hace referencia a una categoria seleccionada
#devuelve una lista con todas las longitudes que dada una categoria seleccionada contenga profit negativo
def filtrar_longitudes(registros,seleccion):
    lista_inicial = []

    for registro in registros:
        if seleccion == registro["Category"]:
            if float(registro["Profit"]) < 0:
                lista_inicial.append(float(registro["Longitude\n"]))
    return lista_inicial

#filtrar_latitudes : List[Dict] Str -> List[float]
#toma una lista de registros y un string que hace referencia a una categoria seleccionada
#devuelve una lista con todas las latitudes que dada una categoria seleccionada contenga profit negativo
def filtrar_latitudes(registros,seleccion):
    lista_inicial = []

    for registro in registros:
        if seleccion == registro["Category"]:
            if float(registro["Profit"]) < 0:
                lista_inicial.append(float(registro["Latitude"]))
    return lista_inicial

#mapa : List[Dict] Str-> None
#toma una lista de registros y un string que hace referencia a una categoria seleccionada
#devuelve un mapa
def mapa(registros,seleccion):
    latitudes = filtrar_latitudes(registros,seleccion)
    longitudes = filtrar_longitudes(registros,seleccion)
    
    dic_aux = {"lat": latitudes,"lon": longitudes}

    st.map(dic_aux)


def main():
    registros = leer_archivo("SampleSuperstore_geo.csv")

    st.set_page_config(layout="wide")

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            mostrar_grafico_ship_mode(registros)

    with col2:
        with st.container(border=True):
            st.title("¿Qué sub-categorías de productos fueron vendidos con un descuento superior al porcentaje seleccionado?")
            mostrar_tabla_slider(registros)
    

    col3, col4 = st.columns(2)
    with col3:
        with st.container(border=True):
            mostrar_grafico_categorias(registros)

    with col4:
        with st.container(border=True):
            mostrar_grafico_barras(registros)

    with st.container(border=True):
        entrada_mapa(registros)

    
if __name__ == "__main__":
    main()
