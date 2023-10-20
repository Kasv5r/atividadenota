import mysql.connector
from tkinter import messagebox
import datetime

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="db_atividade"
        )
        cursor = conexao.cursor()
        print("Conectado com sucesso ao BANCO DE DADOS")
        return conexao, cursor
    except mysql.connector.Error as falha:
        messagebox.showerror(
            "Erro", "Falha na conexão com BANCO DE DADOS"+str(falha))
        return None, None

# Função para converter data para o formato de banco de dados
def converterData(dataString): 
   minhaData = datetime.datetime.strptime(dataString, "%d/%m/%Y")
   dataFormatada = minhaData.date().isoformat()
   return dataFormatada