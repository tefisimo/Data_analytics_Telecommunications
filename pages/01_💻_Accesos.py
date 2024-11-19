import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Configuración de la página de Streamlit
st.set_page_config(page_title="KPI 1", layout="centered")

# Cargar los datos
penetracion_hogares = pd.read_csv('./CSVs/kpi_1/penetracion_hogares.csv')
accesos_tecnologia_localidad = pd.read_csv('./CSVs/kpi_1/accesos_tecnologia_localidad.csv')
velocidad_provincia = pd.read_csv('./CSVs/kpi_2/velocidad_%_por_prov.csv')

# Título
st.title("Dashboard Interactivo - KPI 1")
st.subheader("Aumentar en un 2% la penetración de accesos a Internet por cada 100 hogares, por provincia, para el próximo trimestre")

st.markdown('***')

# Filtros de provincia y año
st.sidebar.header("Filtros")
provincia_selected = st.sidebar.selectbox("Selecciona una provincia:", penetracion_hogares['Provincia'].unique())
year_selected = st.sidebar.selectbox("Selecciona un año:", penetracion_hogares['Año'].unique())

# Filtrar los datos según la provincia y el año seleccionados
df_filtered = penetracion_hogares[(penetracion_hogares['Provincia'] == provincia_selected) & 
                                  (penetracion_hogares['Año'] == year_selected)]


# Creacion del medidor para KPI 1
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

# KPI 1: Acceso al servicio de Internet por cada 100 hogares
kpi1_previo = df_filtered["Accesos por cada 100 hogares"].values[-2]
kpi1_meta = df_filtered["Accesos por cada 100 hogares"].values[-1] 

# Mostrar el medidor de KPI 1
st.subheader(f"En el ultimo trimestre del año {year_selected} hemos cerrado de la siguiente manera")
st.plotly_chart(plot_gauge(kpi1_previo, kpi1_meta, "Acceso Internet por 100 Hogares"))

# Calculo de valor del KPI 1 y condicional para muestra de mensaje
valor_kpi = round((((kpi1_meta-kpi1_previo)/kpi1_previo) * 100), 2)
if valor_kpi > 2:
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

# Mostrar penetración promedio por provincia
st.markdown("### Accesos promedios por Provincia")
penetracion_provincia = penetracion_hogares.groupby('Provincia')['Accesos por cada 100 hogares'].mean()
fig, ax = plt.subplots(figsize=(10, 6))
penetracion_provincia.plot(kind='bar', ax=ax, color='skyblue')
ax.set_title('Penetración de Accesos por Cada 100 Hogares')
ax.set_xlabel('Provincia')
ax.set_ylabel('Penetración por cada 100 Hogares')
st.pyplot(fig)

st.markdown('***')

# Mostrar la penetración de internet por cada 100 hogares en la provincia y año seleccionados
st.markdown(f"### Accesos de Internet por cada 100 Hogares - {provincia_selected} en {year_selected}")
st.dataframe(df_filtered[['Año', 'Trimestre', 'Accesos por cada 100 hogares']])

# Visualización de la tendencia de penetración trimestral para el año seleccionado
st.markdown("### Tendencia Trimestral de la Penetración de Internet")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_filtered['Trimestre'], df_filtered['Accesos por cada 100 hogares'], marker='o', color='b', label='Accesos por cada 100 hogares')
ax.axhline(y=df_filtered['Accesos por cada 100 hogares'].mean(), color='red', linestyle='--', label='Promedio anual')
ax.set_xlabel('Trimestre')
ax.set_ylabel('Accesos por cada 100 hogares')
ax.set_title(f'Tendencia de la Penetración de Internet en {provincia_selected} - {year_selected}')
ax.legend()
ax.grid()
st.pyplot(fig)

st.markdown('***')

# Análisis de accesos por tecnología en la provincia seleccionada
st.markdown("### Accesos de Internet por Tecnología en la Provincia Seleccionada")
penetracion_tecnologia = accesos_tecnologia_localidad[accesos_tecnologia_localidad['Provincia'] == provincia_selected]
penetracion_tecnologia_grouped = penetracion_tecnologia.groupby('Tecnologia')['Accesos'].sum()
fig2, ax2 = plt.subplots(figsize=(8, 6))
penetracion_tecnologia_grouped.plot(kind='bar', ax=ax2, color='orange')
ax2.set_title(f'Accesos por Tecnología en {provincia_selected}')
ax2.set_xlabel('Tecnología')
ax2.set_ylabel('Total de Accesos')
st.pyplot(fig2)

st.markdown('***')

# Calcular el crecimiento intertrimestral de la velocidad media de bajada
df_filtered['Crecimiento Trimestral %'] = df_filtered['Accesos por cada 100 hogares'].pct_change() * 100

# Mostrar tabla con el crecimiento intertrimestral para el año y provincia seleccionados
st.markdown(f"### Crecimiento Intertrimestral de Accesos por cada 100 hogares -  {provincia_selected} en {year_selected}")
st.dataframe(df_filtered[['Trimestre', 'Accesos por cada 100 hogares', 'Crecimiento Trimestral %']])

# Análisis de crecimiento trimestral en la penetración
# Filtrar datos para la provincia seleccionada
datos_provincia = penetracion_hogares[penetracion_hogares['Provincia'] == provincia_selected]
# Calcular el crecimiento porcentual trimestral
datos_provincia['Crecimiento_Trimestral_%'] = datos_provincia['Accesos por cada 100 hogares'].pct_change() * 100
# Mostrar crecimiento trimestral
st.subheader(f"Crecimiento Trimestral de Accesos en {provincia_selected} - DATAFRAME COMPLETO")
st.write(datos_provincia[['Año', 'Trimestre', 'Accesos por cada 100 hogares', 'Crecimiento_Trimestral_%']])
st.line_chart(datos_provincia[['Año', 'Accesos por cada 100 hogares']].set_index('Año'))


# Resumen final
st.markdown("### Conclusiones y Recomendaciones:")
st.write("""
- **Accesos Promedios por Cada 100 hogares por Provincia:** El gráfico de penetración por provincia destaca las áreas con menor acceso, identificando posibles puntos de enfoque para mejorar.
- **Distribución de Tecnología:** En promedio, observamos que todas las provincias cuentan con un mayor acceso en las tecnologías avanzadas.
- **Crecimiento Trimestral:** Visualizar el crecimiento trimestral permite identificar provincias con potencial para aumentar su penetración.
Para que este crecimiento sea realmente inclusivo, podría ser beneficioso centrar los esfuerzos en provincias con menores accesos, lo que permitiría reducir la brecha de conectividad
""")
