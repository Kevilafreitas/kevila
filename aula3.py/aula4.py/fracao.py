#Crie Fracao com _numerador e _denominador. Setter do denominador impede zero. @property valor retorna o resultado. __add__ e __eq__ para somar e comparar frações.
class Fracao:
    def __init__(self, numerador, denominador):
        self._numerador = numerador
        self.denominador = denominador 

    @property
    def denominador(self):
        return self._denominador

    @denominador.setter
    def denominador(self, valor):
        if valor == 0:
            raise ValueError("O denominador não pode ser zero.")
        self._denominador = valor

    @property
    def valor(self):
        return self._numerador / self._denominador
    
    def __add__(self, outra):
        novo_numerador = (
            self._numerador * outra._denominador +
            outra._numerador * self._denominador
        )
        novo_denominador = (
            self._denominador * outra._denominador
        )
        return Fracao(novo_numerador, novo_denominador)
    def __eq__(self, outra):
        return (
            self._numerador * outra._denominador ==
            outra._numerador * self._denominador
        )
    def __str__(self):
        return f"{self._numerador}/{self._denominador}"

f1 = Fracao(1, 2)
f2 = Fracao(3, 4)

soma = f1 + f2
print("Fração 1:", f1)
print("Fração 2:", f2)
print("Soma:", soma)
print("Valor da soma:", soma.valor)

f3 = Fracao(2, 4)
print("f1 == f3 ?", f1 == f3)