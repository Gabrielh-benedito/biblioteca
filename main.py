# Sistema de Biblioteca em SQLite
import sqlite3

def criar_tabela():
    try:
        #Criando uma conexao chamada "biblioteca.db"
        conexao = sqlite3.connect("bibioteca.db")
        #Utilizando curso para execultar comandos SQL
        cursor = conexao.cursor()
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS livros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor INTEGER,
                ano INTEGER,
                disponivel TEXT                      
            )
            """)

    except Exception as erro:
        print(f"erro ao tentar adicionar um livro {erro}")
    finally:
        if conexao:
            conexao.close()

criar_tabela()