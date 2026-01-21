# Práctica 4: Automatización de DynamoDB con Python y Boto3.

## Parte 1: Preparando el Entorno de Programación.

### 1.1. Instalación de AWS CLI y de boto3.
Nos descargamos la última versión de AWS CLI para Windows.
Una vez instalada tenemos que configurarlo desde el cmd.
```
aws configure
```

Copiamos y pegamos la access key, la secret access key, el token de sesión y el nombre de la región.

<img src="imagenes\1.png">

Ahora instalamos boto3 con este comando:
```
pip install boto3

```

<img src="imagenes\2.png">


### 1.2. Verificación de las credenciales.
Ejecutamos este comando para que boto3 se autentique con nuestras credenciales.
```
aws sts get-caller-identity
```

<img src="imagenes\3.png">


## Parte 2: Automatizando Operaciones con Boto3.
Creamos el archivo dynamodb_operations.py.

### 2.1. Conexión a DynamoDB.
Añadimos estas líneas de códido al archivo.

<img src="imagenes\4.png">


## Ejercicio 1: Crear un Nuevo Pedido.
Para crear nuevos pedidos copio la función create_order. 

<img src="imagenes\5.png">

Llamo a la función añadiendo los datos requeridos y ejecuto el archivo.

<img src="imagenes\6.png">

Compruebo que se ha creado el pedido.

<img src="imagenes\7.png">


## Ejercicio 2: Leer un Pedido.
Para que me devuelva un pedido pongo la función get_order y la llamo con el id del pedido que acabo de crear.

<img src="imagenes\8.png">

Me devuelve los datos del pedido.

<img src="imagenes\9.png">


## Ejercicio 3: Actualizar el Estado de un Pedido.
Utilizo la función update_order_status para cambiar el estado del nuevo pedido de pending a delivered.

<img src="imagenes\10.png">

Se cambia a delivered.

<img src="imagenes\11.png">

Compruebo que ha cambiado.

<img src="imagenes\12.png">


## Ejercicio 4: Eliminar un Pedido.
La función delete_order me permite eliminar un pedido utilizando su order_id.

<img src="imagenes\13.png">

Se elimina el pedido.

<img src="imagenes\14.png">

Ya no existe en la base de datos.

<img src="imagenes\15.png">


## Ejercicio 5: Buscar Pedidos por Cliente.
Para este ejercicio creo la función get_orders_by_customer y le paso el nombre de un cliente para que me devuelva sus pedidos.

<img src="imagenes\16.png">

Me devuelve los pedidos del cliente indicado.

<img src="imagenes\17.png">


## Parte 3: Demostración y Entrega.
Añado el bloque final del fichero para ejecutar todas las funciones.

<img src="imagenes\18.png">

Compruebo que funcionan de forma correcta.

<img src="imagenes\19.png">


## Reflexión final.
1. **Automatización vs. Consola: ¿Qué ventajas claras observas al usar un script de Python en lugar de la consola web de AWS para gestionar los datos? ¿Y qué desventajas?**
La ventaja principal es la sencillez y rapidez para ejecutar las operaciones CRUD. La desventaja sería ser la persona que tiene que crear el script.
<br></br>

2. **SDK como Herramienta: ¿En qué otros escenarios (además de gestionar pedidos) podrías imaginar el uso de Boto3 para automatizar tareas en AWS?**
Puede servir para gestionar cualquier base de datos o gestionar recursos de AWS directamente desde python.
<br></br>

3. **Dificultades y Aprendizajes: ¿Qué parte de la práctica te resultó más desafiante? ¿Cuál fue el concepto más interesante que aprendiste?**
La parte más desafiante fue crear la función para buscar los pedidos de un cliente, ya que es la única función que no venía hecha. 
La más interesante fue instalar AWS CLI y usar boto3 para conectarme con AWS y cambiar la base de datos desde el script de mi ordenador.