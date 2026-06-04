#Polimorfismo inicial: Crie Produto base. Crie Smartphone e Notebook com especificações únicas. Crie uma classe Carrinho que aceita qualquer um deles e calcula o valor total da compra.
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_info(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

class Smartphone(Produto):
    def __init__(self, nome, preco, armazenamento):
        super().__init__(nome, preco)
        self.armazenamento = armazenamento

    def exibir_info(self):
        return (f"Smartphone: {self.nome} | "
                f"Armazenamento: {self.armazenamento}GB | "
                f"Preço: R$ {self.preco:.2f}")

class Notebook(Produto):
    def __init__(self, nome, preco, memoria_ram):
        super().__init__(nome, preco)
        self.memoria_ram = memoria_ram

    def exibir_info(self):
        return (f"Notebook: {self.nome} | "
                f"RAM: {self.memoria_ram}GB | "
                f"Preço: R$ {self.preco:.2f}")

class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.preco
        return soma

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.exibir_info())

celular = Smartphone("Galaxy S25", 4500, 256)
notebook = Notebook("Dell Inspiron", 3500, 16)

carrinho = Carrinho()

carrinho.adicionar(celular)
carrinho.adicionar(notebook)

print("Produtos no carrinho:")
carrinho.listar_produtos()
print(f"\nTotal da compra: R$ {carrinho.total():.2f}")