# Práctica 1: Gestión de un Catálogo de Productos con MongoDB.

Antes de empezar con los ejercicios creamos la colección *productos*.
<img src="1.png">

E insertamos varios json con el comando:

```
db.productos.insertOne()
```

Ejemplo:
<img src="2.png">

Una vez insertados varios json empezamos con los ejercicios.

### Ejercicio 1: Encontrar portátiles de una marca con más de 8GB de RAM.
**Se desea obtener todos los productos cuya categoría sea “Portátiles”, que pertenezcan a la marca TecnoÁgora Devices y cuya memoria RAM sea superior a 8GB.**

Utilizamos este comando para realizar este ejercicio:
```
db.productos.find({"categoria" : "Portátiles", "especificaciones.ram": {$gt: 8}, "marca" : "TecnoÁgora Devices"})
```

<img src="3.png">

### Ejercicio 2: Buscar productos con la etiqueta “oferta”.
**Los arreglos en MongoDB permiten búsquedas directas sobre sus valores. Se desea encontrar todos los documentos que contengan la palabra “oferta” dentro del campo tags.**

```
db.productos.find({"tags" : "oferta"})
```

<img src="4.png">

### Ejercicio 3: Incrementar el stock de un producto en 10 unidades.
**En ocasiones es necesario actualizar el valor de un campo numérico. Se desea incrementar el stock de un producto específico (por ejemplo, “Portátil Pro-Book X1”) en 10 unidades.**

Aumentamos el stock con este comando:

```
db.productos.updateOne({"_id" : "SKU-001"}, {$inc: { stock: 10 }})
```

<img src="5.png">

Comprobamos que a aumentado:
<img src="6.png">

### Ejercicio 4: Añadir una nueva reseña (review) a un producto.
**Se desea agregar una nueva reseña a un producto existente (por ejemplo, “Portátil Pro-Book X1”). La reseña debe contener el nombre del usuario, una puntuación y un comentario.**

Agregamos la reseña con este comando:

```
db.productos.updateOne({"nombre" : "Portátil Pro-Book X1"}, {$push: {reviews: {"usuario" : "RubenR", "puntuacion" : "8", "comentario" : "Muy bueno"}}})
```

<img src="7.png">\
<img src = "8.png">


### Ejercicios adicionales.
**1. Mostrar productos con bajo stock. Se desea mostrar todos los productos con menos de 5 unidades disponibles.**

```
db.productos.find({"stock" : {$lt : 5}})
```

<img src="9.png">
<br></br>

**2. Proyección de campos específicos. Se desea mostrar únicamente el nombre y el precio de todos los productos.**

```
db.productos.find({}, {nombre : 1, precio : 1, _id : 0})
```

<img src="10.png">
<br></br>

**3. Eliminar un producto por su identificador. Se desea borrar un documento concreto de la colección, por ejemplo, el producto con _id: “SKU-001”.**

```
db.productos.deleteOne({"_id" : "SKU-001"})
```

<img src="11.png">\
<img src="12.png">
