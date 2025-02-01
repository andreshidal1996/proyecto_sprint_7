import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado de la aplicación
st.header('Proyecto Sprint 7 - Herramientas de Desarrollo Web')

# Cargar los datos
car_data = pd.read_csv('./vehicles_us.csv') # leer los datos

# Usar casillas de verificación en lugar de botones
st.subheader("Selecciona el tipo de gráfico que deseas visualizar")

build_histogram = st.checkbox('Mostrar histograma')
build_scatter = st.checkbox('Mostrar gráfico de dispersión')

if build_histogram:
    st.write('Construyendo un histograma para la columna odómetro')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.write('Construyendo un gráfico de dispersión entre odómetro y precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="type")
    st.plotly_chart(fig_scatter, use_container_width=True)
