![DataConnect](./Imagen/Internet%20solutions.gif)

# Proyecto Individual: Análisis Exploratorio y Dashboard de KPIs

## Analista de Datos: Gustavo Gonzalez

## Introduccion

Este proyecto se centra en la creación de un análisis exploratorio de datos y un dashboard interactivo de KPIs, desarrollado en Streamlit, que permite la visualización y monitoreo de indicadores clave de desempeño en el ámbito de conectividad e Internet. Los objetivos de los KPIs incluyen el análisis de acceso a tecnologías avanzadas (Cablemodem y Fibra Óptica), el incremento de los accesos de conectividad por cada 100 hogares y la velocidad de conexión por provincia. A través de un diseño intuitivo y herramientas interactivas, la plataforma permite observar tendencias, comparar datos y tomar decisiones informadas.

## Requisitos previos

Tener instalado Python y un editor de texto como Visual Studio Code.

Clonar el repositorio del link https://github.com/tefisimo/data_analytics_telecommunications

El cual posee los archivos:
* README.md : Descripción del proyecto.
* EDA.ipynb: Notebook con el análisis exploratorio de datos.
* ETL.ipynb: Notebook de preparación y limpieza de los datos.
* Introduccion.py: Archivo principal para ejecutar la aplicación en Streamlit. 
* requirements.txt: Librerías necesarias para el proyecto.

## Instalación

Instalar dependencias ejecutando en una terminal: pip install -r requirements.txt

Asegúrate de ejecutar este comando desde la ubicación raíz del proyecto, donde se encuentra el archivo requirements.txt.

## Estructura de Datos y ETL

El proceso de ETL incluyó:

* Limpieza de las columnas para obtener información de acceso y velocidad por provincia.
* Formateo de valores en las columnas de **`Provincia`**, **`Tecnologia`**, **`Trimestre`**, **`Año`**  y cálculo de nuevas columnas para análisis de KPIs.
* Filtrado e imputación de valores sobre los valores nulos para mantener integridad en el análisis.

## Exploración de Datos (EDA)

El análisis exploratorio fue clave para entender la relación entre accesos, velocidad y ingresos. Algunos hallazgos:

* Distribución de accesos en tecnologías avanzadas: Las provincias tienden a tener más accesos en Cablemodem y Fibra Óptica en comparación con tecnologías tradicionales.
* Velocidad media de descarga: Provincias con menor acceso a tecnologías avanzadas tienden a presentar una velocidad media por debajo del promedio nacional.
* Crecimiento en el tiempo: Los ingresos por tecnologías avanzadas aumentaron, aunque el análisis considera ajustes por inflación y otros factores económicos.

## KPIs Desarrollados

KPI 1: Aumento de Ingresos

Objetivo: Incrementar en un 4% los ingresos trimestrales por millón de accesos en tecnologías avanzadas.

* Visualización: Un gráfico de línea muestra la tendencia de ingresos por trimestre, con filtros de año y trimestre.
* Hallazgo clave: Existe una correlación directa entre ingresos y accesos en tecnologías avanzadas.

KPI 2: Velocidad Media de Bajada

Objetivo: Incrementar en un 5% la velocidad media de descarga en todas las provincias para el próximo trimestre.

* Visualización: Un medidor muestra la velocidad media por provincia, junto a un gráfico de dispersión que permite comparar con el promedio nacional.
* Hallazgo clave: Provincias con menor acceso presentan una velocidad media más baja, aunque han mostrado incrementos graduales a lo largo del tiempo.

KPI 3: Incremento de Accesos por cada 100 Hogares

Objetivo: Aumentar en un 2% la penetración de accesos a Internet por cada 100 hogares, por provincia, para el próximo trimestre

* Visualización: Un gráfico de barras por provincia permite observar la distribución de accesos.
* Hallazgo clave: Las provincias en promedio tienen un mayor acceso en tecnologías avanzadas, aunque algunas aún necesitan mejorar.

## Implementación en Streamlit
Ejecución
Para iniciar la aplicación: streamlit run Introduccion.py

Funcionalidades de Interactividad

* Filtros por año y provincia: permite un análisis específico para cada KPI.
* Medidores de progreso: muestran el cumplimiento actual en relación con el objetivo de cada KPI.
* Gráficos de tendencias y comparativos: facilitan la visualización de los patrones y el crecimiento de los indicadores en el tiempo.

## Pagina Web del Deploy
https://

## Contacto
Email: gustavoadolfogonz@gmail.com
Linkedin: Gustavo Gonzalez, link: https://www.linkedin.com/in/gustavo-gonzalez-data/