# Configuración de la cadena de conexión
SERVER = 'appweb-crud-db-server.database.windows.net'
DATABASE = 'WebApp-Crud-db'
USERNAME = 'crud_paas'
PASSWORD = 'U12345678-'
DRIVER = 'ODBC Driver 18 for SQL Server'

#connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
connectionString = 'DRIVER='+DRIVER+';SERVER='+SERVER+';PORT=1433;DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+PASSWORD