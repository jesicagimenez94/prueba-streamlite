import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from datetime import datetime

# Configuración de página
st.set_page_config(
    page_title="Dashboard Profesional",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)

# Estilos CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
        background-color: #121212;
        color: #e0e0e0;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }
    [data-testid="stSidebar"] {
        background-color: #1e1e2f;
        border-radius: 12px;
        padding-top: 1rem;
        padding-bottom: 1rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .sidebar-content {
        text-align: center;
        width: 100%;
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
    .option-menu {
        width: 100% !important;
    }
    .main-container {
        background-color: #1e1e2f;
        border-radius: 16px;
        padding: 1rem 1.5rem 1.5rem 1.5rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.6);
    }
    .header-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #bb86fc;
        margin-bottom: 0;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .header-subtitle {
        font-size: 1rem;
        color: #a0a0a0;
        margin-top: 0;
        margin-bottom: 1rem;
    }
    .kpi-box {
        background-color: #29294a;
        border-radius: 14px;
        padding: 0.8rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.image("imagen1.png", width=110)
    st.markdown('<div class="sidebar-name">Ana Luna</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-role">Analista de Datos</div>', unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Dashboard", "Configuración"],
        icons=["house", "bar-chart-line", "gear"],
        menu_icon="cast",
        default_index=1,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#1e1e2f", "width":"100%"},
            "icon": {"color": "#8e8e8e", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "center", "margin":"5px 0", "--hover-color": "#6200ea"},
            "nav-link-selected": {"background-color": "#bb86fc", "color": "#121212"},
        }
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Datos simulados
np.random.seed(42)
dates = pd.date_range(end=datetime.today(), periods=30)
visits = np.random.poisson(lam=11000, size=30) + np.linspace(0, 5000, 30).astype(int)
conversion_labels = ['Orgánico', 'Pago', 'Referido', 'Directo']
conversion_values = [45, 25, 15, 15]
categories = ['Tecnología', 'Moda', 'Hogar', 'Libros', 'Deportes']
cat_values = [2100, 1800, 1600, 1400, 1200]
heatmap_data = np.random.randint(0, 100, size=(7, 24))
days = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
hours = [f"{h}:00" for h in range(24)]
kpi_values = [78, 54, 92]
kpi_labels = ["Satisfacción", "Retención", "Crecimiento"]

def circular_progress(value, label, color):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': label},
        gauge={
            'axis': {'range': [0, 100], 'visible': False},
            'bar': {'color': color},
            'bgcolor': "#3a3a65"
        }
    ))
    fig.update_layout(margin=dict(t=0, b=0), height=160, paper_bgcolor="#29294a")
    return fig

def line_chart(dates, values):
    fig = go.Figure(go.Scatter(x=dates, y=values, mode='lines', line=dict(color='#bb86fc')))
    fig.update_layout(height=250, paper_bgcolor="#29294a", margin=dict(t=25, b=25))
    return fig

def donut_chart(labels, values):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
    fig.update_layout(height=250, paper_bgcolor="#29294a", showlegend=False, margin=dict(t=25, b=25))
    return fig

def horizontal_bar(categories, values):
    fig = go.Figure(go.Bar(x=values, y=categories, orientation='h', marker_color='#bb86fc'))
    fig.update_layout(height=250, paper_bgcolor="#29294a", margin=dict(t=25, b=25))
    return fig

def heatmap(data, x_labels, y_labels):
    fig = go.Figure(go.Heatmap(z=data, x=x_labels, y=y_labels, colorscale='Viridis'))
    fig.update_layout(height=250, paper_bgcolor="#29294a", margin=dict(t=25, b=25))
    return fig

def radar_chart(labels, values):
    fig = go.Figure(go.Scatterpolar(r=values, theta=labels, fill='toself', line_color='#bb86fc'))
    fig.update_layout(height=250, paper_bgcolor="#29294a", margin=dict(t=25, b=25))
    return fig

def show_inicio():
    st.markdown("""
        <div class="main-container">
        <h1 class="header-title">Bienvenido a tu dashboard</h1>
        <p class="header-subtitle">Esta es la aplicación para visualizar datos claves en tiempo real.</p>
        </div>
    """, unsafe_allow_html=True)

def show_dashboard():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<h1 class="header-title">340.108 Visitantes Únicos</h1>', unsafe_allow_html=True)
        st.markdown(f'<p class="header-subtitle">{datetime.today().strftime("%d de %B de %Y")} - Tráfico y conversión</p>', unsafe_allow_html=True)

    kpi_cols = st.columns(3)
    colors = ['#bb86fc', '#6200ea', '#03dac6']
    for i, col in enumerate(kpi_cols):
        with col:
            st.markdown('<div class="kpi-box">', unsafe_allow_html=True)
            st.plotly_chart(circular_progress(kpi_values[i], kpi_labels[i], colors[i]), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    graph_cols = st.columns(3)
    with graph_cols[0]:
        st.markdown('<h4 style="color:#bb86fc;">Visitas</h4>', unsafe_allow_html=True)
        st.plotly_chart(line_chart(dates, visits), use_container_width=True)
    with graph_cols[1]:
        st.markdown('<h4 style="color:#bb86fc;">Tráfico</h4>', unsafe_allow_html=True)
        st.plotly_chart(donut_chart(conversion_labels, conversion_values), use_container_width=True)
    with graph_cols[2]:
        st.markdown('<h4 style="color:#bb86fc;">Categorías</h4>', unsafe_allow_html=True)
        st.plotly_chart(horizontal_bar(categories, cat_values), use_container_width=True)

    st.write("---")
    last_cols = st.columns(2)
    with last_cols[0]:
        st.markdown('<h4 style="color:#bb86fc;">Actividad semanal</h4>', unsafe_allow_html=True)
        st.plotly_chart(heatmap(heatmap_data, hours, days), use_container_width=True)
    with last_cols[1]:
        st.markdown('<h4 style="color:#bb86fc;">Radar Indicadores</h4>', unsafe_allow_html=True)
        radar_labels = ["Calidad", "Velocidad", "Satisfacción", "Eficiencia", "Innovación"]
        radar_values = [70, 80, 85, 60, 90]
        st.plotly_chart(radar_chart(radar_labels, radar_values), use_container_width=True)

def show_configuracion():
    st.markdown("""
        <div class="main-container">
        <h1 class="header-title">Configuración</h1>
        <p class="header-subtitle">Ajustes y preferencias de la aplicación.</p>
        <ul>
            <li>Próximamente...</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

# Navegación
if selected == "Inicio":
    show_inicio()
elif selected == "Dashboard":
    show_dashboard()
else:
    show_configuracion()


