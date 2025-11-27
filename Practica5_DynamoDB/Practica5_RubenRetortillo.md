# Practica 5. Operaciones CRUD en DynamoDB.
## 1. Diseño y creación de la tabla.
Creamos la tabla SensoresEcoCity con los atributos id_sensor, que será la clave primaria, y timestamp, la sort key.

Utilizo este comando para crear la tabla.
<code>aws dynamodb create-table \
    --table-name SensoresEcoCity \
    --attribute-definitions \
        AttributeName=id_sensor,AttributeType=S \
        AttributeName=timestamp,AttributeType=S \
    --key-schema \
        AttributeName=id_sensor,KeyType=HASH \
        AttributeName=timestamp,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST</code>

<img src="imagenes\1.png">

Compruebo que ha sido creada.
<img src="imagenes\2.png">


## 2. Ingesta de datos (Create).
Al añadir los datos hay que añadir los demás atributos medicion, valor y estado.

Ejemplo de comando:
<code>aws dynamodb put-item \
    --table-name SensoresEcoCity \
    --item '{
        "id_sensor": {"S": "SENSOR-ZONA-Norte-01"},
        "timestamp": {"S": "2025-11-18T15:00:00"},
        "medicion": {"S": "Temperatura"},
        "valor": {"N": "20"},
        "estado": {"S": "OK"}
      }'</code>

Todos los datos. 
<img src="imagenes\3.png">


## 3. Consulta de datos (Read - Query)
Consulto los datos del sensor SENSOR-ZONA-Norte-01 con este comando.

<code>aws dynamodb query \
    --table-name SensoresEcoCity \
    --key-condition-expression "id_sensor = :SENSOR" \
    --expression-attribute-values '{ ":SENSOR": {"S": "SENSOR-ZONA-Norte-01"} }'</code>

Al ejecutar el comando nos muestra los datos del SENSOR-ZONA-Norte-01.
<img src="imagenes\4.png">


## 4. Actualización de datos (Update)
Actualizo la medición del sensor zona norte de las 20:00. Cambio estado a mantenimiento y añado una nota que ponga recalibrado por técnico.

<img src="imagenes\5.png">


<code>aws dynamodb update-item \
  --table-name SensoresEcoCity \
  --key '{
        "id_sensor": {"S": "SENSOR-ZONA-Norte-01"},
        "timestamp": {"S": "2025-11-18T20:00:00"}
    }' \
  --update-expression "SET nota = :n, estado = :e" \
  --expression-attribute-values '{
        ":n": {"S": "Recalibrado por técnico"},
        ":e": {"S": "Mantenimiento"}
    }' \
  --return-values UPDATED_NEW</code>

<img src="imagenes\6.png">

Compruebo que se ha actualizado.
<img src="imagenes\7.png">


## 5. Eliminación de datos (Delete)
Elimino la medición del sensor actualiza en el ejercicio anterior.

<code>aws dynamodb delete-item \
    --table-name SensoresEcoCity \
    --key '{
        "id_sensor": {"S": "SENSOR-ZONA-Norte-01"},
        "timestamp": {"S": "2025-11-18T20:00:00"}
    }'</code>

<img src="imagenes\8.png">

Se ha eliminado de la tabla.
<img src="imagenes\9.png">


Reflexión sobre la idoneidad de DynamoDB para datos de IoT (Internet of Things):
Yo creo que DynamoDb es una buena opción pare IoT ya que permite almacenar una gran cantidad de datos de distintos dispositivos y permite tener la escalabilidad necesaria.