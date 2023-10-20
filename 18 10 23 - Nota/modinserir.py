from cnindex import conectar
import mysql.connector
from tkinter import messagebox

def inserir(pdt, name, ori, dest, fpgmt):
    conexao, cursor = conectar()
    try:
        sql = f"""INSERT INTO tb_dados(pdata, nome_cliente, origem, destino, forma_pagamento) VALUES ('{pdt}' , '{name}', 
        '{ori}', '{dest}', '{fpgmt}')
        """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo('Cadastrado', 'Cadastrado com sucesso!')
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror('Falha', 'Falha ao cadastrar: '+str(falha))
        return True

    finally:
        conexao.close()
        cursor.close()
inserir('2023-10-19', 'jOCA', 'recife', 'joao pesoa', 'Pix')

