#Crie uma função chamada tabuada(numero) que imprima a tabuada completa de 1 a 10 desse número. Use um loop for com range(1, 11).
    class Tabuada:
    def tabuada(self, numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")


# Criando o objeto
t = Tabuada()

# Pedindo o número ao usuário
numero = int(input("Digite um número: "))

# Chamando o método
t.tabuada(numero)
