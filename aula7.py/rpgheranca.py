#Sistemas de jogos: Crie Entidade base (nome, vida). Crie Heroi (adiciona mana) e Inimigo (adiciona drop_xp). Implemente uma lógica de batalha simples onde ambos manipulam os atributos herdado
class Entidade:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def esta_vivo(self):
        return self.vida > 0

class Heroi(Entidade):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def atacar(self, inimigo):
        dano = 20
        inimigo.vida -= dano

        if inimigo.vida < 0:
            inimigo.vida = 0
        print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano.")
        print(f"Vida de {inimigo.nome}: {inimigo.vida}")


class Inimigo(Entidade):
    def __init__(self, nome, vida, drop_xp):
        super().__init__(nome, vida)
        self.drop_xp = drop_xp

    def atacar(self, heroi):
        dano = 15
        heroi.vida -= dano
        if heroi.vida < 0:
            heroi.vida = 0
        print(f"{self.nome} atacou {heroi.nome} causando {dano} de dano.")
        print(f"Vida de {heroi.nome}: {heroi.vida}")


heroi = Heroi("Guerreiro", 100, 50)
inimigo = Inimigo("Orc", 80, 100)

rodada = 1

while heroi.esta_vivo() and inimigo.esta_vivo():
    print(f"\n--- Rodada {rodada} ---")

    heroi.atacar(inimigo)

    if inimigo.esta_vivo():
        inimigo.atacar(heroi)

    rodada += 1

print("\n***** Fim da batalha ****")

if heroi.esta_vivo():
    print(f"{heroi.nome} venceu!")
    print(f"Ganhou {inimigo.drop_xp} XP.")
else:
    print(f"{inimigo.nome} venceu!")