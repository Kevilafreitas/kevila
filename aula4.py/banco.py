#Crie Banco com _contas (lista privada). Métodos abrir_conta, fechar_conta, buscar_conta. @property total_em_depositos soma todos os saldos de todas as contas cadastradas.
class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"Conta: {self.numero} | Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}"

class Banco:
    def __init__(self):
        self._contas = [] 

    def abrir_conta(self, conta):
        self._contas.append(conta)
        print(f"Conta {conta.numero} aberta com sucesso.")

    def fechar_conta(self, numero):
        for conta in self._contas:
            if conta.numero == numero:
                self._contas.remove(conta)
                print(f"Conta {numero} fechada com sucesso.")
                return
        print("Conta não encontrada.")

    def buscar_conta(self, numero):
        for conta in self._contas:
            if conta.numero == numero:
                return conta

        return None
    @property
    def total_em_depositos(self):
        total = 0
        for conta in self._contas:
            total += conta.saldo
        return total

c1 = Conta(101, "Ana", 1500)
c2 = Conta(102, "Carlos", 2500)
c3 = Conta(103, "Maria", 1000)

banco = Banco()

banco.abrir_conta(c1)
banco.abrir_conta(c2)
banco.abrir_conta(c3)
print("\nBuscar conta:")
conta = banco.buscar_conta(102)

if conta:
    print(conta)

print("\nTotal em depósitos:")
print(f"R$ {banco.total_em_depositos:.2f}")

print("\nFechando conta 103...")
banco.fechar_conta(103)

print("\nNovo total em depósitos:")
print(f"R$ {banco.total_em_depositos:.2f}")