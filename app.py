import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Dashboard-Chocolate-Export', layout='wide')

# Cargar los datos desde archivos CSV en GitHub
@st.cache_data
def load_data():
    base_url = 'https://raw.githubusercontent.com/LiliSuarez/Dashboard-Chocolate-Export-/main/'
    clientes_df = pd.read_csv(base_url + 'clientes.csv')
    mercados_df = pd.read_csv(base_url + 'mercados.csv')
    exportaciones_df = pd.read_csv(base_url + 'exportaciones.csv')
    barreras_df = pd.read_csv(base_url + 'barreras.csv')
    return clientes_df, mercados_df, exportaciones_df, barreras_df
clientes_df, mercados_df, exportaciones_df, barreras_df = load_data()

# Título del Dashboard
st.title("Dashboard Interactivo de Exportaciones de Chocolates")

# Filtro de país
paises = exportaciones_df["País"].unique()
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", paises)

# Mostrar datos de clientes
st.subheader("Clientes")
clientes_filtrados = clientes_df[clientes_df["País"] == pais_seleccionado]
st.dataframe(clientes_filtrados)

# Mostrar datos de exportaciones
st.subheader("Exportaciones de Chocolates")
exportaciones_filtradas = exportaciones_df[exportaciones_df["País"] == pais_seleccionado]
fig, ax = plt.subplots()
ax.bar(exportaciones_filtradas["País"], exportaciones_filtradas["Exportaciones (USD millones)"], color='#2E86C1')
ax.set_xlabel("País")
ax.set_ylabel("Exportaciones (USD millones)")
ax.set_title(f"Exportaciones de Chocolates en {pais_seleccionado}")
plt.xticks(rotation=45)
st.pyplot(fig)

# Mostrar datos de mercados
st.subheader("Segmentos de Mercado")
mercados_filtrados = mercados_df[mercados_df["País"] == pais_seleccionado]
st.dataframe(mercados_filtrados)

# Mostrar barreras de entrada
st.subheader("Barreras de Entrada")
barreras_filtradas = barreras_df[barreras_df["País"] == pais_seleccionado]
st.dataframe(barreras_filtradas)

# Análisis Comparativo
st.subheader("Análisis Comparativo")
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.bar(mercados_df["País"], mercados_df["Tamaño del Mercado (USD millones)"], color='#F39C12')
ax2.set_xlabel("País")
ax2.set_ylabel("Tamaño del Mercado (USD millones)")
ax2.set_title("Comparación de Tamaños de Mercado")
plt.xticks(rotation=45)
st.pyplot(fig2)
