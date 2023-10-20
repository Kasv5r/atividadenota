from cnindex import conectar
import mysql.connector
from tkinter import messagebox

def atualizarCadastro(id, pdt, name, ori, dest, pgmt):
    conexao, cursor = conectar()
    try:
        sql = f"UPDATE tb_dados SET pdata='{pdt}', nome_cliente='{name}', origem='{ori}', destino='{dest}', forma_pagamento='{pgmt}' WHERE id='{id}'"
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar", "Cadastro atualizado!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao atualizar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()

atualizarCadastro(6, '2023-12-12', 'Joca', 'Recife', 'Rio', 'Pix')