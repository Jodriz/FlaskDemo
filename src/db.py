from pymysql import Connection

class MySQLConnection:    
    def __init__(self, c:Connection):
        self.connection = c
        
# Conexión a base de datos Mysql  
# Puede opcionalmente cambiar los valores a una base de datos local 
# y restaurar con el backup que se encuenta en el 
# folder "database" de este proyecto

"""HOST = "db4free.net"
PORT = 3306
USER = "user_remote_test"
PASSWORD = "password_remote_test"
DB = 'db_remote_test'
"""

# Configuración local
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = ''
DB = 'tarea'


mysql = Connection(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DB)
mysql = MySQLConnection(mysql)

