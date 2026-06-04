#crie Disciplina com nome e lista de alunos (objetos da classe Aluno). Métodos matricular(), media_disciplina() (percorre os alunos e calcula a média geral) e listar_aprovados(). Use @classmethod para criar uma disciplina com nome padrão.
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)


class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular(self, aluno):
        self.alunos.append(aluno)

    def media_disciplina(self):
        if len(self.alunos) == 0:
            return 0

        soma_medias = 0

        for aluno in self.alunos:
            soma_medias += aluno.calcular_media()

        return soma_medias / len(self.alunos)

    def listar_aprovados(self):
        print("Alunos aprovados:")

        for aluno in self.alunos:
            if aluno.calcular_media() >= 6:
                print(f"{aluno.nome} - Média: {aluno.calcular_media():.2f}")

    @classmethod
    def criar_padrao(cls):
        return cls("Programação Orientada a Objetos")

aluno1 = Aluno("Ana", [8, 7, 9])
aluno2 = Aluno("Carlos", [5, 4, 6])
aluno3 = Aluno("Maria", [10, 9, 8])

disciplina = Disciplina.criar_padrao()

disciplina.matricular(aluno1)
disciplina.matricular(aluno2)
disciplina.matricular(aluno3)

print("Disciplina:", disciplina.nome)

print("\nMédia da disciplina:")
print(f"{disciplina.media_disciplina():.2f}")

print()
disciplina.listar_aprovados()