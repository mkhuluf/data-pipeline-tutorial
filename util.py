import psycopg2
import pandas as pd
from mysql import connector as mc
from mysql.connector import errorcode as ec
from config import DB_DETAILS


def load_db_details(env):
    return DB_DETAILS[env]

def get_connection(db_type, db_host, db_name, db_user, db_pass):
    connection = None
    if db_type == 'mysql':
        try:
            connection = mc.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
        except mc.Error as error:
            if error.errno == ec.ER_ACCESS_DENIED_ERROR:
                print("Invalid Credentials")
            else:
                print(error)
    if db_type == 'postgres':
        connection = psycopg2.connect(user=db_user, password=db_pass, host=db_host, database=db_name)

    return connection


def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_loaded == "yes"')