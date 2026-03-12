# Práctica 2. El Índice de las Sombras (NoSQL)
El objetivo de esta práctica es diseñar una base de datos clave-valor para el acceso de alto rendimiento.

## Ejercicio 1. Creación de la tabla principal.
Creamos la tabla CensoAlianza con partition key ID_Ninja, sort key Fecha_Registro y capacidad "On-demand".

<img src = "imagenes/1.png"></img>
<img src = "imagenes/2.png"></img>

<br></br>

## Ejercicio 2. Ingesta de datos críticos.
Creamos 5 registros cada uno con columnas diferentes.

<img src = "imagenes/3.png"></img>
<img src = "imagenes/4.png"></img>
<img src = "imagenes/5.png"></img>
<img src = "imagenes/6.png"></img>
<img src = "imagenes/7.png"></img>

<br></br>

## Ejercicio 3. Simulación de busqueda ANBU.
Uso una query para buscar por ID_Ninja.

<img src = "imagenes/8.png"></img>
<img src = "imagenes/9.png"></img>

<br></br>

Realizo ahora un escaneo para mostrar los ninjas de un clan específico.

<img src = "imagenes/10.png"></img>
<img src = "imagenes/11.png"></img>

El scan es más lento y costoso porque en vez de leer solo los registros que coinciden con la busqueda los lee todos.

<br></br>

## Ejercicio 4. Actualización dinámica.
Modifico un registro añadiendo el atributo Nivel_Amenaza.

<img src = "imagenes/12.png"></img>

<br></br>

## Análisis técnico.
Explica qué Partition Key elegirías si tuvieras que buscar habitualmente por “Aldea” en lugar de por “ID” y qué es un Global Secondary Index (GSI).

Pondría de partition key aldea. GSI es un índice secundario que permite hacer busquedas query a una table usando una partition key diferente.
