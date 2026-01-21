# Práctica 2: Introducción a Neo4j y Modelado de Redes Sociales.

### Ejercicio 1: Diseño del Modelo de Datos de la Red Social.
**Diseña un modelo de datos de grafo para representar usuarios y sus interacciones en una red social. Considera los siguientes tipos de nodos y relaciones:**

**Nodos:
 · User: Con propiedades como username, name, registration_date.
 · Post: Con propiedades como content, timestamp.
Relaciones:
 · FOLLOWS: Entre User y User.
 · POSTED: Entre User y Post.
 · LIKES: Entre User y Post.**

**Dibuja o describe el esquema de tu grafo, mostrando los tipos de nodos, sus propiedades, los tipos de relaciones y sus propiedades.**



### Ejercicio 2: Creación de Nodos y Relaciones Iniciales.
**Utiliza Cypher para crear los siguientes nodos y relaciones en tu base de datos.**

1. **Crear algunos nodos User: Crea al menos tres nodos de tipo User con las propiedades username, name y registration_date. Asegúrate de que los username sean únicos.**
Usuarios:
```
CREATE (:User {username: 'RubenRC', name: 'Ruben', registration_date: 2025-2-15})
CREATE (:User {username: 'Juanceto', name: 'Juan', registration_date: 2024-12-20})
CREATE (:User {username: 'Jordan_Michael', name: 'Michael', registration_date: 2025-6-2})
CREATE (:User {username: 'xxDavidxx', name: 'David', registration_date: 2025-1-30})
```
<img src="imagenes\6.png">
<br></br>

2. **Crear relaciones FOLLOWS: Crea algunas relaciones de tipo FOLLOWS entre tus usuarios (por ejemplo, Alice sigue a Bob, Bob sigue a Charlie).**
Follows:
```
CREATE (:User {username: 'Juanceto', name: 'Juan', registration_date: 2024-12-20})-[:FOLLOWS]->(:User {username: 'Jordan_Michael', name: 'Michael', registration_date: 2025-6-2})
CREATE (:User {username: 'Juanceto', name: 'Juan', registration_date: 2024-12-20})-[:FOLLOWS]->(:User {username: 'xxDavidxx', name: 'David', registration_date: 2025-1-30})
CREATE (:User {username: 'xxDavidxx', name: 'David', registration_date: 2025-1-30})-[:FOLLOWS]->(:User {username: 'Jordan_Michael', name: 'Michael', registration_date: 2025-6-2})
```
<img src="imagenes\7.png">
<br></br>

3. **Crear algunos Post y relaciones POSTED: Haz que al menos dos de tus usuarios publiquen un Post. Cada Post debe tener content y timestamp.**
Posts:
```
CREATE (:Post {content: "Foto de la familia", timestamp: "14:25:10"})
CREATE (:Post {content: "Foto de Segovia", timestamp: "17:40:53"})
CREATE (:Post {content: "Tweet de fútbol", timestamp: "22:10:04"})
```
<img src="imagenes\8.png">
<br></br>

Posted:
```
CREATE (:User {username: 'Jordan_Michael', name: 'Michael', registration_date: 2025-6-2})-[:POSTED]->(:Post {content: "Foto de la familia", timestamp: "14:25:10"})
CREATE (:User {username: 'Jordan_Michael', name: 'Michael', registration_date: 2025-6-2})-[:POSTED]->(:Post {content: "Foto de Segovia", timestamp: "17:40:53"})
CREATE (:User {username: 'xxDavidxx', name: 'David', registration_date: 2025-1-30})-[:POSTED]->(:Post {content: "Tweet de fútbol", timestamp: "22:10:04"})
```
<img src="imagenes\9.png">
<br></br>

4. **Crear relaciones LIKES: Haz que un usuario dé “Like” a un post de otro usuario.**
Liked:
```
CREATE (:User {username: 'Juanceto', name: 'Juan', registration_date: 2024-12-20})-[:LIKED]->(:Post {content: "Tweet de fútbol", timestamp: "22:10:04"})
CREATE (:User {username: 'Juanceto', name: 'Juan', registration_date: 2024-12-20})-[:LIKED]->(:Post {content: "Foto de la familia", timestamp: "14:25:10"})
CREATE (:User {username: 'RubenRC', name: 'Ruben', registration_date: 2025-2-15})-[:LIKED]->(:Post {content: "Foto de Segovia", timestamp: "17:40:53"})
```
<img src="imagenes\10.png">
<br></br>

### Ejercicio 3: Encontrar Amigos y Seguidores.

1. **Encontrar todos los usuarios que un usuario específico sigue: Escribe una consulta Cypher para encontrar todos los usuarios que  cualquier usuario que hayas creado sigue.**
```
MATCH (a:User {name: 'Juan'})-[:FOLLOWS]->(b:User) RETURN a.name, b.name
```
<img src="imagenes\1.png">
<br></br>

2. **Encontrar todos los usuarios que siguen a un usuario específico: Escribe una consulta Cypher para encontrar todos los usuarios que siguen a cualquier usuario que hayas creado.**
```
MATCH (a:User)-[:FOLLOWS]->(b:User {name: 'Michael'}) RETURN a.name, b.name
```
<img src="imagenes\2.png">
<br></br>

### Ejercicio 4: Analizando posts e interacciones.

1. **Encontrar todos los posts de un usuario específico: Escribe una consulta Cypher para encontrar todos los posts de cualquier usuario que hayas creado, mostrando el contenido y la fecha/hora.**
```
MATCH (a:User {name: 'Michael'})-[:POSTED]->(b:Post) RETURN a.name, b.content, b.timestamp
```
<img src="imagenes\3.png">
<br></br>

2. **Encontrar los posts que un usuario ha dado “Like”: Escribe una consulta Cypher para encontrar los posts a los que cualquier usuario que hayas creado ha dado “Like”, mostrando el contenido del post.**
```
MATCH (a:User {name: 'Juan'})-[:LIKED]->(b:Post) RETURN a.name, b.content
```
<img src="imagenes\4.png">
<br></br>

### Ejercicio 5: Explorando el Grafo Visualmente.
1. **Ejecuta algunas de tus consultas anteriores en el Neo4j Browser.**
2. **Experimenta con las opciones de visualización:**
- **Arrastra nodos para reorganizar el grafo.**
- **Haz doble clic en un nodo para expandir sus relaciones.**
- **Usa el panel de estilos para cambiar colores y tamaños de nodos/relaciones.**

**Realiza una captura de pantalla de una visualización interesante de tu red social.**
<img src="imagenes\5.png">