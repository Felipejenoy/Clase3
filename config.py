# Configuración de la cadena de conexión
SERVER = 'appweb-crud-db-server.database.windows.net'  # Nombre del servidor
DATABASE = 'WebApp-Crud-db'                             # Nombre de la base de datos
USERNAME = 'crud_paas'                                  # Nombre de usuario
PASSWORD = 'U12345678-'                                 # Contraseña
DRIVER = 'ODBC Driver 18 for SQL Server'                # Controlador ODBC

# Cadena de conexión
connectionString = f'DRIVER={DRIVER};SERVER={SERVER};PORT=1433;DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
