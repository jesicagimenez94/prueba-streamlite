import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# -------------------- CONFIGURACIÓN DE PÁGINA --------------------
st.set_page_config(page_title="Dashboard", layout="wide", page_icon="📊")

# -------------------- ESTILO GLOBAL --------------------
st.markdown("""
    <style>
    body, .stApp {
        background-color: #1e293b;
        color: white;
        font-family: 'Montserrat', sans-serif;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .metric-style {
        text-align: center;
        padding: 1rem;
        border-radius: 12px;
        background-color: #334155;
        box-shadow: 0 0 15px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.markdown("""
        <div style="text-align:center; margin-bottom:20px;">
            <img src="https://randomuser.me/api/portraits/men/75.jpg" width="100" style="border-radius:50%;">
            <h3 style="margin-top:10px;">James Gibson</h3>
            <p style="color:gray;">Data Analyst</p>
        </div>
    """, unsafe_allow_html=True)

    selected = option_menu(
        menu_title="Menú",
        options=["Inicio", "Dashboard", "Configuración"],
        icons=["house", "bar-chart", "gear"],
        default_index=1,
        styles={
            "container": {"background-color": "#1e1e2f"},
            "icon": {"color": "#f0f0f0", "font-size": "18px"},
            "nav-link": {"color": "#f0f0f0", "margin": "10px"},
            "nav-link-selected": {"background-color": "#4f46e5"},
        }
    )

# -------------------- ENCABEZADO --------------------
st.markdown("## 340,108 Unique Visitors")
st.markdown("Última actualización: **24 Jul 2025** — Métricas globales del tráfico del sitio y conversión")

# -------------------- KPIs --------------------
col1, col2, col3 = st.columns(3)

with col1:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=25,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Conversion Rate", 'font': {'color': 'white'}},
        gauge={'axis': {'range': [0, 100], 'tickcolor': "white"},
               'bar': {'color': "#4f46e5"},
               'bgcolor': "#334155",
               'borderwidth': 2,
               'bordercolor': "gray"},
    ))
    fig.update_layout(paper_bgcolor="#1e293b", height=250, font_color="white")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=50,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "New Users", 'font': {'color': 'white'}},
        gauge={'axis': {'range': [0, 100], 'tickcolor': "white"},
               'bar': {'color': "#10b981"},
               'bgcolor': "#334155",
               'borderwidth': 2,
               'bordercolor': "gray"},
    ))
    fig.update_layout(paper_bgcolor="#1e293b", height=250, font_color="white")
    st.plotly_chart(fig, use_container_width=True)

with col3:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=9,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Bounce Rate", 'font': {'color': 'white'}},
        gauge={'axis': {'range': [0, 100], 'tickcolor': "white"},
               'bar': {'color': "#facc15"},
               'bgcolor': "#334155",
               'borderwidth': 2,
               'bordercolor': "gray"},
    ))
    fig.update_layout(paper_bgcolor="#1e293b", height=250, font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# -------------------- VISITAS MENSUALES --------------------
df = pd.DataFrame({
    "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul"],
    "Visitas": [12000, 18500, 20000, 25000, 28000, 31000, 34000]
})

fig_line = go.Figure()
fig_line.add_trace(go.Scatter(
    x=df["Mes"], y=df["Visitas"],
    mode='lines+markers',
    line=dict(color="#4f46e5", width=3)
))
fig_line.update_layout(
    title="Visitas Mensuales",
    paper_bgcolor="#1e293b",
    plot_bgcolor="#1e293b",
    font_color="white",
    height=300,
    margin=dict(t=40, b=10, l=10, r=10)
)

# -------------------- GRÁFICO DE DONA --------------------
fig_donut = go.Figure(data=[go.Pie(
    labels=["Completado", "Pendiente"],
    values=[65, 35],
    hole=0.6,
    marker_colors=["#10b981", "#374151"]
)])
fig_donut.update_layout(
    title="Progreso de Conversión",
    showlegend=True,
    paper_bgcolor="#1e293b",
    font_color="white",
    height=300,
    margin=dict(t=40, b=10, l=10, r=10)
)

# -------------------- MOSTRAR AMBOS EN PANTALLA --------------------
col4, col5 = st.columns([2, 1])
with col4:
    st.plotly_chart(fig_line, use_container_width=True)
with col5:
    st.plotly_chart(fig_donut, use_container_width=True)
