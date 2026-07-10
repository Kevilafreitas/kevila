import tkinter as tk
from tkinter import messagebox

from clientes import Cliente
from repositorio_cliente import RepositorioCliente


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Gestor de Clientes")
        self.geometry("380x460")

        self.repo = RepositorioCliente()
        self.clientes = self.repo.listar()

        self.total_texto = tk.StringVar()

        self.montar_widgets()
        self.atualizar_lista()

    def montar_widgets(self):

        quadro = tk.Frame(self)
        quadro.pack(pady=10)

        tk.Label(quadro, text="Nome:").grid(row=0, column=0)

        self.campo_nome = tk.Entry(quadro, width=25)
        self.campo_nome.grid(row=0, column=1)

        tk.Label(quadro, text="E-mail:").grid(row=1, column=0)

        self.campo_email = tk.Entry(quadro, width=25)
        self.campo_email.grid(row=1, column=1)

        tk.Button(quadro,
                  text="Adicionar",
                  command=self.adicionar).grid(
                  row=2,
                  column=0,
                  columnspan=2,
                  pady=8)

        self.lista = tk.Listbox(self, width=45, height=12)
        self.lista.pack()

        tk.Label(self,
                 textvariable=self.total_texto).pack()

        quadro2 = tk.Frame(self)
        quadro2.pack(pady=10)

        tk.Button(quadro2,
                  text="Editar",
                  command=self.editar).pack(side="left", padx=5)

        tk.Button(quadro2,
                  text="Excluir",
                  command=self.excluir).pack(side="left", padx=5)

    def atualizar_lista(self):

        self.clientes = self.repo.listar()

        self.lista.delete(0, tk.END)

        for cliente in self.clientes:
            self.lista.insert(tk.END, str(cliente))

        self.total_texto.set(
            f"Total: {len(self.clientes)} cliente(s)"
        )

    def indice_selecionado(self):

        selecao = self.lista.curselection()

        if not selecao:
            messagebox.showerror(
                "Erro",
                "Selecione um cliente."
            )
            return None

        return selecao[0]

    def adicionar(self):

        nome = self.campo_nome.get()
        email = self.campo_email.get()

        if nome == "" or email == "":
            messagebox.showerror(
                "Erro",
                "Preencha todos os campos."
            )
            return

        cliente = Cliente(nome, email)

        self.repo.salvar(cliente)

        self.atualizar_lista()

        self.campo_nome.delete(0, tk.END)
        self.campo_email.delete(0, tk.END)

    def excluir(self):

        indice = self.indice_selecionado()

        if indice is None:
            return

        cliente = self.clientes[indice]

        self.repo.remover(cliente.id)

        self.atualizar_lista()

    def editar(self):

        indice = self.indice_selecionado()

        if indice is None:
            return

        cliente = self.clientes[indice]

        janela = tk.Toplevel(self)

        janela.title("Editar Cliente")

        tk.Label(janela,
                 text="Nome").grid(row=0, column=0)

        campo_nome = tk.Entry(janela)
        campo_nome.grid(row=0, column=1)
        campo_nome.insert(0, cliente.nome)

        tk.Label(janela,
                 text="Email").grid(row=1, column=0)

        campo_email = tk.Entry(janela)
        campo_email.grid(row=1, column=1)
        campo_email.insert(0, cliente.email)

        def salvar():

            cliente.nome = campo_nome.get()
            cliente.email = campo_email.get()

            self.repo.atualizar(cliente)

            self.atualizar_lista()

            janela.destroy()

        tk.Button(janela,
                  text="Salvar",
                  command=salvar).grid(
                  row=2,
                  column=0,
                  columnspan=2,
                  pady=10)

app = App()
app.mainloop()