import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('ANÁLISIS ESTADÍSTICO-GRÁFICO DE VEHÍCULOS EN EL MERCADO')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir un diagrama de dispersión')
if disp_button:
    st.write('Construir un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

build_lineplot = st.checkbox('Construir un diagrama de líneas')
if build_lineplot:
    st.write('Construir un diagram de líneas para el conjunto de datos de anuncios de venta de coches')
    fig = px.line(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
    