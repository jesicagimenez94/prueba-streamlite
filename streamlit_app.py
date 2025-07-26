import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta

# Configuración de la página
st.set_page_config(page_title="Dashboard Moderno", layout="wide")

# Estilos CSS personalizados
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #f0f0f0;
            font-family: 'Montserrat', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #1e1e2f;
        }
        .header-title {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
            color: #ffffff;
        }
        .header-subtitle {
            font-size: 1.1rem;
            color: #bbbbbb;
        }
        .kpi-box {
            background-color: #1e1e2f;
            border-radius: 16px;
            padding: 1rem;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Datos ficticios
np.random.seed(42)
dates = pd.date_range(end=datetime.today(), periods=30)
visits = np.random.randint(4000, 12000, size=len(dates))
conversion_labels = ["Orgánico", "Pago", "Referencias", "Social"]
conversion_values = np.random.randint(10, 40, size=4)
categories = ["Electrónica", "Ropa", "Hogar", "Deportes", "Juguetes"]
cat_values = np.random.randint(100, 1000, size=5)
days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
hours = [str(h)+":00" for h in range(24)]
heatmap_data = np.random.randint(0, 100, size=(7, 24))
kpi_values = [72, 85, 64]
kpi_labels = ["Retención", "Satisfacción", "Conversión"]

# Funciones de visualización
def circular_progress(value, label, color):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': label},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
            'bgcolor': "#2c2c2c",
            'borderwidth': 2,
            'bordercolor': "gray",
        }
    ))
    fig.update_layout(height=200, margin=dict(t=20, b=0, l=0, r=0), paper_bgcolor="#1e1e2f", font_color="#ffffff")
    return fig

def line_chart(x, y):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', line=dict(color='#bb86fc')))
    fig.update_layout(height=300, margin=dict(t=30, b=0), paper_bgcolor="#1e1e2f", plot_bgcolor="#1e1e2f", font_color="white")
    return fig

def donut_chart(labels, values):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5)])
    fig.update_traces(marker=dict(colors=['#bb86fc','#6200ea','#03dac6','#3700b3']))
    fig.update_layout(height=300, paper_bgcolor="#1e1e2f", font_color="white")
    return fig

def horizontal_bar(labels, values):
    fig = go.Figure(go.Bar(y=labels, x=values, orientation='h', marker_color='#03dac6'))
    fig.update_layout(height=300, paper_bgcolor="#1e1e2f", font_color="white")
    return fig

def heatmap(z, x, y):
    fig = go.Figure(data=go.Heatmap(z=z, x=x, y=y, colorscale='Viridis'))
    fig.update_layout(height=300, paper_bgcolor="#1e1e2f", font_color="white")
    return fig

def radar_chart(labels, values):
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=values, theta=labels, fill='toself', line_color='#bb86fc'))
    fig.update_layout(polar=dict(bgcolor="#1e1e2f"), height=300, paper_bgcolor="#1e1e2f", font_color="white")
    return fig

# Función para mostrar la página principal
def show_dashboard():
    st.markdown(f'<h1 class="header-title">Dashboard de Datos</h1>', unsafe_allow_html=True)

    # Filtros
    st.markdown("### Filtros")
    colf1, colf2 = st.columns(2)
    with colf1:
        fecha_min = st.date_input("Fecha desde:", dates.min().date())
    with colf2:
        fecha_max = st.date_input("Fecha hasta:", dates.max().date())

    # Aplicar filtro a las visitas por fecha
    df_visitas = pd.DataFrame({
        "Fecha": dates,
        "Visitas": visits
    })
    df_filtrado = df_visitas[(df_visitas["Fecha"] >= pd.to_datetime(fecha_min)) & (df_visitas["Fecha"] <= pd.to_datetime(fecha_max))]

    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(f'<h1 class="header-title">{df_filtrado["Visitas"].sum():,} Visitantes Únicos</h1>', unsafe_allow_html=True)
        st.markdown(f'<p class="header-subtitle">{datetime.today().strftime("%d de %B de %Y")} - Visión general del tráfico y comportamiento</p>', unsafe_allow_html=True)

    # KPIs
    kpi_cols = st.columns(3)
    colors = ['#bb86fc', '#6200ea', '#03dac6']
    for i, col in enumerate(kpi_cols):
        with col:
            st.markdown(f'<div class="kpi-box">', unsafe_allow_html=True)
            st.plotly_chart(circular_progress(kpi_values[i], kpi_labels[i], colors[i]), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")

    # Gráficos
    graph_cols = st.columns(3)
    with graph_cols[0]:
        st.markdown('<h3 style="color:#bb86fc; font-weight:700;">Visitas en el último mes</h3>', unsafe_allow_html=True)
        st.plotly_chart(line_chart(df_filtrado["Fecha"], df_filtrado["Visitas"]), use_container_width=True)
    with graph_cols[1]:
        st.markdown('<h3 style="color:#bb86fc; font-weight:700;">Fuentes de Tráfico</h3>', unsafe_allow_html=True)
        st.plotly_chart(donut_chart(conversion_labels, conversion_values), use_container_width=True)
    with graph_cols[2]:
        st.markdown('<h3 style="color:#bb86fc; font-weight:700;">Ventas por Categoría</h3>', unsafe_allow_html=True)
        st.plotly_chart(horizontal_bar(categories, cat_values), use_container_width=True)

    st.write("---")

    last_cols = st.columns(2)
    with last_cols[0]:
        st.markdown('<h3 style="color:#bb86fc; font-weight:700;">Mapa de Actividad Semanal</h3>', unsafe_allow_html=True)
        st.plotly_chart(heatmap(heatmap_data, hours, days), use_container_width=True)
    with last_cols[1]:
        st.markdown('<h3 style="color:#bb86fc; font-weight:700;">Indicadores Clave Radar</h3>', unsafe_allow_html=True)
        radar_labels = ["Calidad", "Velocidad", "Satisfacción", "Eficiencia", "Innovación"]
        radar_values = [70, 80, 85, 60, 90]
        st.plotly_chart(radar_chart(radar_labels, radar_values), use_container_width=True)

    st.write("---")

    # Tabla con todos los datos
    st.markdown("### 📄 Detalle de Datos")
    st.dataframe(df_visitas, use_container_width=True)

# Barra lateral con avatar, nombre y menú
with st.sidebar:
    st.image("imagen1.png", width=150)
    st.markdown("""
        <div style="text-align: center;">
            <h2 style="margin-bottom: 0;">Jesica Gimenez</h2>
            <p style="margin-top: 0; color: #bbb;">Analista de Datos</p>
        </div>
    """, unsafe_allow_html=True)

    selected = option_menu(
        menu_title="Menú",
        options=["Inicio", "Dashboard", "Configuración"],
        icons=["house", "bar-chart", "gear"],
        menu_icon="cast",
        default_index=1,
        styles={
            "container": {"background-color": "#1e1e2f"},
            "icon": {"color": "white"},
            "nav-link": {"color": "#bbb", "font-size": "16px"},
            "nav-link-selected": {"background-color": "#3700b3", "color": "white"},
        }
    )

# Mostrar contenido según selección
if selected == "Inicio":
    st.title("Bienvenida a tu Panel de Control")
elif selected == "Dashboard":
    show_dashboard()
elif selected == "Configuración":
    st.title("Configuración")

