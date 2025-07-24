# Prompt como Ingeniero de Prompts:
# Crea un dashboard en Streamlit con los siguientes requisitos:
# - Sidebar oscuro con imagen centrada, nombre y puesto (imagen anime avatar femenina).
# - Menú funcional con botones para 'Inicio', 'Dashboard', 'Configuración'.
# - Todo el contenido debe ajustarse a una sola pantalla sin scroll vertical.
# - Gráficos representativos, responsivos y ordenados horizontalmente.
# - El título debe ser visible, centrado y sin cortarse.
# - Estilo visual profesional, oscuro, tipografía moderna.

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu

# Configuración de página
st.set_page_config(
    page_title="Dashboard Profesional",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)

# CSS personalizado para centrar y dar estilo
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
        background-color: #121212;
        color: #e0e0e0;
        margin: 0; padding: 0;
        overflow-x: hidden;
    }
    [data-testid="stSidebar"] {
        background-color: #1e1e2f;
        padding-top: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .sidebar-content {
        text-align: center;
    }
    .sidebar-name {
        font-weight: 700;
        font-size: 1.25rem;
        margin-top: 0.5rem;
        color: #bb86fc;
    }
    .sidebar-role {
        font-size: 0.9rem;
        color: #a0a0a0;
        margin-bottom: 1rem;
    }
    .nav-link {
        font-size: 16px !important;
        text-align: center !important;
        margin: 5px 0 !important;
    }
    .nav-link-selected {
        background-color: #bb86fc !important;
        color: #121212 !important;
        font-weight: 700 !important;
    }
    .main-container {
        padding: 1rem 2rem;
    }
    .titulo-principal {
        font-size: 2rem;
        color: #bb86fc;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.image("imagen1.png", width=110)
    st.markdown('<div class="sidebar-name">Ana Luna</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-role">Analista de Datos</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Dashboard", "Configuración"],
        icons=["house", "bar-chart-line", "gear"],
        default_index=1,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#1e1e2f", "width": "100%"},
            "icon": {"color": "#8e8e8e", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "center", "--hover-color": "#6200ea"},
            "nav-link-selected": {"background-color": "#bb86fc", "color": "#121212"},
        }
    )

# Contenido principal
st.markdown("<h1 class='titulo-principal'>Dashboard de Ventas - ElectroHouse</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Ventas Totales", "$1.250.000")
with col2:
    st.metric("Unidades Vendidas", "5.432")
with col3:
    st.metric("Clientes Activos", "210")

col4, col5 = st.columns(2)

data = pd.DataFrame({
    "Producto": ["TV", "Heladera", "Lavarropas", "Aire"],
    "Ventas": [320, 210, 150, 180]
})

with col4:
    fig1 = px.bar(data, x="Producto", y="Ventas", title="Ventas por Producto", color_discrete_sequence=["#bb86fc"])
    fig1.update_layout(paper_bgcolor="#121212", plot_bgcolor="#121212", font_color="#e0e0e0")
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    fig2 = px.pie(data, values="Ventas", names="Producto", title="Participación de Ventas")
    fig2.update_layout(paper_bgcolor="#121212", font_color="#e0e0e0")
    st.plotly_chart(fig2, use_container_width=True)

# Elimina el espacio en blanco para evitar scroll vertical
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

