# Práctica 3: DynamoDB y el Poder de las Bases de Datos Serverless.

### Ejercicio 1: Creando nuestra primera tabla en la nube.
**Lo primero es crear el “contenedor” para nuestros datos. En DynamoDB, estos contenedores se llaman tablas.**

1. **Inicia sesión en la Consola de AWS.**
2. **En el buscador de servicios, escribe DynamoDB y accede a su panel.**
3. **Haz clic en “Create table”.**
4. **Configura los siguientes valores:**
 - **Table name: Orders**
 - **Partition key: order_id (y asegúrate de que el tipo sea String).**
5. **Deja el resto de opciones con sus valores por defecto y haz clic en “Create table”.**

**Muestra una imagen de tu tabla Orders creada correctamente en la consola de DynamoDB.**
<img src="imagenes\1.png">
<br></br>

### Ejercicio 2. Insertando nuestros primeros pedidos.
**Ahora que tenemos la tabla, vamos a añadirle datos.**

1. **En el menú de la izquierda, dentro de tu tabla, ve a “Explore items”.**
2. **Haz clic en “Create item”.**
3. **La forma más sencilla de insertar datos complejos es usando la vista JSON. Pega el siguiente contenido. Fíjate en la sintaxis: DynamoDB requiere que especifiques el tipo de dato ("S" para String, "N" para Number).**
4. **Haz clic en “Create item”.**
. **¡Tu turno! Repite el proceso y añade al menos tres pedidos más, con datos diferentes. Varía los productos, clientes y estados (Pending, Shipped, Delivered).**

**Muestra una vista de la tabla con todos los ítems que has creado.**
<img src="imagenes\2.png">
<br></br>

### Ejercicio 3. Explorando y modificando los datos.
**Con los datos ya en la tabla, veamos cómo consultarlos y actualizarlos.**

1. **Dentro de “Explore items”, puedes ver todos los pedidos. La consola ofrece una opción para filtrar (Filter items). Úsala para encontrar pedidos que cumplan ciertas condiciones. Por ejemplo:**
 - **Busca todos los pedidos con status igual a "Shipped".**
<img src="imagenes\3.png">
<img src="imagenes\4.png">


 - **Busca los pedidos de un cliente específico.**
<img src="imagenes\5.png">
<img src="imagenes\6.png">
<br></br>

2. **Haz clic sobre cualquiera de los ítems para ver sus detalles.**


3. **Puedes editar un campo directamente desde esta vista. Busca un pedido con estado "Pending" y cámbialo a "Delivered". Guarda los cambios.**
<img src="imagenes\7.png">
<img src="imagenes\8.png">
<br></br>

### Ejercicio 4. Eliminando un pedido.
**Finalmente, vamos a eliminar un ítem. En DynamoDB, la forma más eficiente de eliminar es usando su clave primaria.**

1. **En la vista “Explore items”, selecciona el ítem que deseas borrar marcando la casilla a su izquierda.**
2. **Haz clic en el menú “Actions” y selecciona “Delete item”.**
3. **Confirma la eliminación. El ítem desaparecerá permanentemente.**

**Muestra el resultado de la tabla después de haber eliminado uno de los ítems.**
<img src="imagenes\9.png">
<br></br>   

### Reflexión Final: DynamoDB en el Ecosistema NoSQL.
**Para tu informe final, incluye una sección de reflexión respondiendo a estas preguntas:**

1. **Comparativa: ¿Qué diferencias clave notaste entre trabajar con DynamoDB y lo que has visto de MongoDB? (Piensa en la sintaxis de inserción, las consultas, el esquema…).**
Las consultas son mucho más sencillas en Dynamo, simplemente escribes el nombre de la columna y el valor que quieres buscar, a diferencia de Mongo que tienes que escribir el comando entero con su sintaxis propia. Además en Dynamo hay un desplegable para filtar si existe o no, mayor menor o igual etc, no como en Mongo que tienes que saber que $lt es la forma de indicar menor que.
<br></br>

2. **Ventajas Serverless: ¿Qué beneficios crees que aporta un servicio como DynamoDB a un equipo de desarrollo? ¿Y qué inconvenientes podría tener?**
La ventaja principal sería no necesitar un servidor para tener la base de datos ni nadie que se encargue de gestionarlo. Un inconveniente podría ser el hecho de tener que pagar según el tiempo de uso.
<br></br>

3. **Experiencia: ¿Qué te resultó más fácil de esta práctica? ¿Qué fue lo más complicado o confuso?**
Lo más fácil fue el proceso de filtrado. No ha habido nada complicado, era seguir los pasos.