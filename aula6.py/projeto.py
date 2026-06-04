class Tenis: 
    def __init__(self, marca, modelo, tamanho, preco, estoque):
        self.marca = marca
        self.modelo = modelo
        self.tamanho = tamanho
        self._preco = preco
        self._estoque = estoque

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if valor > 0:
             self._preco = valor
        else: 
            print("O preço não pode ser negativo")
    

    @property
    def estoque(self):
        return self._estoque
    
    @estoque.setter
    def estoque(self, qtd):
        if qtd > 0:
            self._estoque = qtd
        else:
            print("Estoque não pode ser negativo")

    def __str__(self):
        return f"Tenis: {self.modelo}, {self.marca} | tamanho: {self.tamanho} | preco: {self.preco} | estoque: {self.estoque}" 


   
class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, tenis):
        if tenis.estoque > 0:
            self.itens.append(tenis)
            tenis.estoque -= 1
        else:
            print ("Produto sem estoque")

    def remover_item(self, tenis):
        if tenis in self.itens:
            self.itens.remove(tenis)
            tenis.estoque += 1

    def __str__(self):
        total = 0
        for item in self.itens:
            total += item.preco
        return f"Itens no carrinho: {len(self.itens)} | Total: R$ {total}"


tenis1 = Tenis("Nike", "Air Max", 42, 500, 5)
tenis2 = Tenis("Adidas", "Ultraboost", 40, 600, 10)

carrinho = Carrinho()

carrinho.adicionar_item(tenis1)
carrinho.adicionar_item(tenis2)

print(tenis1)
print(tenis2)
print(carrinho)

carrinho.remover_item(tenis2)
print(carrinho)