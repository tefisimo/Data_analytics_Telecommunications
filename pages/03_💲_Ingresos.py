import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Configuración de la página en Streamlit
st.set_page_config(page_title="KPI 3", layout="centered")

# Cargar los datos
accesos_tecnologia = pd.read_csv('./CSVs/kpi_3/totales_accesos_por_tecnologia.csv')
ingresos = pd.read_csv('./CSVs/kpi_3/ingresos.csv')

# Combina las tablas en un único DataFrame usando Año y Trimestre como claves
df_merged = pd.merge(accesos_tecnologia, ingresos, on=['Año', 'Trimestre'])

# Cálculo de accesos totales en tecnologías avanzadas (Cablemodem y Fibra óptica)
df_merged['Accesos_Tecnologia_Avanzada'] = df_merged['Cablemodem'] + df_merged['Fibra óptica']

# Limpiar columnas no necesarias
df_merged.drop(columns=['ADSL', 'Cablemodem', 'Fibra óptica', 'Wireless', 'Otros', 'Total', 'Periodo_y'], inplace=True)

# Calculo de los ingresos por cada millón de accesos en tecnologías avanzadas
df_merged['Ingresos_por_Millon_Accesos'] = df_merged['Ingresos (miles de pesos)'] / (df_merged['Accesos_Tecnologia_Avanzada'] / 1_000_000)

# Título del dashboard
st.title("Dashboard Interactivo - KPI 3")
st.subheader("Incrementar en un 4% los ingresos trimestrales totales por cada millón de accesos en tecnologías avanzadas (Cablemodem, Fibra óptica) en el próximo trimestre a nivel nacional.")
st.markdown('***')

# Filtro de año
st.sidebar.header("Filtros")
year_selected = st.sidebar.selectbox("Selecciona un año:", df_merged['Año'].unique())

# Filtrar los datos según el año seleccionado
df_filtered = df_merged[df_merged['Año'] == year_selected]


# Creacion del medidor para KPI 3
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

# KPI 3: Ingresos por cada millon de accesos en tecnologias avanzadas
kpi3_previo = df_filtered["Ingresos_por_Millon_Accesos"].values[-2]
kpi3_meta = df_filtered['Ingresos_por_Millon_Accesos'].values[-1] 

# Mostrar el medidor de KPI 3
st.subheader(f"En el ultimo trimestre del año {year_selected} hemos cerrado de la siguiente manera")
st.plotly_chart(plot_gauge(kpi3_previo, kpi3_meta, 'Ingresos_por_Millon_Accesos'))

# Calculo de valor del KPI 2 y condicional para muestra de mensaje
valor_kpi = round((((kpi3_meta-kpi3_previo)/kpi3_previo) * 100), 2)
if valor_kpi > 4:
    st.markdown(f"""<div style="text-align: center; color: lightgreen;">
                ¡Felicidades! Para finales del año {year_selected} se ha logrado sobrepasar el KPI establecido.
                \n El valor porcentual del incremento fue de {valor_kpi}%
                </div>
                """, unsafe_allow_html=True)
else:
    st.markdown(f"""<div style="text-align: center; color: #F2545B;">
                ¡Lo siento! Para finales del año {year_selected} no se ha logrado sobrepasar el KPI establecido.
                \n El valor porcentual fue de {valor_kpi}%
                </div>
                """, unsafe_allow_html=True)


st.markdown('***')

# Análisis de tendencia para el año seleccionado
st.markdown("### Tendencia de Ingresos por Millón de Accesos en Tecnologías Avanzadas")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_filtered['Periodo_x'], df_filtered['Ingresos_por_Millon_Accesos'], marker='o', color='b', label='Ingresos por Millón de Accesos')
ax.set_xlabel('Periodo')
ax.set_ylabel('Ingresos por Millón de Accesos (miles de pesos)')
ax.set_title(f'Tendencia de Ingresos por Millón de Accesos en Tecnologías Avanzadas - Año {year_selected}')
ax.legend()
ax.grid()
st.pyplot(fig)

# Aplicar el cálculo de crecimiento intertrimestral
df_filtered['Crecimiento_Ingresos_por_Millon'] = df_filtered['Ingresos_por_Millon_Accesos'].pct_change() * 100

# Mostrar tabla con el crecimiento intertrimestral para el año seleccionado
st.markdown("### Crecimiento Intertrimestral de Ingresos por Millón de Accesos")
st.dataframe(df_filtered[['Año', 'Trimestre', 'Ingresos_por_Millon_Accesos', 'Crecimiento_Ingresos_por_Millon']])

st.markdown('***')

# Correlación entre accesos y ingresos para el año seleccionado
st.markdown("### Correlación entre Accesos en Tecnologías Avanzadas e Ingresos")
correlation = df_filtered['Accesos_Tecnologia_Avanzada'].corr(df_filtered['Ingresos (miles de pesos)'])
st.write(f"**Correlación entre accesos en tecnologías avanzadas e ingresos para el año {year_selected}:** {correlation:.2f}")

# Visualización de la correlación
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.scatter(df_filtered['Accesos_Tecnologia_Avanzada'], df_filtered['Ingresos (miles de pesos)'], color='purple')
ax2.set_xlabel('Accesos en Tecnologías Avanzadas')
ax2.set_ylabel('Ingresos (miles de pesos)')
ax2.set_title(f'Relación entre Accesos en Tecnologías Avanzadas e Ingresos - Año {year_selected}')
ax2.grid()
st.pyplot(fig2)

st.markdown('***')

# Aplicar el cálculo de crecimiento intertrimestral
df_merged['Crecimiento_Ingresos_por_Millon'] = df_merged['Ingresos_por_Millon_Accesos'].pct_change() * 100

# Mostrar tabla con el crecimiento intertrimestral - DATAFRAME COMPLETO
st.markdown("### Crecimiento Intertrimestral de Ingresos por Millón de Accesos - DATAFRAME COMPLETO")
st.dataframe(df_merged[['Año', 'Trimestre', 'Ingresos_por_Millon_Accesos', 'Crecimiento_Ingresos_por_Millon']])

# Resumen del análisis
st.markdown("### Conclusiones y Recomendaciones:")
st.write(f"""
- **Ingresos por Millón de Accesos**: Observamos cómo los ingresos se relacionan con la cantidad de accesos en tecnologías avanzadas en el año seleccionado.
- **Crecimiento Intertrimestral**: Analizamos el cambio porcentual en los ingresos para evaluar si el crecimiento proyectado es alcanzable.
""")
