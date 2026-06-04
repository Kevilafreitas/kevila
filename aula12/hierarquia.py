#Crie ContaError(Exception) como base, e duas filhas: SaldoInsuficienteError e ValorInvalidoError. Refatore a ContaBancaria do laboratório pra levantar as filhas. No main, mostre que um único except ContaError captura as duas — porque ambas herdam da base. Foco: herança aplicada a exceções (a hierarquia da aula).
class ContaError(Exception):
    pass

class SaldoInsuficienteError(ContaError):
    pass

class ValorInvalidoError(ContaError):
    pass

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError(
                "O valor do depósito deve ser maior que zero."
            )

        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado.")

    def sacar(self, valor):
        if valor <= 0:
            raise ValorInvalidoError(
                "O valor do saque deve ser maior que zero."
            )

        if valor > self.saldo:
            raise SaldoInsuficienteError(
                "Saldo insuficiente para realizar o saque."
            )

        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado.")

    def exibir(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")


conta = ContaBancaria("Ana", 100)

try:
    conta.depositar(-50)

except ContaError as erro:
    print("Erro da conta:", erro)

try:
    conta.sacar(500)

except ContaError as erro:
    print("Erro da conta:", erro)