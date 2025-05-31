import sqlite3


with sqlite3.connect('meu_banco.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM authors")
    autores = cursor.fetchall()
    print(autores)


