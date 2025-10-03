# Sistema de Biblioteca em SQLite
import sqlite3

# def criar_tabela():
#     try:
#         #Criando uma conexao chamada "biblioteca.db"
#         conexao = sqlite3.connect("biblioteca.db")
#         #Utilizando curso para execultar comandos SQL
#         cursor = conexao.cursor()
#         cursor.execute("""  
#             CREATE TABLE IF NOT EXISTS livros(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 titulo TEXT NOT NULL,
#                 autor INTEGER,
#                 ano INTEGER,
#                 disponivel TEXT                      
#             )
#             """)

#     except Exception as erro:
#         print(f"erro ao tentar criar a tabela {erro}")
#     finally:
#         if conexao:
#             conexao.close()

# criar_tabela()

# def cadastrar_livros(titulo,autor,ano):
#     try: 
#         conexao = sqlite3.connect("biblioteca.db")
#         cursor = conexao.cursor()

#         cursor.execute("""
#             INSERT INTO livros (titulo,autor,ano, disponivel)
#             VALUES (?, ?, ?, ?)
#         """,
#         (titulo,autor,ano, "sim")
#         )
#         conexao.commit()
#     except Exception as erro:
#         print(f"erro ao tentar cadastrar livro!{erro}")
#     finally:
#         if conexao:
#             conexao.close()


# titulo = input("Digite o titulo do livro: ").lower().strip()
# autor = input("Digite o nome do autor do livro: ").lower().strip()
# ano = input("Digite o ano de lançamento do livro: ").lower().strip()
# cadastrar_livros(titulo,autor,ano)

# def listar_livros():
#     try:
#         conexao = sqlite3.connect("biblioteca.db")
#         cursor = conexao.cursor()

#         cursor.execute("SELECT * FROM livros")
#         for linha in cursor.fetchall():
#             print(f"ID: {linha[0]}  | Titulo: {linha[1]} | Autor: {linha[2]} | Ano: {linha[3]}")
#     except Exception as erro:
#         print(f"Erro ao tentar Listar livros!")
#     finally:
#         if conexao:
#             conexao.close

# def atualizar_disponibilidade(id_livro):
#     try:
#         conexao = sqlite3.connect("biblioteca.db")
#         cursor = conexao.cursor()

#         cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
#         resultado = cursor.fetchone()
#         if resultado[0] == "sim":
#             novo_status = "não"
#         else:
#             novo_status = "sim"

#         cursor.execute("UPDATE livros SET disponivel = ? WHERE id = ?", (novo_status, id_livro))
#         conexao.commit()
#     except Exception as erro:
#         print(f"ocorreu um erro {erro}")
#     finally:
#         conexao.close


# livro_id = input("Digite o ID do livro que deseja atualizar: ")
# atualizar_disponibilidade(livro_id)

def deletar_livros(id_livro):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))

        conexao.commit()

        if cursor.rowcount > 0:
            print("O livro foi removido com sucesso!")
        else:
            print("Nenhum livro foi encontrado com o id fornecido.")

    except Exception as erro:
        print(f"erro ao tentar excluir livro {erro}")
    finally:
        if conexao:
            conexao.close()

deletar = input("Digite o id do livro que deseja remover: ")
deletar_livros(deletar)