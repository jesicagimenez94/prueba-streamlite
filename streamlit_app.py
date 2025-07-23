import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import random

# -------------------- CONFIGURACIÓN DE PÁGINA --------------------
st.set_page_config(
    page_title="ElectroHouse Dashboard",
    page_icon="⚡",
    layout="wide"
)

# -------------------- ESTILOS PERSONALIZADOS --------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&family=Playfair+Display:wght@600&display=swap');

    html, body, [class*="css"]  {
        background-color: hsl(36, 33%, 97%);
        color: hsl(240, 10%, 3.9%);
        font-family: 'Montserrat', sans-serif;
    }

    h1, h2, h3, h4, h5 {
        font-family: 'Playfair Display', serif;
        letter-spacing: 0.01em;
        text-shadow: 1px 1px 0px rgba(0,0,0,0.05);
    }

    ::-webkit-scrollbar {
        width: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: #ba68c8;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- DATOS FICTICIOS --------------------
np.random.seed(42)
regiones = ['Centro', 'Norte', 'Sur', 'Cuyo', 'NEA', 'NOA', 'Patagonia']
canales = ['Online', 'Retail', 'Mayorista']
categorias = ['Electrodomésticos', 'Tecnología', 'Herramientas', 'Iluminación', 'Climatización']
fechas = pd.date_range(start='2024-01-01', periods=100)

df = pd.DataFrame({
    'Fecha': random.choices(fechas, k=100),
    'ID_Venta': [f"V{1000+i}" for i in range(100)],
    'Cliente': [f"Cliente_{i}" for i in range(100)],
    'Región': np.random.choice(regiones, 100),
    'Producto': [f"Producto_{i%10}" for i in range(100)],
    'Categoría': np.random.choice(categorias, 100),
    'Cantidad': np.random.randint(1, 10, 100),
    'Precio_Unitario': np.random.randint(5000, 30000, 100),
    'Canal_Venta': np.random.choice(canales, 100)
})

df['Ingreso'] = df['Cantidad'] * df['Precio_Unitario']
df['Costo_Unitario'] = df['Precio_Unitario'] * np.random.uniform(0.5, 0.8, 100)
df['Margen_Bruto'] = df['Ingreso'] - (df['Costo_Unitario'] * df['Cantidad'])
df['Mes'] = df['Fecha'].dt.strftime('%b')

# -------------------- SIDEBAR PERSONALIZADO OSCURO --------------------
with st.sidebar:
    st.markdown("""
    <div style="
        background: #1e1e2f;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        color: #f0f0f0;
        font-family: 'Montserrat', sans-serif;
    ">
        <h2 style="
            font-family: 'Playfair Display', serif;
            font-size: 1.6rem;
            text-align: center;
            color: #ba68c8;
            margin-bottom: 1rem;
        ">Jesica Gimenez</h2>

        <div style="text-align:center; margin-bottom: 1rem;">
            <a href='https://portfolio-jesica-gimenez.vercel.app/' target='_blank' style="
                background: linear-gradient(to right, #9c27b0, #ba68c8, #f48fb1);
                color: white;
                padding: 0.4rem 0.8rem;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 600;
                margin: 0.2rem;
                display: inline-block;
            ">🌐 Portfolio</a><br>
            <a href='https://www.linkedin.com/in/jesica-gimenez/' target='_blank' style="
                background: linear-gradient(to right, #7b1fa2, #9c27b0, #ec407a);
                color: white;
                padding: 0.4rem 0.8rem;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 600;
                margin: 0.2rem;
                display: inline-block;
            ">💼 LinkedIn</a>
        </div>

        <p style="font-size: 13.5px; line-height: 1.5; text-align: justify;">
            Dashboard de análisis de ventas con filtros por región, canal y categoría.<br>
            Visualizado con Altair e inspirado en estética Tailwind y branding personal.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------- FILTROS --------------------
st.markdown("### 🎯 Filtros")
col1, col2 = st.columns(2)
region = col1.selectbox("Seleccioná una región", ["Todas"] + sorted(df["Región"].unique()))
canal = col2.selectbox("Seleccioná un canal de venta", ["Todos"] + sorted(df["Canal_Venta"].unique()))

df_filtrado = df.copy()
if region != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Región"] == region]
if canal != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Canal_Venta"] == canal]

# -------------------- MÉTRICAS CLAVE --------------------
st.markdown("### 📊 Métricas Clave")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Ingresos", f"${df_filtrado['Ingreso'].sum():,.0f}")
kpi2.metric("Ventas Totales", df_filtrado["ID_Venta"].nunique())
kpi3.metric("Margen Bruto", f"${df_filtrado['Margen_Bruto'].sum():,.0f}")

# -------------------- VISUALIZACIONES --------------------
st.markdown("### 📈 Visualizaciones")

col1, col2 = st.columns(2)

# Ingreso por categoría
chart1 = df_filtrado.groupby("Categoría")["Ingreso"].sum().reset_index()
bar1 = alt.Chart(chart1).mark_bar().encode(
    y=alt.Y("Categoría:N", sort='-x'),
    x=alt.X("Ingreso:Q", title="Ingreso Total"),
    color=alt.Color("Categoría:N", legend=None)
).properties(height=300)
col1.altair_chart(bar1, use_container_width=True)

# Ingreso por mes
chart2 = df_filtrado.groupby("Mes")["Ingreso"].sum().reindex(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
).reset_index().dropna()
chart2.columns = ["Mes", "Ingreso"]
bar2 = alt.Chart(chart2).mark_line(point=True).encode(
    x="Mes",
    y="Ingreso"
).properties(height=300)
col2.altair_chart(bar2, use_container_width=True)

col3, col4 = st.columns(2)

# Top 5 productos
top_prod = df_filtrado.groupby("Producto")["Cantidad"].sum().reset_index().sort_values("Cantidad", ascending=False).head(5)
chart3 = alt.Chart(top_prod).mark_bar().encode(
    x="Producto",
    y="Cantidad",
    color=alt.Color("Producto", legend=None)
).properties(height=300)
col3.altair_chart(chart3, use_container_width=True)

# Donut chart (categorías)
pie_data = df_filtrado.groupby("Categoría")["Ingreso"].sum().reset_index()
pie = alt.Chart(pie_data).mark_arc(innerRadius=50).encode(
    theta="Ingreso",
    color="Categoría"
).properties(height=300)
col4.altair_chart(pie, use_container_width=True)

# -------------------- TABLA Y EXPORT --------------------
st.markdown("### 🧾 Vista de Datos")
st.dataframe(df_filtrado, use_container_width=True)

st.download_button(
    label="📥 Descargar CSV de datos filtrados",
    data=df_filtrado.to_csv(index=False),
    file_name="ventas_filtradas.csv",
    mime="text/csv"
)
