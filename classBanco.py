import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

class Banco():
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.name = os.getenv("DB_NAME")
        self.ssl = os.getenv("DB_SSL")


    def conectar(self):
        return psycopg.connect(
            host= self.host,
            port= self.port,
            user= self.user,
            password= self.password,
            dbname= self.name,
            sslmode= self.ssl
        )
    

    def consultar(self, sql, parametros=()):
        conexao = None
        cursor = None

        try:
            conexao = self.conectar()
            cursor = conexao.cursor()

            cursor.execute(sql, parametros)

            return cursor.fetchall()

        except Exception as error:
            print("ERRO ENCONTRADO!", error)
            

        finally:
            if conexao is not None:
                conexao.close()


    def manipular(self, sql, parametros=()):
        conexao = None
        cursor = None
        
        try:
            conexao = self.conectar()
            cursor = conexao.cursor()
        
            cursor.execute(sql, parametros)
        
            return conexao.commit()
        
        except Exception as error:
            print("ERRO ENCONTRADO!", error)
        
        finally:
            if conexao is not None:
                conexao.close()