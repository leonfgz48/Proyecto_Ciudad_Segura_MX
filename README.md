# Proyecto Ciudad Segura MX

## Objetivo

Construir un producto de datos que permita atacar los siguientes problemas:

* Falta de conocimiento detallado de la situación delictiva en la cdmx
que 

* falta de herramientas que ayuden a la identificación de retratos hablados 

## ¿Que es Ciudad Segura MX?

Ciudad segura es una plataforma que pretende brindar al usuario la información 
necesaria para poder identificar de manera fácil, cuantitativa y gráfica la 
actividad delictiva presente en la CDMX.

Setrata de una solución a los problemas anteriormente descritos, la cual fusiona 
dos  aspectos principales:

* Tablero de visualización:  Permite visualizar y analizar la evolución de los 
índices delictivos de manera clara y accesible para los usuarios. 

* Tecnología de reconocimiento facial: Permite identificar sospechosos a partir 
de un retrato hablado.

La plataforma se enuentra construida haciendo uso de las siguientes tecnologías:
    
* Python
* AWS S3
* AWS SageMaker
* AWS Rekognition
* AWS Athena
* AWS QuickSight

## Estructura del repositorio

### Documentación (Enregables)

* Working Backwards
    - Press Release (Descripción de la solución e imagen de enganche al producto)
    - Cinco preguntas alrededor del cliente (Entendimiento del cliente)
    - Solución final (imagen)
    - Frequently Asked Question (FAQ):
* Arquitectura de la solución (diagrama).
* Presentación 

### Producto de datos

* src del código en python que contempla:
    - Análisis, limpieza y tratamiento de datos
    - Modelo de clasificación de delitos
    - Análisi de reconocimiento facial mediante cliente de Rekognition AWS
* Librerias
    - Librerias personales requeridas

* Images
    - Carpeta de imagenes de "retratos hablados" (simulados)
    - Carpeta de imagenes de "delincuentes" (simulados)
* Datos
    - Raw data (conjunto de datos previo a tratamientos)
    - Clean data (conjunto de datos posterior a tratamientos)
