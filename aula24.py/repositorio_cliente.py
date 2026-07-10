import sqlite3
from clientes import Cliente


class RepositorioCliente:

    def __init__(self):
        self.conexao = sqlite3.connect("clientes.db")
        self.criar_tabela()

    def criar_tabela(self):

        cursor = self.conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT
        )
        """)

        self.conexao.commit()

    def salvar(self, cliente):

        cursor = self.conexao.cursor()

        cursor.execute("""
        INSERT INTO clientes(nome, email)
        VALUES (?, ?)
        """, (cliente.nome, cliente.email))

        self.conexao.commit()

    def listar(self):

        cursor = self.conexao.cursor()

        cursor.execute("""
        SELECT id, nome, email
        FROM clientes
        """)

        linhas = cursor.fetchall()

        clientes = []

        for id_cliente, nome, email in linhas:
            clientes.append(Cliente(nome, email, id_cliente))

        return clientes

    def remover(self, id_cliente):

        cursor = self.conexao.cursor()

        cursor.execute("""
        DELETE FROM clientes
        WHERE id = ?
        """, (id_cliente,))

        self.conexao.commit()

    def atualizar(self, cliente):

        cursor = self.conexao.cursor()

        cursor.execute("""
        UPDATE clientes
        SET nome = ?, email = ?
        WHERE id = ?
        """, (cliente.nome, cliente.email, cliente.id))

        self.conexao.commit()