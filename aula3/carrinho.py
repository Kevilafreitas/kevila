#Crie Carrinho com lista de Produto. Métodos adicionar, remover e total().
#Dica Avançada: No método total(), use um for para percorrer a lista e acessar o .preco de cada produto. O __str__ deve listar os nomes dos itens e o valor final
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def remover(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                print(f"{nome} removido do carrinho.")
                return

        print(f"{nome} não encontrado no carrinho.")

    def total(self):
        soma = 0

        for produto in self.produtos:
            soma += produto.preco

        return soma

    def __str__(self):
        texto = "Itens no carrinho:\n"

        if len(self.produtos) == 0:
            texto += "Carrinho vazio.\n"
        else:
            for produto in self.produtos:
                texto += f"- {produto.nome} (R$ {produto.preco:.2f})\n"

        texto += f"Total: R$ {self.total():.2f}"

        return texto

p1 = Produto("Mouse", 50.00)
p2 = Produto("Teclado", 120.00)
p3 = Produto("Monitor", 800.00)

carrinho = Carrinho()

carrinho.adicionar(p1)
carrinho.adicionar(p2)
carrinho.adicionar(p3)

print(carrinho)

carrinho.remover("Teclado")

print("\nApós remover:")
print(carrinho)