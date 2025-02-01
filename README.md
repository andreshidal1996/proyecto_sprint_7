# Proyecto Sprint 7 - Herramientas de Desarrollo Web

## Descripción

Esta aplicación web permite a los usuarios explorar datos sobre vehículos usados a la venta. Con la
ayuda de Streamlit, la app permite visualizar diferentes gráficos y analizar el conjunto de datos
`vehicles_us.csv`.

## Funcionalidad

- **Visualización de Histogramas**: Muestra cómo se distribuye el kilometraje (odometer) de los
  vehículos.
- **Gráfico de Dispersión**: Muestra la relación entre el kilometraje y el precio (price) de los
  vehículos, según su tipo.
- **Interfaz Interactiva**: Los usuarios pueden elegir qué gráficos desean ver mediante casillas de
  verificación.

## Requisitos

- Python 3.x
- Streamlit
- Pandas
- Plotly Express

## Uso

1. Clonar el repositorio y entrar al directorio del proyecto.
2. Instalar las dependencias ejecutando:

   ```bash
   pip install -r requirements.txt
   ```

## Liga del proyecto

https://proyecto-sprint-7-0fjn.onrender.com/

## Comentarios adicionales para el tutor

Para este proyecto, he instalado únicamente 3 librerías, y a continuación traté de exportar las
dependencias utilizando los siguientes comandos:

```
$ conda install pandas scipy numpy -y
$ pip install streamlit plotly_express
$ conda list --export requirements.txt
```

Al exportar con el comando de conda, se generó una lista mucho más extensa, con al menos 30
dependencias. Sin embargo, al intentar hacer el deploy en Render, se produjo un error. ¿Qué se puede
hacer en estos casos, cuando el comando genera más dependencias de las que realmente son necesarias?
