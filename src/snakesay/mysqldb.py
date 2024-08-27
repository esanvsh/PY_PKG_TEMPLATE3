from sqlalchemy import create_engine
from sqlalchemy import text

def conn_setup(USERNAME,PASSWORD,MYSQLIP,MYSQLPORT):
    mysql_conn_str = "mysql+pymysql://"+USERNAME+":"+PASSWORD+"@"+MYSQLIP+":"+MYSQLPORT+"/test"
    engine = create_engine(mysql_conn_str)
    connection = engine.connect()
    p = connection.execute(text('SHOW DATABASES'))
    available_tables = p.fetchall()
    print(available_tables)
    return engine, connection

def sql_cmd(connection, sqlcmd):
    q = connection.execute(text(sqlcmd))
    connection.commit()
    print("ID of Row Added  = ",q.lastrowid)
    return q, q.lastrowid

