#Crie Categoria, Produto (agrega Categoria), ItemPedido e Pedido (composição de itens). Pedido deve ter cliente (agregação de Cliente), status='aberto' e método fechar() que valida estoque antes de confirmar. Se qualquer item não tiver estoque suficiente, lança ValueError.
class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, nome, preco, estoque, categoria):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria 

class Cliente:
    def __init__(self, nome):
        self.nome = nome

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    @property
    def subtotal(self):
        return self.produto.preco * self.quantidade
    
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente    
        self.itens = []          
        self.status = "aberto"

    def adicionar_item(self, produto, quantidade):
        item = ItemPedido(produto, quantidade)
        self.itens.append(item)

    def fechar(self):
        for item in self.itens:
            if item.quantidade > item.produto.estoque:
                raise ValueError(
                    f"Estoque insuficiente para {item.produto.nome}"
                )
        
        for item in self.itens:
            item.produto.estoque -= item.quantidade

        self.status = "fechado"
    def total(self):
        total = 0
        for item in self.itens:
            total += item.subtotal
        return total

cat = Categoria("Eletrônicos")

p1 = Produto("Notebook", 3500, 5, cat)
p2 = Produto("Mouse", 80, 10, cat)
cliente = Cliente("Ana")
pedido = Pedido(cliente)

pedido.adicionar_item(p1, 2)
pedido.adicionar_item(p2, 3)

try:
    pedido.fechar()
    print("Pedido confirmado!")
    print("Status:", pedido.status)
    print("Total: R$", pedido.total())
except ValueError as erro:
    print("Erro:", erro)

print("Estoque Notebook:", p1.estoque)
print("Estoque Mouse:", p2.estoque)