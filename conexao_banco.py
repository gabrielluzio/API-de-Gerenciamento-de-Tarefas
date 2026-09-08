import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class ConectarBanco:
    def __init__(self):
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=os.getenv('MYSQL_HOST'),
                user=os.getenv('MYSQL_USER'),
                password=os.getenv('MYSQL_PASSWORD'),
                database=os.getenv('MYSQL_NAME')
            )
            self.cursor = self.conexao.cursor()
            print('Banco conectado!')
        except mysql.connector.Error as erro:
            print(f'Erro ao conectar: {erro}')
            raise


    def fechar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
