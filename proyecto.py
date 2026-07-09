import streamlit as st

from grafico1 import mostrar_grafico_ship_mode
from grafico2 import mostrar_grafico_category
from grafico3 import mostrar_grafico_barras
from grafico4 import mostrar_tabla_slider
from grafico5 import entrada_region_estado
from grafico6 import entrada_mapa
from auxiliares import leer_archivo



def main():
    registros = leer_archivo("SampleSuperstore_geo.csv")

    st.set_page_config(layout="wide")

    st.title("Proyecto programacion :sunglasses:",text_alignment="center")
    st.header("Grupo 10 ",text_alignment="center")
    st.subheader("Temario: SuperStore",text_alignment="center")
    st.subheader("Integrantes: Riboldi Juan Cruz - Costa Alejo - Malamud Tomas", text_alignment="center")

    with st.container(border=True):
        entrada_region_estado(registros)

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
            mostrar_grafico_category(registros)

    with col4:
        with st.container(border=True):
            mostrar_grafico_barras(registros)

    with st.container(border=True):
        entrada_mapa(registros)

    
if __name__ == "__main__":
    main()
