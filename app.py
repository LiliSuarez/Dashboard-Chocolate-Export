import streamlit as st
import csv
import requests
from io import StringIO

# Función para cargar CSV desde GitHub sin usar pandas
def cargar_csv_desde_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        return list(csv.DictReader(StringIO(content)))
    else:
        st.error(f"No se pudo cargar el archivo desde: {url}")
        return []

# URLs de los archivos CSV
clientes_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-ChocolateExport/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-ChocolateExport/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-ChocolateExport/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-ChocolateExport/main/barreras.csv"

# Cargar datos
clientes = cargar_csv_desde_url(clientes_url)
mercados = cargar_csv_desde_url(mercados_url)
exportaciones = cargar_csv_desde_url(exportaciones_url)
barreras = cargar_csv_desde_url(barreras_url)

# Título del dashboard
st.title("Dashboard Interactivo de Exportaciones de Chocolates")

# Selección de país
paises = list(set([row["País"] for row in exportaciones]))
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", sorted(paises))

# Mostrar datos de clientes
st.subheader("Clientes")
clientes_filtrados = [c for c in clientes if c["País"] == pais_seleccionado]
st.write(clientes_filtrados)

# Mostrar datos de exportaciones
st.subheader("Exportaciones de Chocolates")
exportaciones_filtradas = [e for e in exportaciones if e["País"] == pais_seleccionado]
st.write(exportaciones_filtradas)

# Mostrar datos de mercados
st.subheader("Segmentos de Mercado")
mercados_filtrados = [m for m in mercados if m["País"] == pais_seleccionado]
st.write(mercados_filtrados)

# Mostrar barreras
st.subheader("Barreras de Entrada")
barreras_filtradas = [b for b in barreras if b["País"] == pais_seleccionado]
st.write(barreras_filtradas)

# Análisis comparativo
st.subheader("Análisis Comparativo de Tamaño de Mercado")
for m in mercados:
    st.markdown(f"• {m['País']}: {m['Tamaño del Mercado (USD millones)']} millones USD")

