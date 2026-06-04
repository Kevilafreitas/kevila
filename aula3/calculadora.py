#Evolua a calculadora da aula 01 para uma classe com historico. Cada operação registra um texto descritivo na lista. Método ver_historico() exibe tudo. @classmethod limpar_tudo() reseta a instância.
class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado

    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            self.historico.append(f"{a} / {b} = Erro (divisão por zero)")
            return "Erro: divisão por zero"

        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        return resultado

    def ver_historico(self):
        print("Histórico de operações:")
        
        if len(self.historico) == 0:
            print("Nenhuma operação realizada.")
            return

        for operacao in self.historico:
            print(operacao)

    @classmethod
    def limpar_tudo(cls):
        return cls()