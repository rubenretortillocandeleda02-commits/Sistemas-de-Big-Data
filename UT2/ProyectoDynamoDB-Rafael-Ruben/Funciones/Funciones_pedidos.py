import boto3

# 1. Crear un recurso de servicio de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# 2. Seleccionar la tabla 'Pedidos'
table = dynamodb.Table('Pedidos')

# 3. Imprimir un mensaje de confirmación
print(f"Conectado a la tabla '{table.name}' en la región '{dynamodb.meta.client.meta.region_name}'.")

# Función para crear pedidos.
def create_pedido(pedido_id, producto_id, nombre, cantidad):
    '''Crea un nuevo ítem en la tabla Productos.'''
    try:
        response = table.put_item(
           Item={
                'pedido_id': pedido_id,
                'producto_id': producto_id,
                'nombre': nombre,
                'cantidad': cantidad
            }
        )
        print(f"Pedido {pedido_id} creado exitosamente.")
        return response
    except Exception as e:
        print(f"Error al crear el pedido {pedido_id}: {e}")

import csv

def cargar_pedidos_desde_csv(ruta_csv):
    """Lee un CSV y crea pedidos en DynamoDB usando create_pedidos."""
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)  # Cada fila será un diccionario
            for row in reader:
                # Llamamos a tu función para crear el pedido
                create_pedido(
                    producto_id=row['pedido_id'],
                    producto_id=row['producto_id'],
                    nombre=int(row['nombre']),  # Convertimos a entero si hace falta
                    cantidad=int(row['cantidad'])
                )
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_csv}")
    except Exception as e:
        print(f"Error leyendo el CSV: {e}")

# Ejemplo de uso
ruta = 'ruta/a/tu/archivo/productos.csv'
cargar_pedidos_desde_csv(ruta)

# Función para leer un pedido.
def get_pedido(pedido_id):
    '''Obtiene un ítem de la tabla Productos por su ID.'''
    try:
        response = table.get_item(Key={'pedido_id': pedido_id})
        item = response.get('Item')
        if item:
            print(f"Datos del pedido {pedido_id}: {item}")
            return item
        else:
            print(f"No se encontró el pedido con ID {pedido_id}.")
            return None
    except Exception as e:
        print(f"Error al obtener el pedido {pedido_id}: {e}")


# Función para modificar la cantidad de un pedido.
def update_pedido_cantidad(pedido_id, nueva_cantidad):
    '''Actualiza el atributo 'cantidad' de un pedido.'''
    try:
        response = table.update_item(
            Key={'producto_id': pedido_id},
            UpdateExpression="set precio = :precio",
            ExpressionAttributeValues={':precio': float(nueva_cantidad)},
            ReturnValues="UPDATED_NEW"
        )
        print(f"Cantidad del pedido {pedido_id} actualizado a '{nueva_cantidad}'.")
        return response
    except Exception as e:
        print(f"Error al actualizar el pedido {pedido_id}: {e}")

# Función para borrar pedidos.
def delete_pedido(pedido_id):
    '''Elimina un item de la tabla Pedidos.'''
    try:
        response = table.delete_item(Key={'pedido_id': pedido_id})
        print(f"Pedido {pedido_id} eliminado exitosamente.")
        return response
    except Exception as e:
        print(f"Error al eliminar el pedido {pedido_id}: {e}")


# Función para buscar los pedidos de un cliente.
def get_pedido_by_nombre(nombre):
    """Devuelve todos los pedidos realizados por un cliente concreto."""
    from boto3.dynamodb.conditions import Attr
    pedidos_table = dynamodb.Table('Pedidos')

    response = pedidos_table.scan(
    FilterExpression=Attr('nombre').eq(nombre)
    )

    print(f"Pedidos de {nombre}:")
    for item in response.get('Items', []):
        print(item)


if __name__ == "__main__":
    print("--- Demostración de operaciones con DynamoDB ---")

    # 1. Leer el pedido recién creado
    get_pedido("UHF2932")

    # 2. Actualizar su cantidad.
    update_pedido_cantidad("UHF2932", "Delivered")
    get_pedido("UHF2932") # Verificamos el cambio

    # 3. Buscar todos los pedidos de un cliente (usa un nombre que exista en tu tabla)
    get_pedido_by_nombre("María Gómez")

    # 4. Eliminar el pedido
    delete_pedido("UHF2932")
    get_pedido("UHF2932") # Verificamos que ya no existe

    print("\n--- Demostración finalizada ---")