#Crie Personagem com vida=100, ataque e defesa. Método atacar(outro) — dano = max(0, ataque − defesa do outro) — e esta_vivo(). Simule um combate em loop.
class Personagem:
    def __init__(self, nome, ataque, defesa):
        self.nome = nome
        self.vida = 100
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, outro):
        dano = max(0, self.ataque - outro.defesa)
        outro.vida -= dano

        if outro.vida < 0:
            outro.vida = 0

        print(f"{self.nome} atacou {outro.nome} e causou {dano} de dano.")
        print(f"Vida de {outro.nome}: {outro.vida}")

    def esta_vivo(self):
        return self.vida > 0

guerreiro = Personagem("Guerreiro", 20, 5)
orc = Personagem("Orc", 15, 3)

rodada = 1

while guerreiro.esta_vivo() and orc.esta_vivo():
    print(f"\n--- Rodada {rodada} ---")

    guerreiro.atacar(orc)

    if orc.esta_vivo():
        orc.atacar(guerreiro)

    rodada += 1

print("\n***** Fim do Combate ****")

if guerreiro.esta_vivo():
    print(f"{guerreiro.nome} venceu!")
else:
    print(f"{orc.nome} venceu!")