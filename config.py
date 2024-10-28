import os

# Configuración de la cadena de conexión usando variables de entorno
SERVER = os.getenv('DB_SERVER', 'appweb-crud-db-server.database.windows.net')
DATABASE = os.getenv('DB_DATABASE', 'WebApp-Crud-db')
USERNAME = os.getenv('DB_USERNAME', 'crud_paas')
PASSWORD = os.getenv('DB_PASSWORD', 'U12345678-')
DRIVER = os.getenv('DB_DRIVER', 'ODBC Driver 18 for SQL Server')

# Cadena de conexión
connectionString = f'DRIVER={{{DRIVER}}};SERVER={SERVER};PORT=1433;DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
