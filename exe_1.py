import mysql.connector
from dotenv import load_dotenv
import os

def testar_ConexaoDb():
    load_dotenv()


    conexao  = mysql.connector.connect(
        host     = os.getenv("DB_HOST"),
        user     = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME")
    )


    if conexao.is_connected():
        print('Conectado ao banco de Dados')
    else:
        print("Erro ao conectar ")

def cabecalho():
    #Limpar o terminal mais apresentavel
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("       🗄️  BANCO DE DADOS - USUÁRIOS")
    print("=" * 50)
    print()
    print("   Seja bem-vindo ao sistema de gerenciamento!")
    print()
    print("   O que deseja fazer?")
    print()
    print("   [1]  ➕  Adicionar usuário")
    print("   [2]  🗑️   Remover usuário")
    print("   [3]  ✏️   Editar usuário")
    print("   [0]  🚪  Sair")
    print()
    print("=" * 50)
cabecalho()


opcao = input("   Opção: ")