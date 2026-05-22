import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()


conexao  = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
)


if conexao.is_connected():
    db_info = conexao.get_server_info()

    cursor = conexao.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()


    cursor.close()
    conexao.close()
    print('Conexão encerrado')

else:
    print("Erro ao conectar ")
