from flask import Flask, jsonify, request
from flask_cors import CORS
import boto3
from boto3.dynamodb.conditions import Attr
from decimal import Decimal

app = Flask(__name__)
CORS(app)

# Conexión a DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

productos_table = dynamodb.Table('Productos')
pedidos_table = dynamodb.Table('Pedidos')

# -------------------------
# Helper: Convertir Decimals
# -------------------------
def convert_decimals(obj):
    if isinstance(obj, list):
        return [convert_decimals(i) for i in obj]
    if isinstance(obj, dict):
        return {k: convert_decimals(v) for k, v in obj.items()}
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    return obj

# -------------------------
# Funciones Productos
# -------------------------

def create_producto(producto_id, producto, precio, stock):
    try:
        productos_table.put_item(Item={
            'producto_id': int(producto_id), # CORREGIDO: convertir a int
            'producto': producto,
            'precio': Decimal(str(precio)),
            'stock': int(stock)
        })
        return True
    except Exception as e:
        print(f"Error creando producto: {e}")
        return False

def get_producto(producto_id):
    try:
        # CORREGIDO: convertir a int
        response = productos_table.get_item(Key={'producto_id': int(producto_id)})
        return convert_decimals(response.get('Item'))
    except Exception as e:
        print(f"Error obteniendo producto {producto_id}: {e}")
        return None

def delete_producto(producto_id):
    try:
        # CORREGIDO: convertir a int para el filtro
        response = pedidos_table.scan(
            FilterExpression=Attr('producto_id').eq(int(producto_id))
        )
        if response.get('Items'):
            print(f"No se puede borrar producto {producto_id}, tiene pedidos asociados.")
            return False, "El producto tiene pedidos asociados"

        # CORREGIDO: convertir a int
        productos_table.delete_item(Key={'producto_id': int(producto_id)})
        return True, "Eliminado correctamente"
    except Exception as e:
        print(f"Error borrando producto {producto_id}: {e}")
        return False, str(e)

# -------------------------
# Funciones Pedidos
# -------------------------

def create_pedido(pedido_id, producto_id, nombre, cantidad):
    producto_item = get_producto(producto_id)
    if not producto_item:
        print(f"Error: Producto {producto_id} no existe.")
        return False, f"El producto {producto_id} no existe."

    try:
        pedidos_table.put_item(Item={
            'pedido_id': int(pedido_id),     # CORREGIDO: convertir a int
            'producto_id': int(producto_id), # CORREGIDO: convertir a int
            'nombre': nombre,
            'cantidad': int(cantidad)
        })
        return True, "Pedido creado"
    except Exception as e:
        print(f"Error creando pedido: {e}")
        return False, str(e)

def get_pedido(pedido_id):
    try:
        # CORREGIDO: convertir a int
        response = pedidos_table.get_item(Key={'pedido_id': int(pedido_id)})
        return convert_decimals(response.get('Item'))
    except Exception as e:
        print(f"Error obteniendo pedido {pedido_id}: {e}")
        return None

def delete_pedido(pedido_id):
    try:
        # CORREGIDO: convertir a int
        pedidos_table.delete_item(Key={'pedido_id': int(pedido_id)})
        return True
    except Exception as e:
        print(f"Error eliminando pedido {pedido_id}: {e}")
        return False

def update_pedido_cantidad(pedido_id, cantidad):
    try:
        # CORREGIDO: convertir a int
        pedidos_table.update_item(
            Key={'pedido_id': int(pedido_id)},
            UpdateExpression="SET cantidad = :c",
            ExpressionAttributeValues={':c': int(cantidad)}
        )
        return True
    except Exception as e:
        print(f"Error actualizando pedido {pedido_id}: {e}")
        return False

def get_pedidos_por_nombre(nombre):
    try:
        response = pedidos_table.scan(
            FilterExpression=Attr('nombre').eq(nombre)
        )
        items = response.get('Items', [])
        return convert_decimals(items)
    except Exception as e:
        print(f"Error buscando pedidos por nombre '{nombre}': {e}")
        return []

# -------------------------
# RUTAS
# -------------------------

@app.route('/productos', methods=['GET', 'POST'])
def api_productos():
    if request.method == 'GET':
        try:
            return jsonify(convert_decimals(productos_table.scan().get('Items', [])))
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    data = request.json
    required_fields = ('producto_id', 'producto', 'precio', 'stock')
    if not all(k in data for k in required_fields):
        return jsonify({'error': f'Faltan campos. Requeridos: {required_fields}'}), 400

    if create_producto(data['producto_id'], data['producto'], data['precio'], data['stock']):
        return jsonify({'message': 'Producto creado'}), 201
    return jsonify({'error': 'No se pudo crear el producto'}), 500

@app.route('/productos/<producto_id>', methods=['GET', 'DELETE'])
def api_producto_individual(producto_id):
    if request.method == 'GET':
        producto = get_producto(producto_id)
        if producto:
            return jsonify(producto)
        return jsonify({'error': 'Producto no encontrado'}), 404

    success, msg = delete_producto(producto_id)
    if success:
        return jsonify({'message': 'Producto eliminado'})
    return jsonify({'error': f'No se puede eliminar: {msg}'}), 400

@app.route('/pedidos', methods=['GET', 'POST'])
def api_pedidos():
    if request.method == 'GET':
        try:
            return jsonify(convert_decimals(pedidos_table.scan().get('Items', [])))
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    data = request.json
    required = ['pedido_id', 'producto_id', 'nombre', 'cantidad']
    if not all(k in data for k in required):
        return jsonify({'error': 'Faltan campos'}), 400

    success, msg = create_pedido(data['pedido_id'], data['producto_id'], data['nombre'], data['cantidad'])
    if success:
        return jsonify({'message': 'Pedido creado'}), 201
    return jsonify({'error': msg}), 400

@app.route('/pedidos/<pedido_id>', methods=['GET', 'PUT', 'DELETE'])
def api_pedido_individual(pedido_id):
    if request.method == 'GET':
        pedido = get_pedido(pedido_id)
        if pedido:
            return jsonify(pedido)
        return jsonify({'error': 'Pedido no encontrado'}), 404

    if request.method == 'PUT':
        data = request.json
        if 'cantidad' not in data:
            return jsonify({'error': 'Falta cantidad'}), 400
        if update_pedido_cantidad(pedido_id, data['cantidad']):
            return jsonify({'message': 'Pedido actualizado'})
        return jsonify({'error': 'Error actualizando'}), 500

    if delete_pedido(pedido_id):
        return jsonify({'message': 'Pedido eliminado'})
    return jsonify({'error': 'Error al eliminar'}), 500

@app.route('/pedidos/nombre/<nombre>', methods=['GET'])
def api_pedidos_por_nombre(nombre):
    import urllib.parse
    return jsonify(get_pedidos_por_nombre(urllib.parse.unquote(nombre)))

if __name__ == '__main__':
    print("Iniciando servidor con correcciones (IDs como int)...")
    app.run(debug=True)