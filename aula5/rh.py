#Crie Cargo com titulo e salario_base. Crie Funcionario que recebe um Cargo (agregação) e tem bonus=0.0. @property salario_total retorna base + bonus. Crie Departamento que agrega funcionários. Método folha_pagamento() soma todos os salários totais.
class Cargo:
    def __init__(self, titulo, salario_base):
        self.titulo = titulo
        self.salario_base = salario_base


class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo 
        self.bonus = 0.0

    @property
    def salario_total(self):
        return self.cargo.salario_base + self.bonus


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def folha_pagamento(self):
        total = 0
        for funcionario in self.funcionarios:
            total += funcionario.salario_total
        return total


cargo1 = Cargo("Desenvolvedor", 5000)
cargo2 = Cargo("Analista", 4000)

func1 = Funcionario("Ana", cargo1)
func2 = Funcionario("Carlos", cargo2)

func1.bonus = 1000
func2.bonus = 500

dep = Departamento("TI")

dep.adicionar_funcionario(func1)
dep.adicionar_funcionario(func2)

print(f"{func1.nome}: R$ {func1.salario_total:.2f}")
print(f"{func2.nome}: R$ {func2.salario_total:.2f}")

print(f"Folha de pagamento: R$ {dep.folha_pagamento():.2f}")