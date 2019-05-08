import psycopg2
import sqlalchemy as db
from sqlalchemy import create_engine

def connector(host, dbname, user, password):
    """
    :param host: 
    :param dbname: 
    :param user: 
    :param password: 
    :return: 
    """
    conn_string = f"host= {host} dbname={dbname} user= {user} password = {password}"
    connection = psycopg2.connect(conn_string)
    return connection 

def engine(dialect, driver, name, password, host):
    """
    :param dialect:
    :param driver:
    :param name:
    :param password:
    :param host:
    :return:
    """
    engine = create_engine(dialect+driver+'://'+name+':'+password+'@'+host)
    return engine

def explore_tables(eng):
    """
    :param eng: Instance of db engine
    :return None:
    """
    print(eng.table_names())
    return None

def table_dump_view(eng, table_name):
    """
    :param eng: 
    :param table_name: 
    :return: 
    """
    query = 'SELECT * FROM '+ table_name
    results = eng.execute(query).fetchall()
    for each in results: 
        print(each)
    
