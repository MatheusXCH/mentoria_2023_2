import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from classes.database_info import DatabaseInfo
from utils.instancias import INSTANCIA_GERENCIADA, INSTANCIA_VM

db_info = DatabaseInfo(**INSTANCIA_VM)
db_info.connect()
# Crie o engine do SQLAlchemy
engine = db_info.engine

print(engine)

# Crie uma conexão e um cursor
connection = engine.raw_connection()
cursor = connection.cursor(pymysql.cursors.DictCursor)

# Execute um comando SQL para matar todas as conexões
sql = "SHOW FULL PROCESSLIST"
cursor.execute(sql)

# Obtenha os resultados e emita o comando KILL para cada conexão
results = cursor.fetchall()
for row in results:
    print(row)
    connection_id = row[0]
    kill_sql = f"KILL {connection_id}"
    cursor.execute(kill_sql)

# Feche o cursor e a conexão
cursor.close()
connection.close()
