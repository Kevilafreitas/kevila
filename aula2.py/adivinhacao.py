#Crie JogoAdivinhacao com número sorteado entre 1 e 100, contador de tentativas e máximo de 10. Métodos adivinhar(n) e reiniciar(). Use import random.
import random

class JogoAdivinhacao:
    def __init__(self):
        self.numero_sorteado = random.randint(1, 100)
        self.tentativas = 0
        self.maximo_tentativas = 10

    def adivinhar(self, n):
        if self.tentativas >= self.maximo_tentativas:
            print("Você atingiu o limite de tentativas!")
            return

        self.tentativas += 1

        if n == self.numero_sorteado:
            print(f"Parabéns! Você acertou em {self.tentativas} tentativa(s).")
        elif n < self.numero_sorteado:
            print("O número sorteado é maior.")
        else:
            print("O número sorteado é menor.")

    def reiniciar(self):
        self.numero_sorteado = random.randint(1, 100)
        self.tentativas = 0
        print("Jogo reiniciado!")

jogo = JogoAdivinhacao()

jogo.adivinhar(50)
jogo.adivinhar(75)

jogo.reiniciar()

jogo.adivinhar(30)