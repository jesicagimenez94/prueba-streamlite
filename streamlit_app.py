import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Dashboard Profesional",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)

# --- FUENTES Y ESTILOS CUSTOM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
        background-color: #121212;
        color: #e0e0e0;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1e1e2f;
        border-radius: 12px;
        padding: 1rem 0 1rem 0;
    }
    /* Sidebar avatar */
    .avatar-img {
        border-radius: 50%;
        border: 3px solid #6200ea;
        box-shadow: 0 0 10px #6200ea;
        width: 120px;
        height: 120px;
        margin: auto;
        display: block;
    }
    /* Sidebar text */
    .sidebar-name {
        text-align: center;
        font-weight: 700;
        font-size: 1.25rem;
        margin-top: 0.5rem;
        color: #bb86fc;
    }
    .sidebar-role {
        text-align: center;
        font-size: 0.9rem;
        color: #a0a0a0;
        margin-bottom: 1rem;
    }
    /* Botones menú */
    .nav-link {
        font-weight: 600;
        font-size: 1.05rem;
        color: #cfcfcf;
        padding: 0.4rem 1rem;
        border-radius: 10px;
        transition: background-color 0.3s ease;
        cursor: pointer;
    }
    .nav-link:hover {
        background-color: #6200ea;
        color: white;
    }
    /* Active nav */
    .nav-active {
        background-color: #bb86fc !important;
        color: #121212 !important;
        font-weight: 700 !important;
    }
    /* Contenedor principal */
    .main-container {
        background-color: #1e1e2f;
        border-radius: 16px;
        padding: 1rem 1.5rem 1.5rem 1.5rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.6);
        height: 100%;
    }
    /* Encabezado */
    .header-title {
        font-size: 2rem;
        font-weight: 700;
        color: #bb86fc;
        margin-bottom: 0;
    }
    .header-subtitle {
        font-size: 1rem;
        color: #a0a0a0;
        margin-top: 0;
        margin-bottom: 1rem;
    }
    /* KPI container */
    .kpi-box {
        background-color: #29294a;
        border-radius: 14px;
        padding: 1rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)


# --- SIDEBAR ---
with st.sidebar:
    # Avatar anime mujer (ficticia)
    st.markdown('<img class="avatar-img" src="https://i.pinimg.com/originals/3e/52/86/3e52860ebc5dffb8a4f91e272fbb7b43.png" alt="Avatar" />', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-name">Ana Luna</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-role">Data Analyst</div>', unsafe_allow_html=True)

    # Menú interactivo con streamlit-option-menu
    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Dashboard", "Configuración"],
        icons=["house", "bar-chart-line", "gear"],
        menu_icon="cast",
        default_index=1,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#1e1e2f"},
            "icon": {"color": "#8e8e8e", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#6200ea"},
            "nav-link-selected": {"background-color": "#bb86fc", "color": "#121212"},
        }
    )


# --- DATOS FICTICIOS ---

# Fechas para gráfico líneas
np.random.seed(42)
dates = pd.date_range(end=datetime.today(), periods=30)
visits = np.random.poisson(lam=11000, size=30) + np.linspace(0, 5000, 30).astype(int)

# Datos para gráfica de dona
conversion_labels = ['Organic', 'Paid', 'Referral', 'Direct']
conversion_values = [45, 25, 15, 15]

# Datos barras horizontales
categories = ['Tech', 'Fashion', 'Home', 'Books', 'Sports']
cat_values = [2100, 1800, 1600, 1400, 1200]

# Datos heatmap (7 días, 24 hrs)
heatmap_data = np.random.randint(0, 100, size=(7, 24))
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
hours = [f"{h}:00" for h in range(24)]

# KPIs valores (0-100%)
kpi_values = [78, 54, 92]
kpi_labels = ["Satisfacción", "Retención", "Crecimiento"]


# --- FUNCIONES PARA GRAFICOS ---

def circular_progress(value, label, color):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': label, 'font': {'size': 18}},
        gauge={
            'axis': {'range': [0, 100], 'visible': False},
            'bar': {'color': color},
            'bgcolor': "#3a3a65",
            'borderwidth': 0,
            'threshold': {
                'line': {'color': "white", 'width': 2},
                'thickness': 0.75,
                'value': value}
        }
    ))
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        height=170,
        paper_bgcolor="#29294a",
        font=dict(color="white", family="Montserrat")
    )
    return fig

def line_chart(dates, values):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates, y=values,
        mode='lines+markers',
        line=dict(color='#bb86fc', width=3),
        marker=dict(size=6)
    ))
    fig.update_layout(
        margin=dict(l=10, r=10, t=30, b=20),
        paper_bgcolor="#29294a",
        plot_bgcolor="#1e1e2f",
        font=dict(color="white", family="Montserrat"),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        height=280
    )
    return fig

def donut_chart(labels, values):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.55, marker_colors=['#bb86fc','#6200ea','#3700b3','#03dac6'])])
    fig.update_traces(textinfo='percent+label', textfont_size=14, marker=dict(line=dict(color='#121212', width=2)))
    fig.update_layout(
        margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor="#29294a",
        font=dict(color="white", family="Montserrat"),
        height=280,
        showlegend=False,
    )
    return fig

def horizontal_bar(categories, values):
    fig = go.Figure(go.Bar(
        x=values, y=categories,
        orientation='h',
        marker_color='#bb86fc',
        text=values,
        textposition='auto'
    ))
    fig.update_layout(
        margin=dict(l=10, r=10, t=20, b=20),
        paper_bgcolor="#29294a",
        plot_bgcolor="#1e1e2f",
        font=dict(color="white", family="Montserrat"),
        height=280,
        yaxis=dict(autorange="reversed")
    )
    return fig

def heatmap(data, x_labels, y_labels):
    fig = go.Figure(data=go.Heatmap(
        z=data,
        x=x_labels,
        y=y_labels,
        colorscale='Viridis',
        colorbar=dict(title="Intensidad"),
        hoverongaps=False
    ))
    fig.update_layout(
        margin=dict(l=10, r=10, t=30, b=30),
        paper_bgcolor="#29294a",
        font=dict(color="white", family="Montserrat"),
        height=280,
    )
    return fig

def radar_chart(labels, values):
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=labels,
        fill='toself',
        line_color='#bb86fc'
    ))
    fig.update_layout(
        polar=dict(
            bgcolor='#29294a',
            radialaxis=dict(visible=True, range=[0, 100], gridcolor='gray'),
            angularaxis=dict(gridcolor='gray')
        ),
        showlegend=False,
        margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor="#29294a",
        font=dict(color="white", family="Montserrat"),
        height=280,
    )
    return fig

# --- FUNCIONES SECCIONES ---

def show_inicio():
    st.markdown("""
        <div class="main-container">
        <h1 class="header-title">Bienvenido a tu dashboard</h1>
        <p class="header-subtitle">Esta es la aplicación para visualizar datos claves en tiempo real.</p>
        </div>
    """, unsafe_allow_html=True)

def show_dashboard():
    # HEADER (sin que se corte)
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown('<h1 class="header-title">340,108 Unique Visitors</h1>', unsafe_allow_html=True)
        st.markdown('<p class="header-subtitle">' + datetime.today().strftime("%B %d, %Y") + ' - Overview del tráfico y comportamiento</p>', unsafe_allow_html=True)
    with col2:
        st.write("")  # para alinear

    # KPIs circulares
    kpi_cols = st.columns(3)
    colors = ['#bb86fc', '#6200ea', '#03dac6']
    for i, col in enumerate(kpi_cols):
        with col:
            st.markdown(f'<div class="kpi-box">', unsafe_allow_html=True)
            st.plotly_chart(circular_progress(kpi_values[i], kpi_labels[i], colors[i]), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")

    # Gráficos en 3 columnas (línea, dona, barras horizontales)
    graph_cols = st.columns(3)

    with graph_cols[0]:
        st.markdown('<h3 style="color:#bb86fc; font-weight:700;">Visitas en el último mes</h3>', unsafe_allow_html=True)
        st.plotly_chart(line_chart(dates, visits), use_container_width=True)

    with graph_cols[1]:
        st.markdown('<h3 style="color:#bb86fc; font-weight:700;">Fuentes de tráfico</h3>', unsafe_allow_html=True)
        st.plotly_chart(donut_chart(conversion_labels, conversion_values), use_container_width=True)

    with graph_cols[2]:
        st.markdown('<h3 style="color:#bb86fc; font-weight:700;">Ventas por Categoría</h3>', unsafe_allow_html=True)
        st.plotly_chart(horizontal_bar(categories, cat_values), use_container_width=True)

    st.write("---")

    # Últimos 2 gráficos en 2 columnas
    last_cols = st.columns(2)

    with last_cols[0]:
        st.markdown('<h3 style="color:#bb86fc; font-weight:700;">Mapa de actividad semanal</h3>', unsafe_allow_html=True)
        st.plotly_chart(heatmap(heatmap_data, hours, days), use_container_width=True)

    with last_cols[1]:
        st.markdown('<h3 style="color:#bb86fc; font-weight:700;">Indicadores Clave Radar</h3>', unsafe_allow_html=True)
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


# --- MAIN ---

if selected == "Inicio":
    show_inicio()
elif selected == "Dashboard":
    show_dashboard()
else:
    show_configuracion()

