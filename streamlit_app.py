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
        padding: 1rem 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.markdown("""
        <div style="text-align:center; margin-bottom:20px;">
            <img src="https://api.dicebear.com/7.x/adventurer/svg" width="100" style="border-radius:50%;">
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
st.markdown("### 340,108 Unique Visitors")
st.markdown("Última actualización: **24 Jul 2025** — Métricas globales del tráfico del sitio y conversión")

# -------------------- DATOS BASE --------------------
df_line = pd.DataFrame({
    "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul"],
    "Visitas": [12000, 18500, 20000, 25000, 28000, 31000, 34000]
})

df_region = pd.DataFrame({
    "Región": ["Norte", "Centro", "Sur", "Oeste", "Este"],
    "Usuarios": [12000, 18000, 9000, 15000, 13000]
})

# -------------------- KPIs --------------------
def build_kpi(value, title, color):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title, 'font': {'color': 'white'}},
        gauge={
            'axis': {'range': [0, 100], 'tickcolor': "white"},
            'bar': {'color': color},
            'bgcolor': "#334155",
            'borderwidth': 2,
            'bordercolor': "gray"},
    ))
    fig.update_layout(paper_bgcolor="#1e293b", height=230, font_color="white", margin=dict(t=10, b=0))
    return fig

fig1 = build_kpi(25, "Conversion Rate", "#4f46e5")
fig2 = build_kpi(50, "New Users", "#10b981")
fig3 = build_kpi(9, "Bounce Rate", "#facc15")

# -------------------- GRÁFICO LÍNEA --------------------
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(
    x=df_line["Mes"], y=df_line["Visitas"],
    mode='lines+markers',
    line=dict(color="#4f46e5", width=3)
))
fig_line.update_layout(
    title="Visitas Mensuales",
    paper_bgcolor="#1e293b",
    plot_bgcolor="#1e293b",
    font_color="white",
    height=230,
    margin=dict(t=40, b=10, l=10, r=10)
)

# -------------------- GRÁFICO BARRAS --------------------
fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(
    x=df_region["Región"],
    y=df_region["Usuarios"],
    marker_color="#0ea5e9"
))
fig_bar.update_layout(
    title="Usuarios por Región",
    paper_bgcolor="#1e293b",
    plot_bgcolor="#1e293b",
    font_color="white",
    height=230,
    margin=dict(t=40, b=10, l=10, r=10)
)

# -------------------- GRÁFICO DONA --------------------
fig_donut = go.Figure(data=[go.Pie(
    labels=["Completado", "Pendiente"],
    values=[65, 35],
    hole=0.6,
    marker_colors=["#10b981", "#374151"]
)])
fig_donut.update_layout(
    title="Progreso de Conversión",
    showlegend=False,
    paper_bgcolor="#1e293b",
    font_color="white",
    height=230,
    margin=dict(t=40, b=10, l=10, r=10)
)

# -------------------- RENDER 6 GRÁFICOS (2 filas x 3 columnas) --------------------
col1, col2, col3 = st.columns(3)
with col1: st.plotly_chart(fig1, use_container_width=True)
with col2: st.plotly_chart(fig2, use_container_width=True)
with col3: st.plotly_chart(fig3, use_container_width=True)

col4, col5, col6 = st.columns(3)
with col4: st.plotly_chart(fig_line, use_container_width=True)
with col5: st.plotly_chart(fig_bar, use_container_width=True)
with col6: st.plotly_chart(fig_donut, use_container_width=True)
