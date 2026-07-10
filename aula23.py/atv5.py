import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agenda")
        self.geometry("300x300")
    
        self.itens = []

        self.entry = tk.Entry(self, width=30)
        self.entry.pack(pady=10)


        self.btn_adicionar = tk.Button(
        self,text="adicionar",
        command=self.adicionar )

        self.btn_adicionar.pack(pady=5)

        self.lista = tk.Listbox(self,
        width=35,
        height=10
        )

        self.lista.pack(pady=10)


        self.btn_excluir = tk.Button(self,
        text="excluir",
        command=self.excluir
        )

        self.btn_excluir.pack(pady=5)
    
    def adicionar(self):
        texto = self.entry.get().strip()
        if texto:
            self.itens.append(texto)
            self.atualizar_lista()
            self.entry.delete(0, tk.END)
                

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)

        for item in self.itens:
            self.lista.insert(tk.END, item)


    def excluir(self):
        selecionado = self.lista.curselection()
        if not selecionado:
            return
        resposta = messagebox.askyesno(
            "excluir",
            "deseja realmente excluir?"
        )
        if resposta:
            indice = selecionado[0]
            self.itens.pop(indice)
            self.atualizar_lista()




app = App()
app.mainloop()


