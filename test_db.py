import pyodbc

server = 'cms-server-anmol.database.windows.net'
database = 'cmsdatabase'
username = 'cmsadmin'
password = 'Cms@12345'

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=tcp:cms-server-anmol.database.windows.net,1433;"
    "DATABASE=cmsdatabase;"
    "UID=cmsadmin;"
    "PWD=Cms@12345;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    print("SUCCESS: Connected to Azure SQL")
    print(row)
except Exception as e:
    print("Connection Failed")
    print(e)