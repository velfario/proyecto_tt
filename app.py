import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv') # leer los datos


# Titulo de la aplicación
st.header('Análisis de la base de datos vehicles_us.csv', divider='gray')


# crear el checkbox del histograma
hist_check = st.checkbox('Construir histograma')
if hist_check: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear el checkbox de dispersión
scat_check = st.checkbox('Graficar dispersión')
if scat_check: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
