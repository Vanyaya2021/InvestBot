import psycopg2
from Configurations import config
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def connect_to_db():
    try:
        conn = psycopg2.connect(dbname=config.dbName, user=config.dbUser,
                        password=config.dbPassword, host=config.dbhost)
        return conn
    except:
        print(Exception)

def update_db(conn, sql = None):
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

def query(sql):
    conn = connect_to_db()
    try:
        records = update_db(conn,sql)
        return records
    except psycopg2.Error as e:
        logging.exception(e.pgerror)
        return None