import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        load_dotenv()
        conn = psycopg2.connect(
            dbname=os.getenv("DBNAME", "name"),
            user=os.getenv("DBUSER", "user"),
            password=os.getenv("DBPASSWORD", "password"),
            host=os.getenv("DBHOST", "host"),
            port=os.getenv("DBPORT", "port")
        )
        print("Conexão realizada!")
        conn.close()

    except Exception as e:
        print("Erro ao conectar.")
        print(e)
        
    