import streamlit as st

# Configuración de la página en Streamlit
st.set_page_config(page_title="Análisis de KPIs de Conectividad e Ingresos", layout="centered")

# URL de la imagen de encabezado
url_imagen = "./Imagen/Internet solutions.gif"

# Mostrar imagen
st.image(url_imagen, use_container_width=True)

# Título principal
st.title("Bienvenidos al Análisis de KPIs de Conectividad e Ingresos")

# Descripción del Proyecto
st.markdown("""
Este dashboard interactivo ha sido desarrollado para explorar y analizar los indicadores clave de desempeño (KPIs) relacionados con la conectividad a Internet y los ingresos generados a través de tecnologías avanzadas en distintas provincias. El objetivo es facilitar una comprensión profunda y visual de cómo evolucionan estos indicadores a lo largo del tiempo, así como las tendencias clave que guiarán las futuras decisiones estratégicas.
""")

st.sidebar.header("🌐 Bienvenidos")
st.sidebar.markdown("""\nCon este Dashboard tendrás acceso a datos actualizados y análisis de información clave acerca del ámbito de telecomunicaciones en Argentina desde el año 2014 al 2024. 
                    Esto con el objetivo de poder orientar e implementar decisiones que permitan mejorar el enfoque de inversiones, la calidad del servicio y el acceso del servicio en la población.
                    \nUtiliza los filtros y gráficos interactivos para personalizar tu vista. 
                    \nNo dudes en consultar cualquier duda o generar alguna acotación, sera bien recibida.
                    \n Contacto: gustavoadolfogonz@gmail.com
                    """)

# Sección de Descripción de los KPIs
st.subheader("Descripción del Proyecto")
st.markdown("""
Este análisis aborda tres KPIs fundamentales:

1. **KPI 1**: Aumentar el acceso al servicio de Internet en cada 100 hogares, por provincia, con un crecimiento proyectado del 2% en el próximo trimestre.
2. **KPI 2**: Incrementar la velocidad media de bajada en todas las provincias en un 5% en el próximo trimestre, para mejorar la experiencia del usuario.
3. **KPI 3**: Aumentar en un 4% los ingresos trimestrales por cada millón de accesos en tecnologías avanzadas (como Cablemodem y Fibra óptica) para el próximo trimestre.
""")

# Sección de Estructura del Dashboard
st.subheader("Estructura del Dashboard")
st.markdown("""
Este dashboard permite seleccionar provincias, años y otros filtros para visualizar la evolución de estos KPIs de forma intuitiva. Cada página de KPI incluye:

- Visualización de tendencias para evaluar el rendimiento en cada periodo.
- Cálculos intertrimestrales y gráficos interactivos que ayudan a proyectar el cumplimiento de los objetivos.
- Análisis de correlaciones y patrones en los datos, para una interpretación más detallada y estratégica.
""")

# Sección de Expectativas del Análisis
st.subheader("¿Qué se puede esperar de este análisis?")
st.markdown("""
Este proyecto facilita el monitoreo y análisis detallado de cada KPI, permitiendo identificar áreas de mejora y oportunidades de crecimiento en el acceso y uso de Internet. Se ha diseñado con el propósito de ofrecer una visión integral de los datos de conectividad en distintas regiones, apoyando decisiones basadas en datos y contribuyendo al avance tecnológico y social.
""")


