import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from streamlit_option_menu import option_menu

# -------------------- CONFIGURACIÓN DE PÁGINA --------------------
st.set_page_config(
    page_title="Dashboard Streamlit",
    page_icon="📊",
    layout="wide"
)

# -------------------- ESTILOS CSS PERSONALIZADOS --------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #1e293b;
        color: white;
    }
    .css-1d391kg { background-color: #1e293b; }
    .big-font {
        font-size:36px !important;
        font-weight: bold;
    }
    .metric-label {
        color: #94a3b8;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR CON MENÚ --------------------
with st.sidebar:
    selected = option_menu(
        menu_title="Menú Principal",
        options=["Dashboard", "Análisis", "Configuración"],
        icons=["bar-chart-line", "pie-chart", "gear"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#1e1e2f"},
            "icon": {"color": "#ffffff", "font-size": "20px"},
            "nav-link": {
                "color": "#ffffff",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#4f46e5",
            },
            "nav-link-selected": {"background-color": "#4f46e5"},
        }
    )

# -------------------- MÉTRICAS PRINCIPALES --------------------
col1, col2, col3 = st.columns(3)

col1.metric("Visitas", "340,108", "+3.2%")
col2.metric("Conversiones", "25%", "+1.1%")
col3.metric("Nuevos Usuarios", "50+", "+2.5%")

# -------------------- GRÁFICO DE LÍNEA --------------------
df = pd.DataFrame({
    "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun"],
    "Visitas": [12000, 18000, 26000, 22000, 28000, 34000]
})

line_chart = go.Figure()
line_chart.add_trace(go.Scatter(x=df["Mes"], y=df["Visitas"], mode='lines+markers',
                                line=dict(color='#4f46e5', width=3)))
line_chart.update_layout(
    paper_bgcolor="#1e293b",
    plot_bgcolor="#1e293b",
    font=dict(color="white"),
    margin=dict(l=20, r=20, t=40, b=20),
    height=300,
    title="Visitas Mensuales"
)

# -------------------- GRÁFICOS DE DONA --------------------
donut1 = go.Figure(data=[go.Pie(
    labels=["Completado", "Pendiente"],
    values=[65, 35],
    hole=0.6,
    marker_colors=["#10b981", "#374151"]
)])
donut1.update_layout(
    showlegend=True,
    paper_bgcolor="#1e293b",
    font=dict(color="white"),
    height=300,
    margin=dict(t=40, b=10),
    title="Progreso General"
)

donut2 = go.Figure(data=[go.Pie(
    labels=["Desktop", "Mobile", "Tablet"],
    values=[55, 30, 15],
    hole=0.6,
    marker_colors=["#3b82f6", "#f97316", "#10b981"]
)])
donut2.update_layout(
    showlegend=True,
    paper_bgcolor="#1e293b",
    font=dict(color="white"),
    height=300,
    margin=dict(t=40, b=10),
    title="Tráfico por Dispositivo"
)

# -------------------- DISTRIBUIR GRÁFICOS EN COLUMNAS --------------------
col4, col5, col6 = st.columns(3)
with col4:
    st.plotly_chart(line_chart, use_container_width=True)
with col5:
    st.plotly_chart(donut1, use_container_width=True)
with col6:
    st.plotly_chart(donut2, use_container_width=True)

