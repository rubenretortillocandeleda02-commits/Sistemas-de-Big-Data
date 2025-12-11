
import boto3

# 1. Crear un recurso de servicio de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# 2. Seleccionar la tabla 'Pedidos'
table = dynamodb.Table('Pedidos')

# 3. Imprimir un mensaje de confirmación
print(f"Conectado a la tabla '{table.name}' en la región '{dynamodb.meta.client.meta.region_name}'.")

# Función para crear pedidos.
def create_pedido(pedido_id, producto_id, nombre, cantidad):
    '''Crea un nuevo ítem en la tabla Pedidos.'''
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
        print(f"Error al crear el pedido {pedido_id}:  {e}")



import csv

def cargar_pedidos_desde_csv(ruta_csv):
    """Lee un CSV y crea pedidos en DynamoDB usando create_pedido."""
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)  # Cada fila será un diccionario
            for row in reader:
                # Llamamos a tu función para crear el pedido
                create_pedido(
                    pedido_id=int(row['pedido_id']),
                    producto_id=int(row['producto_id']),
                    nombre=row['nombre'],
                    cantidad=int(row['cantidad'])
                )

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_csv}")
    except Exception as e:
        print(f"Error leyendo el CSV: {e}")

# Ejemplo de uso
ruta = "ruta csv"
cargar_pedidos_desde_csv(ruta)