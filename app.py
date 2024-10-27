
from flask import Flask, request, jsonify
import pyodbc
import config

app = Flask(__name__)

# Función para crear la tabla 'items' si no existe
def create_items_table():
    conn = None
    try:
        conn = pyodbc.connect(config.connectionString)
        cursor = conn.cursor()
        # Comando SQL para crear la tabla 'items' si no existe
        cursor.execute('''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='items' AND xtype='U')
        CREATE TABLE items (
            id INT PRIMARY KEY IDENTITY(1,1),
            name NVARCHAR(100) NOT NULL
        );
        ''')
        conn.commit()
        print("Tabla 'items' creada o ya existe.")
    except Exception as e:
        print(f'Error al crear la tabla: {e}')
    finally:
        if conn:
            conn.close()

# Ejecutamos la creación de la tabla
#create_items_table()

# Ruta para crear un nuevo item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    name = data['name']
    conn = None  # Inicializamos 'conn' fuera del bloque try

    try:
        conn = pyodbc.connect(config.connectionString)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (name) VALUES (?)", name)
        conn.commit()
        return jsonify({'message': 'Item creado!'}), 201
    except pyodbc.Error as e:
        return jsonify({'error': 'Error de conexión o de ejecución SQL', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'Otro error ocurrió', 'details': str(e)}), 500
    finally:
        if conn is not None:
            try:
                conn.close()
            except Exception as e:
                print(f'Error al cerrar la conexión: {e}')

# Ruta para obtener todos los items
@app.route('/items', methods=['GET'])
def get_items():
    conn = None  # Inicializamos 'conn' fuera del bloque try
    try:
        conn = pyodbc.connect(config.connectionString)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        items = [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]
        return jsonify(items), 200
    except pyodbc.Error as e:
        return jsonify({'error': 'Error de conexión o de ejecución SQL', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'Otro error ocurrió', 'details': str(e)}), 500
    finally:
        if conn is not None:
            try:
                conn.close()
            except Exception as e:
                print(f'Error al cerrar la conexión: {e}')

if __name__ == '__main__':
    app.run(debug=True)
