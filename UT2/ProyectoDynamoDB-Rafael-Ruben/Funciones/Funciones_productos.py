import boto3

# 1. Crear un recurso de servicio de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# 2. Seleccionar la tabla 'Productos'
table = dynamodb.Table('Productos')

# 3. Imprimir un mensaje de confirmación
print(f"Conectado a la tabla '{table.name}' en la región '{dynamodb.meta.client.meta.region_name}'.")

# Función para crear productos.
def create_producto(producto_id, producto, precio, stock):
    '''Crea un nuevo ítem en la tabla Productos.'''
    try:
        response = table.put_item(
           Item={
                'producto_id': producto_id,
                'producto': producto,
                'precio': precio,
                'stock': stock
            }
        )
        print(f"Producto {producto_id} creado exitosamente.")
        return response
    except Exception as e:
        print(f"Error al crear el producto {producto_id}:  {e}")

# Función para leer un producto.
def get_producto(producto_id):
    '''Obtiene un ítem de la tabla Productos por su ID.'''
    try:
        response = table.get_item(Key={'producto_id': producto_id})
        item = response.get('Item')
        if item:
            print(f"Datos del prodcuto {producto_id}: {item}")
            return item
        else:
            print(f"No se encontró el producto con ID {producto_id}.")
            return None
    except Exception as e:
        print(f"Error al obtener el producto {producto_id}: {e}")


# Función para modificar el precio de un producto.
def update_producto_precio(producto_id, nuevo_precio):
    '''Actualiza el atributo 'precio' de un producto.'''
    try:
        response = table.update_item(
            Key={'producto_id': producto_id},
            UpdateExpression="set precio = :precio",
            ExpressionAttributeValues={':precio': float(nuevo_precio)},
            ReturnValues="UPDATED_NEW"
        )
        print(f"Precio del producto {producto_id} actualizado a '{nuevo_precio}'.")
        return response
    except Exception as e:
        print(f"Error al actualizar el producto {producto_id}: {e}")

# Función para modificar el stock de un producto.

import csv

def cargar_productos_desde_csv(ruta_csv):
    """Lee un CSV y crea productos en DynamoDB usando create_producto."""
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)  # Cada fila será un diccionario
            for row in reader:
                # Llamamos a tu función para crear el producto
                create_producto(
                    producto_id=row['producto_id'],
                    producto=row['producto'],
                    precio=int(row['precio']),  # Convertimos a entero si hace falta
                    stock=int(row['stock'])
                )
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_csv}")
    except Exception as e:
        print(f"Error leyendo el CSV: {e}")

# Ejemplo de uso
ruta = 'ruta/a/tu/archivo/productos.csv'
cargar_productos_desde_csv(ruta)


# Función para borrar productos.
def delete_producto(producto_id):
    '''Elimina un item de la tabla Productos.'''
    try:
        response = table.delete_item(Key={'producto_id': producto_id})
        print(f"Producto {producto_id} eliminado exitosamente.")
        return response
    except Exception as e:
        print(f"Error al eliminar el prodcuto {producto_id}: {e}")


if __name__ == "__main__":
    print("--- Demostración de operaciones con DynamoDB ---")

    # 1. Crear un nuevo pedido
    create_producto("", "", "", )

    # 2. Leer el pedido recién creado
    get_producto("UHF2932")

    # 3. Actualizar su precio.
    update_producto_precio("UHF2932", "Delivered")
    get_producto("UHF2932") # Verificamos el cambio

    # 4. Actualizar su stock.
    update_producto_stock("UHF2932", "Delivered")
    get_producto("UHF2932") # Verificamos el cambio

    # 5. Eliminar el pedido
    delete_producto("UHF2932")
    get_producto("UHF2932") # Verificamos que ya no existe

    print("\n--- Demostración finalizada ---")
