# Importar librerías necesarias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Cargar los datos
velocidad_por_prov = pd.read_csv('./CSVs/kpi_2/velocidad_%_por_prov.csv')

# Configuración de la página
st.set_page_config(page_title="KPI 2", layout="centered")

# Título de la aplicación
st.title("Dashboard Interactivo - KPI 2")
st.subheader("Incrementar la velocidad media de bajada en Mbps en un 5% por provincia para el siguiente trimestre.")

st.markdown('***')

# Filtros de provincia y año
st.sidebar.header("Filtros")
provincia_selected = st.sidebar.selectbox("Selecciona una provincia:", velocidad_por_prov['Provincia'].unique())
year_selected = st.sidebar.selectbox("Selecciona un año:", velocidad_por_prov['Año'].unique())

# Filtrar datos para la provincia seleccionada
datos_provincia = velocidad_por_prov[velocidad_por_prov['Provincia'] == provincia_selected]

# Filtrar los datos según la provincia y el año seleccionados
df_filtered = velocidad_por_prov[(velocidad_por_prov['Provincia'] == provincia_selected) & 
                                  (velocidad_por_prov['Año'] == year_selected)]


# Creacion del medidor para KPI 2
def plot_gauge(kpi_previous, kpi_actual, title):
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=kpi_actual,
        delta={'reference': kpi_previous},
        gauge={
            'axis': {'range': [None, kpi_actual + 10]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, kpi_actual], 'color': "lightblue"},
                {'range': [kpi_previous, kpi_actual], 'color': "lightgreen"}
            ]
        },
        title={'text': title},
    ))
    fig.update_layout(height=300, margin={'t': 0, 'b': 0, 'l': 0, 'r': 0})
    return fig

# KPI 2: Acceso al servicio de Internet por cada 100 hogares
kpi2_previo = df_filtered["Mbps (Media de bajada)"].values[-2]
kpi2_meta = df_filtered["Mbps (Media de bajada)"].values[-1] 

# Mostrar el medidor de KPI 2
st.subheader(f"En el ultimo trimestre del año {year_selected} en la provincia de {provincia_selected} hemos cerrado de la siguiente manera")
st.plotly_chart(plot_gauge(kpi2_previo, kpi2_meta, "Mbps (Media de bajada)"))

# Calculo de valor del KPI 2 y condicional para muestra de mensaje
valor_kpi = round((((kpi2_meta-kpi2_previo)/kpi2_previo) * 100), 2)
if valor_kpi > 5:
    st.markdown(f"""<div style="text-align: center; color: lightgreen;">
                ¡Felicidades! Para finales del año {year_selected} en la provincia de {provincia_selected} se ha logrado sobrepasar el KPI establecido.
                \n El valor porcentual del incremento fue de {valor_kpi}%
                </div>
                """, unsafe_allow_html=True)
else:
    st.markdown(f"""<div style="text-align: center; color: #F2545B;">
                ¡Lo siento! Para finales del año {year_selected} en la provincia de {provincia_selected} no se ha logrado sobrepasar el KPI establecido.
                \n El valor porcentual fue de {valor_kpi}%
                </div>
                """, unsafe_allow_html=True)

st.markdown('***')

# Gráfico de tendencia de velocidad para la provincia seleccionada
st.subheader(f"Tendencia de Velocidad Media de Bajada en {provincia_selected}")
fig, ax = plt.subplots()
ax.plot(datos_provincia['Año'], datos_provincia['Mbps (Media de bajada)'], marker='o', color='teal')
ax.set_title(f"Velocidad Media de Bajada en {provincia_selected}")
ax.set_xlabel("Año")
ax.set_ylabel("Velocidad Media (Mbps)")
st.pyplot(fig)

# Calcular promedio nacional por trimestre
promedio_nacional_trimestre = velocidad_por_prov.groupby('Año')['Mbps (Media de bajada)'].mean()

# Gráfico de comparación de velocidad
st.subheader(f"Comparación de Velocidad Media de {provincia_selected} con el Promedio Nacional")
fig, ax = plt.subplots()
ax.plot(datos_provincia['Año'], datos_provincia['Mbps (Media de bajada)'], marker='o', label=provincia_selected, color='teal')
ax.plot(promedio_nacional_trimestre, marker='o', linestyle='--', label='Promedio Nacional', color='black')
ax.set_title(f"Comparación de Velocidad Media en {provincia_selected} vs Promedio Nacional")
ax.set_xlabel("Año")
ax.set_ylabel("Velocidad Media (Mbps)")
ax.legend()
st.pyplot(fig)

st.markdown('***')

# Mostrar la velocidad media de bajada trimestral en la provincia y año seleccionados
st.markdown(f"### Velocidad Media de Bajada (Mbps) - {provincia_selected} en {year_selected}")
st.dataframe(df_filtered[['Trimestre', 'Mbps (Media de bajada)']])

# Visualización de la tendencia de velocidad media de bajada trimestral
st.markdown(f"### Tendencia Trimestral de la Velocidad Media de Bajada - {provincia_selected} en {year_selected}")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_filtered['Trimestre'], df_filtered['Mbps (Media de bajada)'], marker='o', color='g', label='Mbps (Media de bajada)')
ax.axhline(y=df_filtered['Mbps (Media de bajada)'].mean(), color='red', linestyle='--', label='Promedio anual')
ax.set_xlabel('Trimestre')
ax.set_ylabel('Mbps (Media de bajada)')
ax.set_title(f'Tendencia de la Velocidad Media de Bajada en {provincia_selected} - {year_selected}')
ax.legend()
ax.grid()
st.pyplot(fig)

st.markdown('***')

# Calcular el crecimiento intertrimestral de la velocidad media de bajada
df_filtered['Crecimiento_Trimestral_%'] = df_filtered['Mbps (Media de bajada)'].pct_change() * 100

# Mostrar tabla con el crecimiento intertrimestral para el año y provincia seleccionados
st.markdown(f"### Crecimiento Intertrimestral de Velocidad Media de Bajada -  {provincia_selected} en {year_selected}")
st.dataframe(df_filtered[['Trimestre', 'Mbps (Media de bajada)', 'Crecimiento_Trimestral_%']])

# Calcular el crecimiento porcentual trimestral
datos_provincia['Crecimiento_Trimestral_%'] = datos_provincia['Mbps (Media de bajada)'].pct_change() * 100

# Mostrar crecimiento trimestral
st.subheader(f"Crecimiento Trimestral de Velocidad en {provincia_selected} - DATAFRAME COMPLETO")
st.write(datos_provincia[['Año', 'Trimestre', 'Mbps (Media de bajada)', 'Crecimiento_Trimestral_%']])
st.line_chart(datos_provincia[['Año', 'Mbps (Media de bajada)']].set_index('Año'))


st.markdown("### Conclusiones y Recomendaciones:")
st.write("""
- Hemos encontrado como patron relacionando el analisis previo de los accesos que las provincias con menor cantidad de accesos por cada 100 hogares presentan velocidades medias de bajada por debajo del promedio nacional.
- Esto no implica que estas provincias no hayan tenido incrementos en su velocidad a lo largo del tiempo; de hecho, en promedio, la velocidad ha aumentado.
""")
