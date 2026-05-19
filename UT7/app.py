import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

@st.cache_data
def cargar_gran_pergamino():
    df = pd.read_csv("players_data.csv")
    return df

datos = cargar_gran_pergamino()

st.sidebar.markdown(
    """ 
    # Elite Scouting System
    
    ---
    """
)

nombre = st.sidebar.selectbox("Jugador Objetivo", datos.sort_values("Nombre"))

st.title("Panel de Análisis de Scouting")
st.markdown(
    f""" 
    Análisis detallado de **{nombre}** y búsqueda de candidatos compatibles.
    """
)


col1, col2, col3, col4 = st.columns(4)

equipo = datos.loc[datos['Nombre'] == nombre, 'Equipo'].values[0]
edad = datos.loc[datos['Nombre'] == nombre, 'Edad'].values[0]
valor = datos.loc[datos['Nombre'] == nombre, 'Valor_Mercado'].values[0]
equipo = datos.loc[datos['Nombre'] == nombre, 'Equipo'].values[0]


metricas_clustering = ['Goles', 'Pases_%', 'Recuperaciones']

kmeans = KMeans(n_clusters=3, random_state=42)

datos['Cluster'] = kmeans.fit_predict(datos[metricas_clustering])

centros = kmeans.cluster_centers_
idx_delanteros = centros[:, 0].argmax()
idx_medios = centros[:, 1].argmax()

nombres_roles = {}
for i in range(3):
    if i == idx_delanteros:
        nombres_roles[i] = "Delantero"
    elif i == idx_medios:
        nombres_roles[i] = "Medio"
    else:
        nombres_roles[i] = "Defensa"

datos['Rol_Tactico_KMeans'] = datos['Cluster'].map(nombres_roles)

rol_tactico = datos.loc[datos['Nombre'] == nombre, 'Rol_Tactico_KMeans'].values[0]

with col1:
    st.metric("Equipo", equipo)
with col2:
    st.metric("Edad", f"{edad} años")
with col3:
    st.metric("Valor", f"{valor} M€")
with col4:
    st.metric("Rol Táctico", rol_tactico)

df_filtrado = datos[(datos['Nombre'] == nombre) & (datos['Edad'] >= edad)]


st.sidebar.markdown(
    """ 
    ### Parámetros de Búsqueda
    """
)
prioridad = st.sidebar.radio(
    label="Prioridad de Búsqueda",
    options=["Similitud Actual", "Potencial Juvenil"]
)

edad = st.sidebar.slider("Límite de Edad", 16, 40, edad)

presupuesto = st.sidebar.number_input("Presupuesto Máximo (M€)", min_value=0, max_value=250, value=200)

st.markdown(
    """   
    ---
    """
)

goles = datos.loc[datos['Nombre'] == nombre, 'Goles'].values[0]
asistencias = datos.loc[datos['Nombre'] == nombre, 'Asistencias'].values[0]
pases = datos.loc[datos['Nombre'] == nombre, 'Pases_%'].values[0]
regates = datos.loc[datos['Nombre'] == nombre, 'Regates'].values[0]
duelos = datos.loc[datos['Nombre'] == nombre, 'Duelos_Aereos'].values[0]
xg = datos.loc[datos['Nombre'] == nombre, 'xG'].values[0]
recuperaciones = datos.loc[datos['Nombre'] == nombre, 'Recuperaciones'].values[0]


col_polar, col_mapa = st.columns(2)

with col_polar:
    st.markdown(
    """   
    ### Perfil Estadístico (Radar)
    """
    )
    metricas = ['Pases_%', 'Asistencias', 'Goles', 'xG', 'Duelos_Aereos', 'Recuperaciones', 'Regates', 'Pases_%']
    valores_jugador = [pases, asistencias, goles, xg, duelos, recuperaciones, regates, pases]
    
    fig_radar = px.scatter_polar(r=valores_jugador, theta=metricas, render_mode="svg")
    
    fig_radar.update_traces(mode="lines+markers", fill="toself")
    
    st.plotly_chart(fig_radar, use_container_width=True)

with col_mapa:
    st.markdown(
    """   
    ### Posicionamiento Táctico
    """
)
    fig_tactico = px.scatter(
        x=[datos.loc[datos['Nombre'] == nombre, 'Coord_X_Media'].values[0]],
        y=[datos.loc[datos['Nombre'] == nombre, 'Coord_Y_Media'].values[0]],
        range_x=[0, 100], 
        range_y=[0, 100],
        labels={'x': 'Profundidad', 'y': 'Amplitud'}
    )
    
    fig_tactico.update_traces(marker=dict(symbol='cross', size=20, color='red'))
    
    st.plotly_chart(fig_tactico, use_container_width=True)


st.markdown(
    """
    ### Candidatos Identificados
    """)

metricas_similitud = ['Pases_%', 'Regates', 'Recuperaciones', 'Duelos_Aereos', 'xG', 'Goles', 'Asistencias']

datos_norm = datos.copy()
for col in metricas_similitud:
    datos_norm[col] = datos[col] / datos[col].max()

p = datos_norm[datos_norm['Nombre'] == nombre][metricas_similitud].iloc[0]
candidatos_norm = datos_norm[datos_norm['Nombre'] != nombre][metricas_similitud]

distancias = (((candidatos_norm - p) ** 2).sum(axis=1)) ** 0.5

candidatos_df = datos[datos['Nombre'] != nombre].copy()
candidatos_df['Distancia'] = distancias

candidatos_filtrados = candidatos_df[
    (candidatos_df['Edad'] <= edad) & 
    (candidatos_df['Valor_Mercado'] <= presupuesto)
]

top_5 = candidatos_filtrados.sort_values(by='Distancia').head(5)
columnas_tabla = ['Nombre', 'Equipo', 'Edad', 'Valor_Mercado', 'Goles', 'Asistencias', 'Potencial']

st.dataframe(top_5[columnas_tabla], use_container_width=True)
st.caption("Nota: Las filas resaltadas en azul indican oportunidades de mercado basadas en rendimiento/coste.")

st.markdown("---")
st.markdown("### Seleccione candidato para comparativa técnica")

candidato_seleccionado = st.selectbox(
    "Candidato para comparar", 
    options=top_5['Nombre'].unique(), 
    label_visibility="collapsed"
)

col_radar2, col_proyeccion = st.columns(2)

with col_radar2:
    st.markdown("### Comparativa de Habilidades")
    
    fila_candidato = top_5[top_5['Nombre'] == candidato_seleccionado].iloc[0]
    
    nombres_radar = [nombre, nombre, nombre, nombre, nombre, nombre, nombre, nombre,
                     candidato_seleccionado, candidato_seleccionado, candidato_seleccionado, candidato_seleccionado, candidato_seleccionado, candidato_seleccionado, candidato_seleccionado, candidato_seleccionado]
                     
    metricas_radar = ['Pases_%', 'Regates', 'Recuperaciones', 'Duelos_Aereos', 'xG', 'Goles', 'Asistencias', 'Pases_%',
                      'Pases_%', 'Regates', 'Recuperaciones', 'Duelos_Aereos', 'xG', 'Goles', 'Asistencias', 'Pases_%']
                      
    valores_radar = [p, regates, recuperaciones, duelos, xg, goles, asistencias, p,
                     fila_candidato['Pases_%'], fila_candidato['Regates'], fila_candidato['Recuperaciones'], 
                     fila_candidato['Duelos_Aereos'], fila_candidato['xG'], fila_candidato['Goles'], fila_candidato['Asistencias'], fila_candidato['Pases_%']]
    
    df_doble_radar = pd.DataFrame({
        'Jugador': nombres_radar,
        'Métrica': metricas_radar,
        'Valor': valores_radar
    })
    
    fig_doble = px.line_polar(df_doble_radar, r='Valor', theta='Métrica', color='Jugador', line_close=True)
    fig_doble.update_traces(fill='toself')
    st.plotly_chart(fig_doble, use_container_width=True)


with col_proyeccion:
    st.markdown(f"### Proyección de Crecimiento: {candidato_seleccionado}")
    
    goles_base = fila_candidato['Goles']
    
    df_proyeccion = pd.DataFrame({
        'Año': ['2024', '2025', '2026', '2027'],
        'Goles Proyectados': [goles_base, goles_base + 3, goles_base + 6, goles_base + 10]
    })
    
    fig_linea = px.line(df_proyeccion, x='Año', y='Goles Proyectados', markers=True)
    
    fig_linea.add_hline(y=goles, line_dash="dash", annotation_text=f"Nivel {nombre}", annotation_position="bottom right")
    
    st.plotly_chart(fig_linea, use_container_width=True)
